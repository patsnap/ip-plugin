# Writing patent technical descriptions

Use one italic sentence per patent, normally 20–50 English words. For Chinese, use about 12–60 characters. For other requested languages, use comparable information density. Explain why the patent belongs in the area and what its specific technical subject is.

## Three required elements

```text
Protects {specific object}, using {mechanism/construction}, serving {role in this technology or commercialization path}.
```

A sentence missing any element fails the requirement.

## Layer-specific templates

### Physical/manufacturing foundations

Focus: concrete mechanical/structural object → architectural function → manufacturing/assembly relationship.

> Protects the {structural feature} of {component}, defining {dimension/interface/flow-path} relationships that provide {function} within {architecture}.

Examples:
- Protects a shared building arrangement for multiple modules, defining lifting corridors, pool structures and module spacing to connect factory-built modules with on-site installation.
- Protects tube-sheet openings and seals inside a pressure vessel, separating primary and secondary circuits in an integrated design without external main piping.

### Regulatory licensing/certification barriers

Focus: concrete passive mechanism → evidenced certification role → position in family evolution.

> Protects a {passive/adaptive} implementation of {system}, using {gravity/density difference/immersion/phase change} to perform {function}, supporting {specific safety case} in {certification}.

Examples (claims about certification or citation counts require actual evidence):
- Protects passive emergency-feedwater startup through hot/cold-leg density differences, driving natural circulation without external power or a main pump and supporting the loss-of-power residual-heat-removal safety case.
- For an early, highly cited member, its evidenced role as a reference for industry passive-safety designs may supply the third element. A citation statement alone does not replace the protected object and mechanism.

### Commercialization

Focus: system hierarchy → topology/coupling → specific commercial application.

> Protects {architectural feature} at the {grid/module/process} level, enabling {capability} for {named product family/application}.

Examples:
- Protects the internal-grid topology of a multi-module power station, enabling islanded operation and module-level load dispatch for the station's product family.
- Protects coupling between reactor heat and hydrogen production through an indirect thermal loop, supplying industrial process heat for green industry and data-center energy applications.

## Prohibited

- Generic filler: “This patent concerns reactor technology and is important.”
- Title-only repetition: “Protects a passive emergency-feedwater system.”
- Claim-scope assertions: “Covers all natural-circulation cooling” or “Competitors cannot design around it.”
- Invented parameters, materials or values unsupported by original evidence read, or technical-summary fields presented as originals.
- Identical opening phrasing for every patent in an area; vary expression without omitting required elements.

## Quality check

Check every listed sentence; actual `listed_count` determines the total, not a target of 30:

1. Does it identify a concrete protected object rather than a broad field?
2. Does it name a mechanism/construction rather than merely “advanced” or “efficient”?
3. Does it explain relevance to its area?
4. Is there only one representative per simple family, with no count-padding siblings?
5. Does any sentence exceed evidence actually read? For protected objects, component relationships and mechanisms, were corresponding claims/description grounds checked and retained?
6. Does any wording improperly interpret claim scope?
