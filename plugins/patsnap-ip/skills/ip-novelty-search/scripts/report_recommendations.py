"""04：宿主编写行动建议，模板负责排版；不调用模型或保存工具状态。"""

from html import escape


def _object(value, required, optional=()):
    """严格限制展示字段，避免拼错字段后静默丢失内容。"""
    if not isinstance(value, dict) or not set(required) <= value.keys() or not value.keys() <= set(required) | set(optional):
        raise ValueError("recommendation_presentation: invalid fields")


def _text(value):
    """展示文字必须是非空字符串。"""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("recommendation_presentation: nonempty text required")


def _rows(value, stage=False):
    """条目数量由材料决定；高亮仅标注关注阶段，不表达评估结论。"""
    if not isinstance(value, list) or not value:
        raise ValueError("recommendation_presentation: nonempty list required")
    for row in value:
        _object(row, ("title", "body"), ("label", "highlight") if stage else ())
        for key, item in row.items():
            if key == "highlight":
                if type(item) is not bool:
                    raise ValueError("recommendation_presentation: highlight must be boolean")
            else:
                _text(item)
    if stage and sum(row.get("highlight", False) for row in value) > 1:
        raise ValueError("recommendation_presentation: highlight at most one stage")


class RecommendationPresentation:
    """已确认的编辑式建议章节，以及旧报告数据的无损回退。"""

    def validate_recommendation_presentation(self):
        """合并建议必须覆盖全部实际方案，不能遗漏或重复分配方案。"""
        if not self.modular:
            return
        value = self.draft["report"].get("recommendation_presentation")
        if value is None:
            return
        _object(value, ("headline", "summary_title", "summary", "sections"),
                ("eyebrow", "emphasis", "chapter_note", "closing"))
        for key in value.keys() - {"sections", "closing"}:
            _text(value[key])
        if value.get("emphasis") and value["emphasis"] not in value["headline"]:
            raise ValueError("recommendation_presentation: emphasis must occur in headline")
        if "closing" in value:
            _rows([value["closing"]])
        sections = value["sections"]
        if not isinstance(sections, list) or not sections:
            raise ValueError("recommendation_presentation: sections required")
        covered = []
        for section in sections:
            if not isinstance(section, dict):
                raise ValueError("recommendation_presentation: invalid section")
            kind = section.get("kind")
            if kind == "materials":
                _object(section, ("kind", "title", "items"), ("subtitle",))
                _rows(section["items"])
            elif kind in {"structure", "process"}:
                body_key = "points" if kind == "structure" else "stages"
                _object(section, ("kind", "title", "solutions", "lead", "introduction", body_key),
                        ("notes", "focus"))
                names = section["solutions"]
                if not isinstance(names, list) or not names or any(not isinstance(n, str) or n not in self.solution_keys for n in names):
                    raise ValueError("recommendation_presentation: unknown solution")
                covered.extend(names)
                _text(section["lead"])
                _text(section["introduction"])
                _rows(section[body_key], stage=kind == "process")
                if "notes" in section:
                    _rows(section["notes"])
                if "focus" in section:
                    _rows([section["focus"]])
            else:
                raise ValueError("recommendation_presentation: unknown section kind")
            _text(section["title"])
            if "subtitle" in section:
                _text(section["subtitle"])
        if len(covered) != len(set(covered)) or set(covered) != set(self.solution_keys):
            raise ValueError("recommendation_presentation: cover every solution exactly once")

    def recommendation_section(self, index, title, subtitle, body, anchors=""):
        """统一左侧章节索引、右侧内容，并保留每个方案原有定位锚点。"""
        return (
            f'<section class="report-advice-section">{anchors}'
            f'<header class="report-advice-label"><span class="report-advice-number">{index:02d}</span>'
            f'<h3>{escape(title)}</h3>{subtitle}</header><div class="report-advice-content">{body}</div></section>'
        )

    def recommendation_rows(self, rows, css):
        """标题只作纯文字，正文复用安全 Markdown 渲染。"""
        return "".join(
            f'<div class="{css}"><strong>{escape(row["title"])}</strong>'
            f'<div class="report-advice-copy">{self.markdown(row["body"])}</div></div>'
            for row in rows
        )

    def recommendation_chapter(self):
        """按保存的展示文案输出；旧草稿仍完整展示逐方案建议。"""
        value = self.draft["report"].get("recommendation_presentation")
        if value is None:
            return '<div class="report-advice">' + "".join(
                self.recommendation_section(
                    index, solution["name"], "",
                    self.recommendation_body(self.findings[solution["name"]]),
                    f'<span class="report-advice-anchor" id="recommendations-{self.solution_keys[solution["name"]]}"></span>',
                )
                for index, solution in enumerate(self.solutions, 1)
            ) + '</div>'
        headline = escape(value["headline"])
        if value.get("emphasis"):
            emphasis = escape(value["emphasis"])
            headline = headline.replace(emphasis, f'<span>{emphasis}</span>', 1)
        headline = headline.replace("\n", "<br>")
        eyebrow = f'<p class="report-advice-eyebrow">{escape(value["eyebrow"])}</p>' if value.get("eyebrow") else ""
        blocks = [
            f'<div class="report-advice-hero"><div>{eyebrow}<h3>{headline}</h3></div>'
            f'<aside><strong>{escape(value["summary_title"])}</strong>{self.markdown(value["summary"])}</aside></div>'
        ]
        for index, section in enumerate(value["sections"], 1):
            names = section.get("solutions", [])
            anchors = "".join(
                f'<span class="report-advice-anchor" id="recommendations-{self.solution_keys[name]}"></span>'
                for name in names
            )
            subtitle = '<p>' + '<br>'.join(escape(name) for name in names) + '</p>' if names else ""
            if section.get("subtitle"):
                subtitle += f'<p>{escape(section["subtitle"])}</p>'
            if section["kind"] == "materials":
                body = '<div class="report-advice-materials">' + self.recommendation_rows(section["items"], "report-advice-material") + '</div>'
            else:
                body = f'<h4 class="report-advice-lead">{escape(section["lead"])}</h4>{self.markdown(section["introduction"])}'
                if section["kind"] == "structure":
                    body += '<div class="report-advice-dimensions">' + self.recommendation_rows(section["points"], "report-advice-dimension") + '</div>'
                else:
                    body += '<ol class="report-advice-process">'
                    for stage in section["stages"]:
                        focus = ' class="report-advice-stage-focus"' if stage.get("highlight") else ""
                        label = f'<small>{escape(stage["label"])}</small>' if stage.get("label") else ""
                        body += f'<li{focus}>{label}<h4>{escape(stage["title"])}</h4>{self.markdown(stage["body"])}</li>'
                    body += '</ol>'
                body += self.recommendation_rows(section.get("notes", []), "report-advice-note")
                if section.get("focus"):
                    body += self.recommendation_rows([section["focus"]], "report-advice-focus")
            blocks.append(self.recommendation_section(index, section["title"], subtitle, body, anchors))
        if value.get("closing"):
            blocks.append(self.recommendation_rows([value["closing"]], "report-advice-closing"))
        return '<div class="report-advice">' + ''.join(blocks) + '</div>'
