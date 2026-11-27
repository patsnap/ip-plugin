#!/usr/bin/env python3
"""Validate novelty-search candidate retention and phase reconciliation."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROUTES = {"complete_combination", "relation", "synonym", "classification", "citation", "user_candidate"}
STAGES = {"searched", "shortlisted", "fetched", "compared", "final", "excluded"}
PRIORITIES = {"high", "normal", "background"}
RELATION_SOURCES = {"disclosure", "user_clarification", "candidate_feedback"}
DEDUP_FILL_STATUSES = {"target_met", "results_exhausted", "tool_limit", "budget_limit", "tool_error"}
REFLECTION_BASES = {"disclosure", "user_clarification", "candidate_feedback", "retrieval_sample"}
REFLECTION_DECISIONS = {"family_expand", "term_rewrite", "route_reconstruct", "request_input", "converge"}
RELATION_COVERAGE = {"covered", "partial", "missing"}
IMPLEMENTATION_DIMENSIONS = {
    "structure", "position", "connection", "kinematics", "sequence", "condition",
    "control", "material", "path", "interface", "mechanism",
}
PN_KEYS = {"publicationnumber", "publicationno", "publicationid", "publication_number", "publication_no", "pn"}
PN_RE = re.compile(r"^[A-Z]{2}[A-Z0-9]*\d[A-Z0-9]*$", re.IGNORECASE)


def _key(value: Any) -> str:
    return re.sub(r"[^a-z_]", "", str(value).lower())


def _norm_pn(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    normalized = re.sub(r"[^A-Z0-9]", "", value.upper())
    return normalized if PN_RE.fullmatch(normalized) else None


def _pn_values(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, str):
        pn = _norm_pn(value)
        if pn:
            found.add(pn)
    elif isinstance(value, list):
        for item in value:
            found.update(_pn_values(item))
    return found


def _publication_number_groups(value: Any) -> list[frozenset[str]]:
    """Return one alias group for each result object carrying a PN field."""
    groups: list[frozenset[str]] = []
    if isinstance(value, dict):
        direct: set[str] = set()
        for key, item in value.items():
            if _key(key) in PN_KEYS:
                direct.update(_pn_values(item))
        if direct:
            groups.append(frozenset(direct))
        for key, item in value.items():
            if _key(key) not in PN_KEYS:
                groups.extend(_publication_number_groups(item))
    elif isinstance(value, list):
        for item in value:
            groups.extend(_publication_number_groups(item))
    return groups


def _read_json(path: Path, errors: list[str], label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{label} does not exist: {path}")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{label} is not readable JSON: {path}: {exc}")
    return None


def _content_mentions_identity(path: Path, identities: set[str]) -> bool:
    try:
        content = path.read_text(encoding="utf-8").upper()
    except (OSError, UnicodeDecodeError):
        return False
    collapsed = re.sub(r"[^A-Z0-9]", "", content)
    return any(identity in collapsed for identity in identities)


def _refs_exist(refs: Any, root: Path, errors: list[str], context: str,
                identities: set[str] | None = None) -> bool:
    if not isinstance(refs, list) or not refs:
        errors.append(f"{context} must include non-empty evidence_refs")
        return False
    ok = True
    root = root.resolve()
    for ref in refs:
        if not isinstance(ref, str) or not ref.strip():
            errors.append(f"{context} has an invalid evidence reference")
            ok = False
            continue
        path = (root / ref).resolve()
        if not path.is_relative_to(root):
            errors.append(f"{context} evidence reference leaves task root: {ref}")
            ok = False
        elif not path.is_file():
            errors.append(f"{context} evidence file does not exist: {ref}")
            ok = False
        elif identities and not _content_mentions_identity(path, identities):
            errors.append(f"{context} evidence file does not mention candidate identity: {ref}")
            ok = False
    return ok


def _parse_date(value: Any) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def validate_ledger(data: Any, root: Path, phase: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["ledger root must be an object"]
    version = data.get("ledger_version")
    if version not in {1, 2}:
        errors.append("ledger_version must be 1 or 2")

    dedup_fill_policy = data.get("dedup_fill_policy")
    if dedup_fill_policy not in {None, "required"}:
        errors.append("dedup_fill_policy must be required when provided")
    fill_response_files: set[str] = set()
    route_reflection_policy = data.get("route_reflection_policy")
    if route_reflection_policy not in {None, "required"}:
        errors.append("route_reflection_policy must be required when provided")

    queries = data.get("queries")
    if not isinstance(queries, list) or not queries:
        errors.append("queries must be a non-empty list")
        queries = []
    query_by_id: dict[str, dict[str, Any]] = {}
    for index, query in enumerate(queries):
        context = f"queries[{index}]"
        if not isinstance(query, dict):
            errors.append(f"{context} must be an object")
            continue
        query_id = query.get("query_id")
        if not isinstance(query_id, str) or not query_id.strip():
            errors.append(f"{context}.query_id must be a non-empty string")
            continue
        if query_id in query_by_id:
            errors.append(f"duplicate query_id: {query_id}")
        query_by_id[query_id] = query
        if query.get("route") not in ROUTES:
            errors.append(f"{context}.route must be one of {sorted(ROUTES)}")
        units = query.get("comparison_unit_numbers")
        if not isinstance(units, list) or not units or any(
            not isinstance(item, int) or isinstance(item, bool) or item < 1 for item in units
        ):
            errors.append(f"{context}.comparison_unit_numbers must contain positive integers")
        if dedup_fill_policy == "required" and query.get("route") != "user_candidate":
            fill = query.get("dedup_fill")
            if not isinstance(fill, dict):
                errors.append(f"{context}.dedup_fill is required")
            else:
                signature = fill.get("query_signature")
                if not isinstance(signature, str) or not signature.strip():
                    errors.append(f"{context}.dedup_fill.query_signature must be a non-empty string")
                number_fields = (
                    "target_unique_groups", "raw_result_count",
                    "unique_identity_count", "unique_group_count",
                )
                values = {field: fill.get(field) for field in number_fields}
                if any(not isinstance(value, int) or isinstance(value, bool) for value in values.values()):
                    errors.append(f"{context}.dedup_fill counts must be integers")
                else:
                    target = values["target_unique_groups"]
                    raw = values["raw_result_count"]
                    identities = values["unique_identity_count"]
                    groups = values["unique_group_count"]
                    if target < 1 or raw < 0 or not 0 <= groups <= identities <= raw:
                        errors.append(f"{context}.dedup_fill counts are inconsistent")
                    status = fill.get("status")
                    if status == "target_met" and groups < target:
                        errors.append(f"{context}.dedup_fill target_met requires enough unique groups")
                    if status in DEDUP_FILL_STATUSES - {"target_met"} and groups >= target:
                        errors.append(f"{context}.dedup_fill must use target_met after reaching the target")
                status = fill.get("status")
                if status not in DEDUP_FILL_STATUSES:
                    errors.append(f"{context}.dedup_fill.status is invalid")
                if status in {"budget_limit", "tool_error"} and (
                    not isinstance(fill.get("limitation"), str) or not fill.get("limitation", "").strip()
                ):
                    errors.append(f"{context}.dedup_fill {status} requires limitation")
                pages = fill.get("pages")
                if not isinstance(pages, list) or not pages:
                    errors.append(f"{context}.dedup_fill.pages must be a non-empty list")
                else:
                    expected_offset = 0
                    returned_sum = 0
                    for page_index, page in enumerate(pages):
                        page_context = f"{context}.dedup_fill.pages[{page_index}]"
                        if not isinstance(page, dict):
                            errors.append(f"{page_context} must be an object")
                            continue
                        offset, limit, returned = (
                            page.get("offset"), page.get("limit"), page.get("returned_count")
                        )
                        if not all(isinstance(item, int) and not isinstance(item, bool)
                                   for item in (offset, limit, returned)):
                            errors.append(f"{page_context} offset, limit and returned_count must be integers")
                        elif offset != expected_offset or limit < 1 or returned < 0 or returned > limit:
                            errors.append(f"{page_context} pagination values are inconsistent")
                        else:
                            expected_offset += limit
                            returned_sum += returned
                        response_file = page.get("response_file")
                        if not isinstance(response_file, str) or not response_file.strip():
                            errors.append(f"{page_context}.response_file must be a non-empty string")
                        else:
                            fill_response_files.add(response_file)
                    if isinstance(fill.get("raw_result_count"), int) and returned_sum != fill.get("raw_result_count"):
                        errors.append(f"{context}.dedup_fill.raw_result_count must equal page totals")
                if phase == "final" and status not in DEDUP_FILL_STATUSES:
                    errors.append(f"{context}.dedup_fill is not terminal")
        if version == 2 and query.get("route") == "relation":
            proposition = query.get("relation_proposition")
            if not isinstance(proposition, dict):
                errors.append(f"{context}.relation_proposition is required for relation queries")
            else:
                for field in ("subject", "relation", "object_or_condition"):
                    if not isinstance(proposition.get(field), str) or not proposition.get(field, "").strip():
                        errors.append(f"{context}.relation_proposition.{field} must be a non-empty string")
                constraints = proposition.get("constraints")
                if not isinstance(constraints, list) or any(
                    not isinstance(item, str) or not item.strip() for item in constraints
                ):
                    errors.append(f"{context}.relation_proposition.constraints must be a list of strings")
                source = proposition.get("source")
                if source not in RELATION_SOURCES:
                    errors.append(
                        f"{context}.relation_proposition.source must be one of {sorted(RELATION_SOURCES)}"
                    )
                source_refs = proposition.get("source_refs")
                if not isinstance(source_refs, list) or not source_refs or any(
                    not isinstance(item, str) or not item.strip() for item in source_refs
                ):
                    errors.append(f"{context}.relation_proposition.source_refs must be a non-empty list")
                if source == "candidate_feedback" and not _norm_pn(
                    proposition.get("source_publication_number")
                ):
                    errors.append(
                        f"{context}.relation_proposition.source_publication_number is required for candidate_feedback"
                    )
            if not isinstance(query.get("semantic_query"), str) or not query.get("semantic_query", "").strip():
                errors.append(f"{context}.semantic_query is required for relation queries")
            keywords = query.get("keywords")
            if not isinstance(keywords, list) or not keywords or any(
                not isinstance(item, str) or not item.strip() for item in keywords
            ):
                errors.append(f"{context}.keywords must be a non-empty list for relation queries")

    if version == 2:
        for index, query in enumerate(queries):
            if not isinstance(query, dict) or query.get("route") != "synonym":
                continue
            context = f"queries[{index}]"
            base_id = query.get("derived_from_query_id")
            base = query_by_id.get(base_id) if isinstance(base_id, str) else None
            if not isinstance(base_id, str) or not base_id.strip():
                errors.append(f"{context}.derived_from_query_id is required for synonym queries")
            elif not isinstance(base, dict) or base.get("route") != "relation":
                errors.append(f"{context}.derived_from_query_id must reference a relation query")
            elif set(query.get("comparison_unit_numbers", [])) != set(
                base.get("comparison_unit_numbers", [])
            ):
                errors.append(f"{context} must inherit comparison_unit_numbers from its relation query")
            if not isinstance(query.get("semantic_query"), str) or not query.get("semantic_query", "").strip():
                errors.append(f"{context}.semantic_query is required for synonym queries")
            expansion = query.get("relation_synonym_expansion")
            if not isinstance(expansion, dict):
                errors.append(f"{context}.relation_synonym_expansion is required for synonym queries")
                continue
            variants: dict[str, list[str]] = {}
            for field in ("subject_variants", "relation_variants", "object_or_condition_variants"):
                values = expansion.get(field)
                if not isinstance(values, list) or not values or any(
                    not isinstance(item, str) or not item.strip() for item in values
                ):
                    errors.append(f"{context}.relation_synonym_expansion.{field} must be a non-empty list")
                    variants[field] = []
                else:
                    variants[field] = values
            base_proposition = base.get("relation_proposition") if isinstance(base, dict) else None
            if isinstance(base_proposition, dict):
                for source_field, variant_field in (
                    ("subject", "subject_variants"),
                    ("relation", "relation_variants"),
                    ("object_or_condition", "object_or_condition_variants"),
                ):
                    if base_proposition.get(source_field) not in variants.get(variant_field, []):
                        errors.append(
                            f"{context}.{variant_field} must retain the source relation {source_field}"
                        )
            base_constraints = (
                base_proposition.get("constraints", []) if isinstance(base_proposition, dict) else []
            )
            constraint_groups = expansion.get("constraint_variant_groups")
            group_variants: dict[str, list[str]] = {}
            if not isinstance(constraint_groups, list):
                errors.append(
                    f"{context}.relation_synonym_expansion.constraint_variant_groups must be a list"
                )
                constraint_groups = []
            for group_index, group in enumerate(constraint_groups):
                group_context = (
                    f"{context}.relation_synonym_expansion.constraint_variant_groups[{group_index}]"
                )
                if not isinstance(group, dict):
                    errors.append(f"{group_context} must be an object")
                    continue
                source_constraint = group.get("source_constraint")
                values = group.get("variants")
                if source_constraint not in base_constraints:
                    errors.append(f"{group_context}.source_constraint must reference a source constraint")
                    continue
                if source_constraint in group_variants:
                    errors.append(f"{group_context}.source_constraint is duplicated")
                if not isinstance(values, list) or not values or any(
                    not isinstance(item, str) or not item.strip() for item in values
                ):
                    errors.append(f"{group_context}.variants must be a non-empty list")
                    values = []
                elif source_constraint not in values:
                    errors.append(f"{group_context}.variants must retain the source constraint")
                group_variants[source_constraint] = values
            if set(group_variants) != set(base_constraints):
                errors.append(
                    f"{context}.constraint_variant_groups must cover every source constraint exactly once"
                )
            phrases = expansion.get("composed_phrases")
            phrase_texts: list[str] = []
            if not isinstance(phrases, list) or not phrases:
                errors.append(
                    f"{context}.relation_synonym_expansion.composed_phrases must be a non-empty list"
                )
                phrases = []
            for phrase_index, phrase in enumerate(phrases):
                phrase_context = (
                    f"{context}.relation_synonym_expansion.composed_phrases[{phrase_index}]"
                )
                if not isinstance(phrase, dict):
                    errors.append(f"{phrase_context} must be an object")
                    continue
                for field in ("text", "language"):
                    if not isinstance(phrase.get(field), str) or not phrase.get(field, "").strip():
                        errors.append(f"{phrase_context}.{field} must be a non-empty string")
                text_value = phrase.get("text")
                if isinstance(text_value, str) and text_value.strip():
                    phrase_texts.append(text_value)
                for phrase_field, variant_field in (
                    ("subject_variant", "subject_variants"),
                    ("relation_variant", "relation_variants"),
                    ("object_or_condition_variant", "object_or_condition_variants"),
                ):
                    value = phrase.get(phrase_field)
                    if value not in variants.get(variant_field, []):
                        errors.append(
                            f"{phrase_context}.{phrase_field} must reference a declared {variant_field} value"
                        )
                used_constraints = phrase.get("constraint_variants")
                if not isinstance(used_constraints, list):
                    errors.append(
                        f"{phrase_context}.constraint_variants must reference declared values"
                    )
                else:
                    for source_constraint, allowed in group_variants.items():
                        if sum(item in allowed for item in used_constraints) != 1:
                            errors.append(
                                f"{phrase_context}.constraint_variants must select one value for "
                                f"source constraint {source_constraint!r}"
                            )
                    declared = {item for allowed in group_variants.values() for item in allowed}
                    if any(item not in declared for item in used_constraints):
                        errors.append(
                            f"{phrase_context}.constraint_variants must reference declared values"
                        )
            keywords = query.get("keywords")
            if not isinstance(keywords, list) or keywords != phrase_texts:
                errors.append(
                    f"{context}.keywords must exactly match composed_phrases text in order"
                )

    reflections = data.get("route_reflections")
    if route_reflection_policy == "required" and (not isinstance(reflections, list) or not reflections):
        errors.append("route_reflection_policy requires non-empty route_reflections")
    if reflections is None:
        reflections = []
    elif not isinstance(reflections, list):
        errors.append("route_reflections must be a list")
        reflections = []
    reflection_ids: set[str] = set()
    for index, reflection in enumerate(reflections):
        context = f"route_reflections[{index}]"
        if not isinstance(reflection, dict):
            errors.append(f"{context} must be an object")
            continue
        reflection_id = reflection.get("reflection_id")
        if not isinstance(reflection_id, str) or not reflection_id.strip():
            errors.append(f"{context}.reflection_id must be a non-empty string")
            continue
        if reflection_id in reflection_ids:
            errors.append(f"duplicate reflection_id: {reflection_id}")
        reflection_ids.add(reflection_id)
        query_ids = reflection.get("query_ids")
        if not isinstance(query_ids, list) or not query_ids or any(
            not isinstance(item, str) or item not in query_by_id for item in query_ids
        ):
            errors.append(f"{context}.query_ids must reference existing queries")
        sample_size = reflection.get("sample_size")
        unique = reflection.get("unique_families_or_provisional_groups")
        dominant = reflection.get("dominant_mechanism_count")
        if not all(isinstance(item, int) and not isinstance(item, bool)
                   for item in (sample_size, unique, dominant)):
            errors.append(f"{context} sample and diversity values must be integers")
            sample_size = unique = dominant = 0
        elif sample_size < 20 or unique < 1 or dominant < 1 or unique > sample_size or dominant > sample_size:
            errors.append(f"{context} sample and diversity values are inconsistent")
        coverage = reflection.get("decisive_relation_coverage")
        if coverage not in RELATION_COVERAGE:
            errors.append(f"{context}.decisive_relation_coverage is invalid")
        echo = reflection.get("effect_term_echo")
        if not isinstance(echo, bool):
            errors.append(f"{context}.effect_term_echo must be boolean")
            echo = False
        dimensions = reflection.get("missing_dimensions")
        if not isinstance(dimensions, list) or any(item not in IMPLEMENTATION_DIMENSIONS for item in dimensions):
            errors.append(f"{context}.missing_dimensions contains an invalid value")
            dimensions = []
        basis = reflection.get("evidence_basis")
        if basis not in REFLECTION_BASES:
            errors.append(f"{context}.evidence_basis must be one of {sorted(REFLECTION_BASES)}")
        _refs_exist(reflection.get("evidence_refs"), root, errors, context)
        decision = reflection.get("decision")
        if decision not in REFLECTION_DECISIONS:
            errors.append(f"{context}.decision must be one of {sorted(REFLECTION_DECISIONS)}")
        if not isinstance(reflection.get("decision_reason"), str) or not reflection.get("decision_reason", "").strip():
            errors.append(f"{context}.decision_reason must be a non-empty string")

        dominant_locked = sample_size > 0 and dominant * 5 >= sample_size * 3
        relation_gap = coverage in {"partial", "missing"}
        if echo and relation_gap and decision not in {"route_reconstruct", "request_input"}:
            errors.append(f"{context} effect-term echo with a relation gap requires route_reconstruct or request_input")
        elif dominant_locked and relation_gap and decision not in {"route_reconstruct", "term_rewrite", "request_input"}:
            errors.append(f"{context} dominant mechanism with a relation gap requires query reconstruction or input")
        elif dominant_locked and decision == "converge":
            errors.append(f"{context} cannot converge while one mechanism occupies at least 60%")
        if decision == "converge" and (coverage != "covered" or echo):
            errors.append(f"{context} converge requires covered relations and no effect-term echo")
        if decision in {"route_reconstruct", "request_input"} and not dimensions:
            errors.append(f"{context} {decision} requires missing_dimensions")

        followups = reflection.get("followup_query_ids", [])
        if decision in {"route_reconstruct", "term_rewrite"}:
            if not isinstance(followups, list) or not followups:
                errors.append(f"{context} {decision} requires followup_query_ids")
            else:
                for query_id in followups:
                    query = query_by_id.get(query_id) if isinstance(query_id, str) else None
                    if not isinstance(query, dict):
                        errors.append(f"{context} references unknown followup query {query_id!r}")
                    elif query.get("reconstructed_from_reflection_id") != reflection_id:
                        errors.append(
                            f"{context} followup query {query_id} must backlink with reconstructed_from_reflection_id"
                        )
        elif followups not in ([], None):
            errors.append(f"{context}.followup_query_ids is only valid for rewrite or reconstruction")

    scope = data.get("scope") if isinstance(data.get("scope"), dict) else {}
    cutoff = _parse_date(scope.get("publication_date"))
    if scope.get("publication_date") and cutoff is None:
        errors.append("scope.publication_date must be an ISO date")
    inclusive = scope.get("publication_date_inclusive")
    if version == 2 and cutoff is not None and not isinstance(inclusive, bool):
        errors.append("ledger_version 2 requires boolean scope.publication_date_inclusive")
    raw_jurisdictions = scope.get("required_publication_jurisdictions", [])
    if not isinstance(raw_jurisdictions, list) or any(
        not isinstance(item, str) or not item.strip() for item in raw_jurisdictions
    ):
        errors.append("scope.required_publication_jurisdictions must be a list of strings")
        required_jurisdictions: set[str] = set()
    else:
        required_jurisdictions = {item.upper() for item in raw_jurisdictions}

    candidates = data.get("candidates")
    if not isinstance(candidates, list):
        errors.append("candidates must be a list")
        candidates = []
    candidate_by_pn: dict[str, dict[str, Any]] = {}
    identity_owner: dict[str, str] = {}
    for index, candidate in enumerate(candidates):
        context = f"candidates[{index}]"
        if not isinstance(candidate, dict):
            errors.append(f"{context} must be an object")
            continue
        pn = _norm_pn(candidate.get("publication_number"))
        if not pn:
            errors.append(f"{context}.publication_number must be an exact publication number")
            continue
        aliases_raw = candidate.get("aliases", [])
        if not isinstance(aliases_raw, list):
            errors.append(f"{context}.aliases must be a list")
            aliases: set[str] = set()
        else:
            aliases = _pn_values(aliases_raw)
            if len(aliases) != len(aliases_raw):
                errors.append(f"{context}.aliases contains an invalid publication number")
        identities = {pn, *aliases}
        if pn in candidate_by_pn:
            errors.append(f"duplicate candidate publication_number: {pn}")
        candidate_by_pn[pn] = candidate
        for identity in identities:
            owner = identity_owner.get(identity)
            if owner and owner != pn:
                errors.append(f"candidate alias collision: {identity} belongs to {owner} and {pn}")
            else:
                identity_owner[identity] = pn
        if candidate.get("priority") not in PRIORITIES:
            errors.append(f"{context}.priority must be one of {sorted(PRIORITIES)}")
        stage = candidate.get("stage")
        if stage not in STAGES:
            errors.append(f"{context}.stage must be one of {sorted(STAGES)}")
        discoveries = candidate.get("discoveries")
        if not isinstance(discoveries, list) or not discoveries:
            errors.append(f"{context}.discoveries must be a non-empty list")
        else:
            for discovery in discoveries:
                if not isinstance(discovery, dict) or discovery.get("query_id") not in query_by_id:
                    errors.append(f"{context} references an unknown discovery query_id")
        decision = candidate.get("decision")
        if decision not in {"advance", "exclude"}:
            errors.append(f"{context}.decision must be advance or exclude")
        if not isinstance(candidate.get("reason"), str) or not candidate.get("reason", "").strip():
            errors.append(f"{context}.reason must be a non-empty string")

        eligibility = candidate.get("eligibility")
        eligibility = eligibility if isinstance(eligibility, dict) else {}
        if version == 2 and cutoff is not None:
            published = _parse_date(candidate.get("publication_date"))
            computed_date = ("unverified" if published is None else
                             "eligible" if (published <= cutoff if inclusive else published < cutoff)
                             else "ineligible")
            if eligibility.get("date") != computed_date:
                errors.append(f"{context}.eligibility.date must match computed value {computed_date}")
            if phase == "final" and stage == "final" and computed_date != "eligible":
                errors.append(f"final candidate {pn} is not publication-date eligible")
        elif phase == "final" and cutoff is not None and stage == "final" and eligibility.get("date") != "eligible":
            errors.append(f"final candidate {pn} is not publication-date eligible")

        if version == 2 and required_jurisdictions:
            actual = candidate.get("jurisdiction")
            actual = actual.upper() if isinstance(actual, str) else None
            computed = "eligible" if actual in required_jurisdictions else "ineligible" if actual else "unverified"
            if eligibility.get("jurisdiction") != computed:
                errors.append(f"{context}.eligibility.jurisdiction must match computed value {computed}")
            if phase == "final" and stage == "final" and computed != "eligible":
                errors.append(f"final candidate {pn} is not jurisdiction eligible")

        if decision == "exclude":
            if stage != "excluded":
                errors.append(f"{context} excluded decision requires stage=excluded")
            _refs_exist(candidate.get("evidence_refs"), root, errors, context, identities)
        if phase == "fetch" and candidate.get("priority") == "high" and decision == "advance" and stage not in {"fetched", "compared", "final"}:
            errors.append(f"{context} high-priority candidate has not reached fetched stage")
        if phase == "compare" and candidate.get("priority") == "high" and decision == "advance" and stage not in {"compared", "final"}:
            errors.append(f"{context} high-priority candidate has not reached compared stage")
        if phase == "final":
            if stage not in {"final", "excluded"}:
                errors.append(f"{context} lacks a terminal final/excluded disposition")
            if decision == "advance" and stage != "final":
                errors.append(f"{context} advanced candidate requires stage=final at final phase")

    response_files = data.get("search_response_files")
    if not isinstance(response_files, list) or not response_files:
        errors.append("search_response_files must be a non-empty list")
        response_files = []
    missing_fill_files = sorted(fill_response_files - set(response_files))
    if missing_fill_files:
        errors.append("dedup_fill response files missing from search_response_files: " + ", ".join(missing_fill_files))
    observed_groups: list[frozenset[str]] = []
    for index, relative in enumerate(response_files):
        if not isinstance(relative, str) or not relative.strip():
            errors.append(f"search_response_files[{index}] must be a non-empty relative path")
            continue
        response = _read_json(root / relative, errors, "search response")
        if response is not None:
            observed_groups.extend(_publication_number_groups(response))
    missing_groups = [group for group in observed_groups if not set(group).intersection(identity_owner)]
    if missing_groups:
        errors.append("search results missing from candidate ledger: " + ", ".join(
            "/".join(sorted(group)) for group in missing_groups
        ))

    retrieval = data.get("retrieval_assessment")
    if isinstance(retrieval, dict):
        family = retrieval.get("family_diversity")
        if isinstance(family, dict):
            values = (family.get("top_k"), family.get("unique_families"), family.get("dominant_family_count"))
            if not all(isinstance(item, int) and not isinstance(item, bool) for item in values):
                errors.append("family_diversity values must be integers")
            else:
                top_k, unique, dominant = values
                if top_k < 10 or unique < 1 or dominant < 1 or unique > top_k or dominant > top_k:
                    errors.append("family_diversity values are inconsistent")
                elif dominant * 2 > top_k and retrieval.get("strength") != "weak":
                    errors.append("dominant family exceeds 50%; retrieval strength must be weak")
        precision = retrieval.get("object_precision_sample")
        if isinstance(precision, dict):
            values = (precision.get("reviewed"), precision.get("on_object"))
            if not all(isinstance(item, int) and not isinstance(item, bool) for item in values):
                errors.append("object_precision_sample values must be integers")
            else:
                reviewed, on_object = values
                if reviewed < 10 or on_object < 0 or on_object > reviewed:
                    errors.append("object_precision_sample values are inconsistent")
                elif on_object * 5 < reviewed * 3 and retrieval.get("strength") != "weak":
                    errors.append("on-object rate is below 60%; retrieval strength must be weak")
    if isinstance(retrieval, dict) and retrieval.get("strength") == "weak":
        feedback_ids = retrieval.get("feedback_query_ids")
        if not isinstance(feedback_ids, list) or not feedback_ids:
            errors.append("weak retrieval requires feedback_query_ids")
        else:
            routes = {query_by_id[item].get("route") for item in feedback_ids if item in query_by_id}
            unknown = [item for item in feedback_ids if item not in query_by_id]
            if unknown:
                errors.append("weak retrieval references unknown feedback queries: " + ", ".join(unknown))
            if "relation" not in routes:
                errors.append("weak retrieval feedback must include a relation query")
            if not routes.intersection({"synonym", "classification", "citation"}):
                errors.append("weak retrieval feedback must include synonym, classification, or citation route")
        if version == 2:
            decisive = retrieval.get("decisive_comparison_unit_numbers")
            if not isinstance(decisive, list) or not decisive or any(
                not isinstance(item, int) or isinstance(item, bool) or item < 1 for item in decisive
            ):
                errors.append("weak retrieval requires decisive_comparison_unit_numbers")
            else:
                covered = {
                    unit
                    for query in query_by_id.values()
                    if query.get("route") == "relation"
                    for unit in query.get("comparison_unit_numbers", [])
                    if isinstance(unit, int) and not isinstance(unit, bool)
                }
                missing_units = sorted(set(decisive) - covered)
                if missing_units:
                    errors.append(
                        "decisive comparison units lack relation-query coverage: "
                        + ", ".join(map(str, missing_units))
                    )

    if required_jurisdictions:
        reconciliation = data.get("jurisdiction_reconciliation")
        if not isinstance(reconciliation, dict):
            errors.append("required publication jurisdictions need jurisdiction_reconciliation")
            reconciliation = {}
        for jurisdiction in sorted(required_jurisdictions):
            entry = reconciliation.get(jurisdiction)
            context = f"jurisdiction_reconciliation.{jurisdiction}"
            if not isinstance(entry, dict):
                errors.append(f"{context} is required")
                continue
            if entry.get("status") not in {"represented", "all_excluded", "no_eligible_candidate"}:
                errors.append(f"{context}.status is invalid")
            if not isinstance(entry.get("reason"), str) or not entry.get("reason", "").strip():
                errors.append(f"{context}.reason must be a non-empty string")
            if entry.get("status") == "all_excluded":
                _refs_exist(entry.get("evidence_refs"), root, errors, context)
            if phase == "final" and entry.get("status") == "represented":
                represented = any(
                    item.get("stage") == "final" and (
                        str(item.get("jurisdiction", "")).upper() == jurisdiction if version == 2 else pn.startswith(jurisdiction)
                    ) for pn, item in candidate_by_pn.items()
                )
                if not represented:
                    errors.append(f"{context} says represented but no final candidate has that jurisdiction")

    if phase == "final":
        nonterminal = sum(1 for item in candidate_by_pn.values() if item.get("stage") not in {"final", "excluded"})
        computed = len(missing_groups) + nonterminal
        if data.get("unexplained_drop_count") != computed:
            errors.append(f"unexplained_drop_count must equal computed value {computed}, got {data.get('unexplained_drop_count')!r}")
        if computed:
            errors.append(f"computed unexplained drop count must be 0, got {computed}")
    elif phase == "compare" and data.get("unexplained_drop_count") != 0:
        errors.append("unexplained_drop_count must be 0")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", required=True, type=Path)
    parser.add_argument("--root", type=Path)
    parser.add_argument("--phase", choices=("fetch", "compare", "final"), required=True)
    args = parser.parse_args()
    root = (args.root or args.ledger.parent).resolve()
    pre_errors: list[str] = []
    data = _read_json(args.ledger.resolve(), pre_errors, "ledger")
    errors = pre_errors if data is None else pre_errors + validate_ledger(data, root, args.phase)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"candidate ledger valid for phase={args.phase}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
