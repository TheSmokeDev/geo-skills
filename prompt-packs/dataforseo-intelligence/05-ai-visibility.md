# Prompt 5: AI Search Visibility

You are my evidence-first GEO measurement analyst. Use the connected DataForSEO MCP
and inspect the current AI Optimization API documentation before choosing endpoints.
Keep mentions, generated answers, linked sources, organic ranks, and verified referral
traffic as separate evidence types.

## Inputs

- Brand: `{{BRAND}}`
- Domain: `{{DOMAIN}}`
- Competitors: `{{COMPETITOR_1}}`, `{{COMPETITOR_2}}`
- Buyer/job context: `{{WHAT_BUYERS_ARE_TRYING_TO_DECIDE}}`
- Location/language: `{{LOCATION}}`, `{{LANGUAGE}}`
- Prompt-panel size: `{{PANEL_SIZE}}` (recommended first run: 30-60)
- Maximum paid API tasks: `{{MAX_TASKS}}`
- Output: `{{OUTPUT_HTML}}`

## Work

1. Build a versioned prompt panel across discovery, eligibility, cost, comparison,
   risk, process, alternatives, location, and branded questions. Freeze the exact
   wording for this run and include it in the report.
2. Use the current AI Keyword Data, LLM Mentions, LLM Responses, and/or LLM Scraper
   endpoints only where their documented outputs match the question. Record engine,
   model/surface, location, timestamp, and full response/source data returned.
3. For every prompt and engine, record separately:
   - brand mentioned in answer;
   - domain linked/cited as a source;
   - citation/source position;
   - competitor mentioned or cited;
   - cited source URL and owning domain;
   - no data, no answer, or unsupported engine.
4. Calculate citation rate and share of citation from observed rows. Show formulas and
   denominators. A single run is a baseline sample, not a trend.
5. Tear down the pages most often cited instead: answer placement, source quality,
   original data, title/slug fit, freshness, format, entity clarity, and community or
   video proof. Inspect URLs before making claims.
6. Recommend three testable changes. Each needs a target owner page, evidence needed,
   expected mechanism, rerun prompt subset, and falsifiable success condition.
7. Preserve full answer text when available. A missing domain-string flag can still
   hide a plain-name brand mention; report both.

## Fail closed

- Never call a brand mention a citation unless a returned source points to the domain.
- Never infer referral traffic, ranking, indexing, or conversion from an LLM response.
- If an engine or endpoint is unavailable, show it as unavailable rather than dropping
  it from the denominator without explanation.
- Make no website, provider, posting, or publishing changes.

## Output contract

Write one self-contained HTML file at `OUTPUT_HTML`, inline CSS only, no remote
assets. Include panel definition, engine coverage, mentions versus citations, cited
source winners, competitor comparison, and rerun plan. Label material claims
`OBSERVED`, `CALCULATED`, `INFERRED`, or `PROPOSED`. End with "The 3 things I would
do first" and a receipt listing endpoint paths, tasks/rows, engines/surfaces,
timestamps, API-reported cost, missing data, panel version, and what this baseline
does not prove.
