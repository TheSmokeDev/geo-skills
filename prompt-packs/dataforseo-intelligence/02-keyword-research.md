# Prompt 2: Keyword Research and Owner Clustering

You are my evidence-first search strategist. Use the connected DataForSEO MCP and
inspect its current documentation before choosing endpoints.

## Inputs

- Seed: `{{SEED_KEYWORD}}`
- Business offer: `{{WHAT_THE_BUSINESS_SELLS}}`
- Audience: `{{AUDIENCE}}`
- Location: `{{LOCATION}}`
- Language: `{{LANGUAGE}}`
- Existing site/domain: `{{DOMAIN_OR_NONE}}`
- Maximum paid API tasks: `{{MAX_TASKS}}` (recommended: 20)
- Maximum returned keyword rows: `{{MAX_ROWS}}` (recommended: 1,500)
- Output: `{{OUTPUT_HTML}}`

## Work

1. Expand the seed with the current keyword-ideas, suggestions, related-keyword, and
   site-keyword endpoints that are relevant. Preserve source endpoint per keyword and
   deduplicate normalized terms.
2. Attach observed monthly volume, keyword difficulty, CPC, intent, and data date
   only when returned. Missing is `not available`, never zero.
3. Remove terms the business cannot credibly serve. Keep a cut log with the exact
   reason: wrong product, geography, audience, legal scope, or navigational brand.
4. Assign every retained query to exactly one primary intent: informational,
   commercial investigation, transactional, or navigational.
5. Cluster terms that belong on the same owner page. For each cluster produce a page
   purpose, working title, slug, primary decision, must-answer questions, conversion
   goal, and whether the action is `upgrade`, `create`, `consolidate`, or `hold`.
6. If a domain is supplied, check its ranking/relevant pages before recommending a
   new owner. Record owner conflicts and likely cannibalization.
7. Inspect the actual Google SERP for the highest-priority clusters. A "weak SERP"
   requires observed evidence such as intent mismatch, thin pages, stale information,
   or forum-only results; difficulty alone is not evidence.
8. Produce a build order driven by business fit, observed demand, SERP evidence,
   existing authority, and owner-page readiness. Do not equate high volume with high
   value.

## Fail closed

- Disclose caps and pagination. Never call a capped set "the full keyword universe."
- Do not invent volume, difficulty, intent, or a conversion rate.
- Do not recommend location pages without credible service-area evidence.
- Make no website, ad, provider, Search Console, or publishing changes.

## Output contract

Write one self-contained HTML file at `OUTPUT_HTML`, inline CSS only, no remote
assets. Include hero metrics, the cut log, intent/cluster table, owner-conflict
register, SERP evidence, and sequenced roadmap. Label claims `OBSERVED`,
`CALCULATED`, `INFERRED`, or `PROPOSED`. End with "The 3 things I would do first"
and a coverage receipt listing endpoint paths, task/row counts, market, date, cost
when returned, missing data, and what the report does not prove.
