# Patsnap Query Rules

> 字段和语法用于构建检索式；实际调用以工具schema为准，未执行的语法需标明待验证。参见[工具使用要点](tool-usage.md)。

Use this reference when converting a technical theme into a Patsnap search formula. If the user provides Patsnap's exact field names or examples, follow those over this generic guidance.

These rules are based on Patsnap Search Helper, the user's Search Helper screenshots, and Patsnap Help Center behavior. These syntax references do not prove that a formula has been executed. Check current tool schemas and record the outcome of any validation.

## Core Syntax

### Boolean and Grouping

- Use `AND`, `OR`, and `NOT` in uppercase for readability.
- Default Patsnap field-search logic is `NOT > AND > OR` unless the user changes search settings to interpret by input order.
- Always use parentheses to preserve intent, especially around synonym groups and exclusions.
- Use quotation marks for exact phrases. Without quotation marks, Patsnap treats words in a phrase like separate terms joined by `AND`.
- When no logical operator is written between two keywords, Patsnap performs `AND`.
- Position operators have higher priority than logical operators.

```text
(keyword1 AND keyword2) OR ("exact phrase" AND keyword3)
```

### Logical Operators

| Operator | Use | Example |
| --- | --- | --- |
| `AND` | Both sides must exist; order does not matter. Also used implicitly between terms with no operator. | `太阳能 AND 电池`; `TTL:纳米 AND AN:清华大学` |
| `OR` | At least one side must exist. Use for synonyms, alternatives, and equivalent search conditions. | `发动机 OR 引擎`; `TTL:非晶硅电池 OR IPC:H01L31/075` |
| `NOT` | Exclude records matching the following condition from the preceding result set. | `电视 NOT 等离子`; `AN:华为科技 NOT ABST:手机` |
| `GAND` | Limit search to matched members in an event group or paired field group. | `EPDS:DE GAND EPDS_SLS:1` |

Use `GAND` only for supported grouped-event fields, including award name/level/session, EP designated state/legal status groups, citation relationship groups, enterprise custom fields, and company workspace fields. For normal keyword logic, use `AND`.

### Fielded Search

Field syntax is:

```text
FIELD:(term1 OR term2)
FIELD:single_term
```

Common high-value fields and examples:

| Field | Meaning | Example |
| --- | --- | --- |
| `TAC` | Title, abstract, claims | `TAC:("solid electrolyte" OR sulfide)` |
| `TACD` | Title, abstract, claims, description | `TACD:(battery $W5 separator)` |
| `TTL` | Title | `TTL:(electr*)` |
| `CLMS` | Claims | `CLMS:("prosthetic hip" OR "hip replacement")` |
| `AN` | Original assignee/applicant | `AN:(Nintendo)` |
| `ALL_AN` | All assignee fields; useful for exclusions | `NOT ALL_AN:(Nokia)` |
| `AUTHORITY` | Patent authority/jurisdiction | `AUTHORITY:(US OR EP OR CN)` |
| `IPC` | IPC classification | `IPC:(H01M)` |
| `CPC` | CPC classification | `CPC:(H01M)` |
| `PBD_Y` | Publication year | `PBD_Y:[2010 to *]` |

Patsnap contains many additional fields in Search Helper. If a field is not confirmed by the current MCP declaration or supplied reference, mark it unverified; do not invent unsupported field names.

For the full field abbreviation list parsed from the user's document, read `searchable-fields.md` before producing an executable formula.

### Classification Field Scope

Be explicit about classification field scope. In Patsnap, `IPC:C22B3/00` is not equivalent to `IPC_LOW:C22B3/00`.

| Need | Use | Meaning |
| --- | --- | --- |
| Retrieve only records assigned to the exact IPC/CPC code as expressed by the field | `IPC:(C22B3/00)` or `CPC:(C22B3/00)` | Exact/current classification-code match; do not assume all lower subgroups are included |
| Retrieve records under a main group and all lower subgroups | `IPC_LOW:(C22B3/00)` or `CPC_LOW:(C22B3/00)` | Lower-level/descendant classification retrieval |
| Retrieve a broad technology branch from a known parent group | Prefer `_LOW` fields | Prevent missing records classified only in subgroups |
| Use classification as a precision filter for a specific subgroup | Use exact `IPC/CPC` or the exact lower subgroup | Avoid over-broad main-group recall |

Rule: if the intent is "C22B3/00大组下的所有小组", use `IPC_LOW:C22B3/00`, not `IPC:C22B3/00`. Apply the same logic to `CPC_LOW`.

### Classification-Based Noise Blocks

When result review shows a stable cross-domain noise cluster, use classification fields as part of the noise block. Prefer classification plus keyword/context exclusions over applicant-only exclusions, because applicants may work across domains and applicant names do not explain the technical cause.

Examples:

| Noise cluster | Typical fields | Use |
| --- | --- | --- |
| Pesticide/agrochemical noise | `IPC_LOW:A01N`, `IPC_LOW:A01P`, `CPC_LOW:A01N`, `CPC_LOW:A01P` | Exclude when the technical topic is not agriculture, pesticides, biocides, fungicides, herbicides, insecticides, nematicides, or crop protection |
| Medical/pharmaceutical noise | `IPC_LOW:A61K`, `IPC_LOW:A61P`, `CPC_LOW:A61K`, `CPC_LOW:A61P` | Exclude when the topic is not therapeutic, pharmaceutical, diagnostic, or medical |
| Food/agriculture noise | `IPC_LOW:A23`, `IPC_LOW:A01` | Exclude when food/agriculture is outside the boundary |

For a non-agriculture topic where pesticide records are confirmed false positives, create a named block:

```text
AGRI_NOISE =
(IPC_LOW:A01N OR IPC_LOW:A01P OR CPC_LOW:A01N OR CPC_LOW:A01P)
OR TACD:(农药 OR 杀虫剂 OR 杀菌剂 OR 杀真菌剂 OR 杀线虫剂 OR 除草剂 OR 作物保护 OR 植物保护 OR 农用化学 OR 农业制剂 OR 植物病原性真菌 OR fungicide OR pesticide OR insecticide OR herbicide OR nematicide OR crop protection OR agrochemical OR plant pathogen)
```

Do not add a broad classification noise block blindly. Add it when sample review shows that the cluster is stable noise and not a legitimate adjacent application.

### Wildcards

Use wildcards mainly when stemming is off and after checking ambiguity:

| Wildcard | Meaning | Example |
| --- | --- | --- |
| `*` | Zero or more characters; can appear at beginning, middle, or end | `electr*` |
| `?` | Exactly one character | `organi?er` |
| `#` | Zero or one character | `colo#r` |

Wildcard constraints from Search Helper:

- Do not use wildcards inside quotation marks.
- In one keyword, `*` may be used at most twice and cannot be combined with other wildcards.
- When `*` is used in the middle of a word, it can represent unlimited characters and the prefix must keep at least 2 characters.
- When `*` is used at both beginning and end, the middle term must keep at least 3 characters.
- `?` can be repeated, but repeated question marks must be contiguous.
- In one keyword, `#` may be used at most once and cannot be combined with other wildcards.
- In stemming-on mode, wildcard truncation does not apply to that keyword.
- In proximity queries, wildcards can be used only inside the keyword; truncation does not apply to the wildcarded keyword.
- In stemming mode or in suffix wildcard usage, title/abstract/claims/description-related fields support English only.

Examples:

```text
*otor
*oto*
EP200*B2
?otor
US7654???
#otor
m#tor
```

### Position Connectors

Use proximity when `AND` is too loose but exact phrases are too narrow:

| Connector | Meaning | Example |
| --- | --- | --- |
| `$Wn` | Terms within n words, any order | `protein $W3 analysis` |
| `$PREn` | First term before second term within n words | `data $PRE4 line` |
| `$WS` | Terms within 99 words, any order | `display $WS HDMI` |
| `$SEN` | Terms in the same sentence | `cathode $SEN coating` |
| `$PARA` | Terms in the same paragraph | `separator $PARA electrolyte` |

Prefer `$Wn`, `$SEN`, or `$PARA` over plain `AND` when the relationship between terms matters.

`n` supports `0 <= n <= 99`.

### Proximity Modeling Patterns

Use these patterns to avoid flat `AND`/`OR` formulas that are either too noisy or too brittle.

| Pattern | When to use | Preferred expression |
| --- | --- | --- |
| Fixed phrase with minor inserted words | Chinese/English compound scenario terms such as 锂电池回收, 废旧动力电池回收, cathode material recycling | `(对象 $W5-9 动作)` |
| Ordered technical relation | A must appear before B, such as precursor -> product, process -> output, or modifier -> object | `(A $PREn B)` |
| Element/material system | Several materials/elements must co-occur as one system, such as Ni-Co-Mn | `((A $Wn B) $Wn C)` plus order variants |
| Object-action relation | High-frequency object terms need to be tied to operations, such as metal + separation/recovery | `(对象 $Wn 动作)` |
| Effect/application relation | A function or effect applies to a product/application | `(对象 $SEN 功效)` or `(对象 $Wn 功效)` |
| Method-equipment relation | A process is carried out in/on an apparatus | `(方法 $SEN 设备)` or `(方法 $Wn 设备)` |
| Description-only background | Relationship may span longer text but should remain related | `$PARA`, or a broader field with later denoising |

Recommended starting windows:

- `$W0-$W2`: tight phrase variants, equivalent to near-exact terms.
- `$W3-$W5`: common compound technical expressions and element systems.
- `$W5-$W9`: application scenarios with inserted qualifiers, such as 废旧锂离子动力电池正极材料回收.
- `$SEN`: when multiple keywords must be in the same sentence but order/distance is uncertain.
- `$PARA`: only when the concept is often explained across a paragraph; expect more noise and validate precision.

Always tune the window after reading retrieved patent wording. If noise is high, narrow the window or move one concept to `TAC`; if recall misses known samples, widen slightly or move the secondary concept to `TACD`.

Examples:

```text
((锂电池 OR 锂离子电池 OR 动力电池 OR 正极材料) $W7 (回收 OR 再生 OR 资源化 OR 湿法 OR 浸出))

((black mass OR cathode powder) $W5 (battery OR lithium OR recycling OR leachate))

((镍 $W5 钴) $W5 锰) OR ((镍 $W5 锰) $W5 钴)

((nickel OR cobalt OR manganese) $W5 (extract* OR separat* OR recover*))

((固态 OR 固体 OR 聚合物) $PRE3 电池)
```

### Feedback-Derived Translation Variants

When missed relevant samples are mostly non-English patents or machine translations, inspect how the concept is translated in title, abstract, claims, and AI-generated fields. Add a dedicated recall branch for systematic translation variants, not a global broadening of the main formula.

Rules:

- Keep broad translated words inside a strongly constrained branch. For example, `提取` may be a translation of extraction, but it is too broad unless combined with battery recovery, metal system, and extraction/extractant context.
- Include machine-translation variants for known terms when they recur across missed samples, such as `黑色物质`, `黑色聚集体`, or `黑块` for black mass.
- Include domain process abbreviations such as `SSX` only with application and object constraints.
- If a missed sample does not contain the core technical concept and only belongs to a neighboring boundary, record it as a boundary sample rather than forcing the core formula to cover it.

Example branch:

```text
S_LANGUAGE_RECALL =
(
  BATTERY_RECOVERY_BLOCK
  OR TACD:(回收的电池 OR 黑色物质 OR 黑色聚集体 OR 黑块 OR 废旧二次电池 OR 废弃二次电池 OR 使用过的电池 OR 非新锂电池 OR 电池粉末 OR 电池材料)
)
AND
(
  SOLVENT_EXTRACTION_BLOCK
  OR TACD:(溶剂提取 OR 选择性提取 OR 溶液提取 OR 提取剂 OR 提取物 OR 选择性反萃取 OR 酸性萃取剂 OR SSX)
)
AND
(
  TARGET_OBJECT_BLOCK
)
AND
(
  CORE_TECH_BLOCK
  OR TACD:(酸性萃取剂 OR 酸性提取剂 OR known trade names / seed-derived terms)
)
```

Validate this branch separately. It is usually a recall branch, not a high-precision branch.

### Chemical-Class Expansion

For chemical-class topics, do not stop at the class name. Expand the class through concrete members, salts, derivatives, process states, trade names, and structural classification anchors, then keep noisy lower members inside constrained branches.

Rules:

- Include representative lower members and homologues when they are technically plausible. For example, a carboxylic-acid topic may need `甲酸`, `乙酸`, `丙酸`, `丁酸`, `脂肪酸`, `formic acid`, `acetic acid`, `propionic acid`, and `butyric acid`.
- Include class morphology variants in Chinese, such as `羧酸型`, `羧酸系`, `羧酸萃取`, and `羧酸类萃取剂`, when user feedback or missed samples show direct class terms are insufficient.
- Include process-state terms that appear in the field, such as `皂化/saponification`, `共萃取/co-extraction`, and `协同萃取/synergistic extraction`, when they describe how the chemical class is used.
- Include structural classification anchors only with application/process/object constraints. For carboxylic-acid extractant topics, `C07C` can support carboxylic structures, `C07F9/00` can support organophosphorus comparison or synergistic systems, and `B01D11/04` can support liquid-liquid extraction equipment, but none of them should stand alone as a positive formula.
- Treat very broad lower members as recall aids, not proof of relevance. For example, `甲酸` and `乙酸` are carboxylic acids but often indicate leaching or pH adjustment, so require extraction context, application context, and target-object context.

### Frequency Operator

Use `$FREQn` to require that a keyword appears at least n times in a specified field:

```text
汽车 $FREQ2
TTL:("car" $FREQ2) AND ABST:("engine")
```

Rules:

- Supported fields include title, abstract, claims, description, and their combined fields.
- Machine-translated fields are not supported.
- `n` has a maximum value of 50.
- If stemming is on, Patsnap counts expanded stemming variants together.
- Frequency works only for a single keyword or phrase.
- Frequency search is available only in the publication database.

### Ranges, Exact Phrases, Separators, and Stemming

Use square brackets for ranges:

```text
PBD:[20010101 TO 20101231]
IPC:[H01L31/0203 TO H01L31/042]
```

Use quotation marks when word order must be fixed:

```text
"electric vehicle"
```

Use `_` as an optional separator inside a keyword to match space, hyphen, underscore, and no-separator variants. Treat `_` as a single searchable character when used in the following cases: inside quotation marks, multiple `_` in one keyword, `_` combined with another wildcard, or `_` at the beginning/end of a term.

```text
T_shirt
```

This can match `T shirt`, `T-shirt`, and `Tshirt`.

Stemming behavior:

- When stemming is on, Patsnap searches the original word and expanded singular/plural/tense variants. For example, `come` may expand to `come`, `comes`, `came`, `coming`.
- When stemming is off, only the original keyword is searched.
- Stemming only affects English keywords.
- Stemming does not work in applicant, inventor, and other name fields.

### Corporate Tree Search

Use `TREE@` to search a name and all lower-level companies in the Patsnap corporate tree. The company name after `TREE@` must be the full name of a company node in the Patsnap corporate tree.

```text
ANCS:(TREE@"拜耳股份公司")
```

`TREE@` is supported under `ANS`, `ANCS`, and `ALL_AN`.

### Special Characters

Patsnap supports special-character searching for characters including:

```text
-, /, °C, °F, %, ±, °, ™, ©, mg/L, @
```

Example:

```text
ABST:(85°C)
```

## Field Strategy

Build queries by information reliability:

| Layer | Use | Typical fields to map in Patsnap |
| --- | --- | --- |
| Core text | Main technology concept | title, abstract, claims, title/abstract/claims combined |
| Bibliographic | Scope and filtering | publication/application date, publication country, patent type, legal status |
| Classification | Recall expansion and quality checks | IPC, CPC, Locarno or domain-specific classification |
| Entity | Seed mining or optional focus | applicant, current assignee, inventor, agency, applicant group |
| Relationship | Expansion and validation | cited patents, citing patents, simple family, INPADOC family, priority |

Prefer `TAC` for balanced technology-topic searching because title, abstract, and claims are high-signal fields. Use `TACD` only when recall is insufficient or when technical terms are likely to appear in description but not claims. Use `CLMS` or independent-claims fields when the user needs high precision around protected technical features.

Do not invent exact Patsnap field codes when they are unknown. Use readable placeholders such as:

```text
TAC=(...technology terms...)
AND IPC=(...classification codes...)
NOT TAC=(...noise terms...)
```

Then add a note: "Replace field placeholders with the user's Patsnap field syntax before execution."

## Concept Blocks

Write each formula as named blocks before merging:

```text
A_OBJECT = (...materials/components/entities...)
B_ACTION = (...processes/mechanisms/functions...)
C_APPLICATION = (...scenarios/end products...)
D_CLASS = (...IPC/CPC...)
E_EXCLUDE = (...false-positive domains...)

FINAL = (A_OBJECT AND (B_ACTION OR C_APPLICATION)) OR D_CLASS
FINAL_PRECISION = FINAL NOT E_EXCLUDE
```

Keep Chinese and English terms in the same concept block when both are relevant. Include abbreviations only after checking ambiguity.

### Explicit-Term And Functional-Inference Layers

When a concept can be expressed either explicitly or implicitly through domain context, split it into two layers:

- **Explicit layer**: the record directly names the role, such as `carboxylic acid extractant`, `羧酸萃取剂`, or `solid electrolyte`.
- **Functional-inference layer**: the record names the material/object but not the role, and the role is inferred from nearby process, function, or application context, such as `carboxylic acid` appearing with `solvent extraction`, `organic phase`, `stripping`, or metal separation.

Use this pattern when explicit role terms are likely too narrow for domain experts:

```text
A_EXPLICIT =
TAC:(羧酸萃取剂 OR "carboxylic acid extractant")

A_FUNCTIONAL =
(
  TAC:(羧酸 OR "carboxylic acid" OR "naphthenic acid" OR "versatic acid")
  AND TACD:(溶剂萃取 OR "solvent extraction" OR extractant OR extraction OR "organic phase" OR stripping)
)
OR TAC:((羧酸 OR "carboxylic acid" OR "naphthenic acid" OR "versatic acid") $SEN (萃取 OR extractant OR extraction))
```

Rules:

- Put explicit terms in high-signal fields for precision.
- For functional-inference terms, put the core material/object in high-signal fields such as `TAC` whenever it is the core search point; place process/function/application context in `TACD` if it is broader context.
- Add same-sentence proximity expressions such as `TAC:(羧酸 $SEN 萃取)` when the material-function relationship itself should be explicit.
- Mark functional-inference records for later labeling because the material may be a reagent, pH regulator, synergist, impurity, or true extractant.
- Do not let generic material terms stand alone.

## Expansion Sources

Use these sources to expand terms:

- seed patent titles, abstracts, first claims, and independent claims;
- Patsnap keyword analytics, similar patents, citation network, and family members;
- IPC/CPC definitions and neighboring subgroups;
- papers, standards, product manuals, regulatory terms, and industry names;
- Chinese-English terminology, spelling variants, hyphenation variants, and plural/singular forms;
- chemical CAS/name/trade-name mapping when the topic involves materials or compounds.

## Operator Guidance

- Use parentheses aggressively; every `OR` cluster should have a clear boundary.
- Use `$Wn`, `$PREn`, `$WS`, `$SEN`, and `$PARA` to improve precision, especially for two common words that only matter near each other.
- For short abbreviations or high-frequency material/entity terms, avoid bare `OR` expansion when possible. Pair them with action, function, application, or object terms using proximity operators, such as `((nickel OR cobalt) $W5 (extract* OR separat* OR recover*))`.
- When several elements/materials must co-occur as one technical system, bind them with proximity operators and enumerate order variants if necessary, such as `((镍 $W5 钴) $W5 锰)` and `((nickel $W5 cobalt) $W5 manganese)`. Use the distance window as a precision/recall knob.
- For compound application-scenario phrases, pair the object and action with proximity instead of relying only on fixed phrases. Start with `$W5-$W9` when unsure, then tune from retrieved patent wording, such as `(锂电池 $W5 回收)` or `((lithium OR battery) $W7 recycl*)`.
- Before finalizing a formula, audit every flat `A AND B` block and decide whether it should be converted to a proximity expression, kept as independent concepts, or split into separate retrieval routes.
- Use truncation/wildcards only after checking ambiguity. Avoid broad stems that create uncontrollable noise.
- Avoid overusing `NOT`; prefer precise positive constraints first. Use exclusions only for stable, reviewed false positives.
- Keep date/legal/status filters outside the core technology block so the technology formula remains reusable.
- Use the same MCP natural-language query builder when appropriate and actual search/fetch records for terminology and classification evidence; do not invoke undeclared keyword/classification helpers.
- When using IPC/CPC parent groups for recall, use `IPC_LOW`/`CPC_LOW`; do not use exact `IPC`/`CPC` when the intent is to include descendant subgroups.
- For topic retrieval, prefer proximity and frequency controls before adding heavy `NOT` exclusions; they are easier to audit and usually preserve recall better.

## Query Variants

Produce separate variants when needed:

- **Broad landscape**: maximize recall; tolerate more noise; include classification and wider text fields.
- **Balanced analysis**: combine core terms with function/application filters; default for technology reports.
- **Monitoring**: more precise and stable; suitable for periodic updates.
- **Evidence mining**: narrow formulas targeted at claims, examples, or specific mechanisms.

## Patsnap Execution Notes

When executing through the specified MCP, record:

- database and collection;
- exact formula;
- search date and timezone;
- deduplication setting: publication, application, simple family, or extended family;
- actual supported filters or constraints included in the executable formula;
- result count before and after filters;
- exported fields.

## Source Notes

Key Patsnap behaviors to preserve in the skill:

- Search Helper exposes searchable fields, search syntax, and number-format guidance.
- Field Search lets users combine fields, operators, and keywords and indicates syntax errors visually.
- Search settings can choose default logic or input-order logic; default logic is `NOT > AND > OR`.
- Keyword Helper can suggest Chinese/English synonyms, hyponyms, and similar keywords.
- Classification helpers can add IPC/CPC and related classification fields.
- User-provided Search Helper screenshots define common logical operators, wildcards, proximity operators, frequency operator, range syntax, exact phrase syntax, optional separator `_`, stemming behavior, `TREE@`, and special-character handling.
