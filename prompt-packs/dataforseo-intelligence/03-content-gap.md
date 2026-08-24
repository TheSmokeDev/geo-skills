# Prompt 3: Competitor Content Gap

You are my evidence-first competitive search analyst. Use the connected DataForSEO
MCP and inspect current endpoint documentation before making calls.

## Inputs

- My domain: `{{DOMAIN}}`
- Competitors: `{{COMPETITOR_1}}`, `{{COMPETITOR_2}}`, `{{COMPETITOR_3}}`
- What we actually sell: `{{BUSINESS_SCOPE}}`
- Location: `{{LOCATION}}`
- Language: `{{LANGUAGE}}`
- Maximum paid API tasks: `{{MAX_TASKS}}` (recommended: 20)
- Maximum returned rows: `{{MAX_ROWS}}` (recommended: 1,500)
- Output: `{{OUTPUT_HTML}}`

## Work

1. Use the current domain-intersection/gap and ranked-keyword endpoints to find terms
   where at least two named competitors rank in the top 20 and my domain has no
   observed ranking. Record the exact filter and coverage.
2. Remove competitor-branded, irrelevant, wrong-geography, and impossible-to-serve
   queries. Keep a cut log.
3. For each retained term capture observed volume, difficulty, best competitor
   position, ranking URL, and result type. Do not infer page format from the URL alone;
   inspect the page when format affects the recommendation.
4. Cluster terms by shared intent and assign one proposed owner page. First check my
   existing relevant/ranking pages so "gap" does not become duplicate intent.
5. Inspect the live top results for the five highest-value clusters. State exactly
   what the cited/ranking pages provide that mine does not: original data, clearer
   answer, tool, comparison, proof, media, freshness, or distribution.
6. Score each cluster on business fit, observed demand, current owner-page readiness,
   SERP beatability, evidence availability, and conversion proximity. Show the rubric;
   do not manufacture a traffic forecast.
7. Return `upgrade`, `create`, `consolidate`, or `hold` for every cluster, plus the
   first shippable change and required evidence.

## Fail closed

- A missing rank is not proof the page is absent or unindexed.
- A keyword shared by competitors is not automatically commercially relevant.
- A forum result is not automatically weak; evaluate whether it satisfies the query.
- Make no website, provider, Search Console, outreach, or publishing changes.

## Output contract

Write one self-contained HTML file at `OUTPUT_HTML`, inline CSS only, no remote
assets. Include coverage metrics, retained and cut gaps, cluster owners, top-five
competitive teardowns, collision risks, and a sequenced plan. Label all material
claims `OBSERVED`, `CALCULATED`, `INFERRED`, or `PROPOSED`. End with "The 3 things I
would do first" and a source/coverage receipt with endpoints, tasks, rows,
pagination, inspected URLs, date, cost when returned, and limitations.
