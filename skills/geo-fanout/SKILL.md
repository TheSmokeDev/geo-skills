---
name: geo-fanout
description: Query fan-out and topic-cluster optimization for AI search. Maps a topic's full sub-query space, audits cluster coverage against what engines actually fan out into, and engineers titles and URL slugs for semantic match with fan-out queries. Use when a site needs to win citations beyond the organic top 10 or cover a topic cluster instead of a single head term.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Query Fan-Out / Topic-Cluster Optimization Skill

## Purpose

This skill optimizes a site for **query fan-out** -- the mechanism by which AI search engines rewrite a single user prompt into a cluster of sub-queries and retrieve sources per sub-query. Fan-out coverage is the 2026 meta-factor for AI citation: pages win citations by matching the sub-queries engines generate, not by ranking #1 for the head term. This skill maps a topic's sub-query space, audits how much of it the site covers, and engineers titles and URL slugs so pages survive the pre-read gatekeeping step.

## Core Insight

Fan-out is the top-scoring citation factor in Zyppy's 23-factor meta-analysis: **9.3/10** (DigitalApplied synthesis of 54 studies, Jun 2026). Engines like Gemini 3 (Jan 2026) and ChatGPT decompose one prompt into multiple sub-queries, run each against their index, and cite the pages that best match each sub-query. The consequence is a collapsed dependence on organic rank:

- Only **38% of AIO-cited URLs rank in the organic top 10** -- down from 76% (Ahrefs, 863K SERPs / 4M URLs, Mar 2026).
- **31% of AIO citations come from positions 11-100**, and **31% from beyond position 100** (same study).

Page-3 organic is NOT disqualifying. The fan-out is the small-site opening: a low-authority page that precisely answers one sub-query can be cited over a high-authority page that only covers the head term.

Win the cluster, not the head term.

---

## How Fan-Out Works (Mechanism)

1. User submits one prompt (e.g., "how much does SR-22 insurance cost in California?").
2. The engine classifies whether to search at all (ChatGPT: only ~18-24% of prompts trigger search).
3. The prompt is rewritten into a cluster of sub-queries -- eligibility, cost, process, location, and language variants of the underlying intent.
4. Each sub-query is run against the engine's retrieval index (ChatGPT: Bing; Gemini/AIO: Google).
5. Retrieved pages pass a **pre-read gate** on title, snippet, and URL before content is ever opened.
6. The engine cites the best-matching pages across the cluster (~15-50% of retrieved URLs get cited; ⚠️ single source, SubscribePR Jul 2026).

Steps 3-5 are what this skill optimizes. Steps 1-2 and 6 are covered by `skills/geo-citability/` and `skills/geo-ai-index-access/`.

---

## Step 1: Map the Sub-Query Space

For each target topic, enumerate the sub-query space an engine would fan out into. Generate candidate sub-queries across these five variant axes:

| Axis | What to Generate | Example (topic: SR-22 insurance in California) |
|---|---|---|
| **Eligibility** | who qualifies, requirements, edge cases, disqualifiers | "who needs SR-22 in California", "SR-22 after DUI requirements" |
| **Cost** | price, average cost, cheapest, cost by segment | "average SR-22 cost California 2026", "cheapest SR-22 insurance Los Angeles" |
| **Process** | how to get, how long, steps, filing, renewal | "how to file SR-22 in California", "how long does SR-22 last" |
| **Location** | state, county, city, metro variants | "SR-22 insurance San Diego", "SR-22 cost by California county" |
| **Language** | non-English variants of every axis above | "seguro SR-22 California precio", "quien necesita SR-22" |

Procedure:

1. State the head term / target prompt.
2. Generate 5-15 sub-queries per axis (25-75 total per topic). Use real query sources where available: Google Search Console queries, Bing Webmaster Tools keyword data, autocomplete, "People Also Ask".
3. Deduplicate and cluster the list into 5-10 sub-topics that each deserve a page (or a clearly differentiated section).
4. For each sub-query, record: which existing URL (if any) covers it, and whether coverage is **dedicated** (page is about this) or **incidental** (mentioned in passing).

**Compliance line:** do NOT spin keyword-variant pages with near-identical content. Google's official 2026 guidance classifies keyword-variant page farming as scaled-content abuse (Google Search Central, May 2026). Every cluster page must carry per-page unique data (per-city rates, per-county figures, original numbers) -- the same differentiation bar AI Mode applies when rewarding 15-20-page topic clusters over single pages.

## Step 2: Cluster-Coverage Audit

1. Build the coverage matrix: rows = sub-queries from Step 1, columns = candidate URLs on the site.
2. For each sub-query, WebFetch the mapped page and check:
   - Does the page's H1/title directly answer this sub-query?
   - Does a self-contained passage answer it in the first 40-60 words of a section? (See `skills/geo-citability/` for passage scoring.)
   - Is the answer data-dense (specific numbers, dates, named entities)?
3. Score each sub-query: **Covered** (dedicated page, direct answer), **Weak** (incidental mention or buried answer), **Missing** (no page).
4. Compute cluster coverage = Covered / total sub-queries.
5. Prioritize gaps by expected retrieval volume: cost and location variants typically carry the most fan-out traffic; language variants are often the thinnest competition.

**Deliverable from the audit:** a build list of missing pages (each with its target sub-query, required unique data, and engineered title/slug per Step 3) plus a rewrite list of weak pages.

## Step 3: Title + Slug Semantic-Match Engineering

Titles and slugs are citation factors **before content is read** -- they gate whether the engine even opens the page (Ahrefs, 1.4M prompts, Apr 2026):

- Cited-URL titles score **0.656 cosine similarity to the fan-out queries** vs **0.484 for non-cited URLs** (same study).
- **Natural-language slugs cite at 89.78% vs 81.11%** for non-natural slugs (same study).

Procedure for each page in the build/rewrite list:

1. Take the primary sub-query the page targets.
2. Write the title to mirror that sub-query in natural language -- include the entity, the variant axis (cost/location/etc.), and the year where freshness matters. Example: `SR-22 Insurance Cost in California (2026 Rates by County)`.
3. Write the slug as a natural-language phrase, not a keyword string or ID:
   - Good: `/sr-22-insurance-cost-california/`
   - Bad: `/sr22-ca-cost-v2/`, `/page?id=4471`, `/blog/post-8823/`
4. Keep title and H1 aligned with the slug -- all three are read at the gatekeeping step.
5. Sanity-check similarity: the title should read as a direct answer to the sub-query, not a clever headline.

This is the highest-leverage-per-minute intervention in the pack: no new content, no links, just matching the strings engines fan out into.

---

## Vertical Caveat: High-Overlap Verticals Still Reward Classic SEO

The 38% overlap figure is an average. **Insurance, healthcare, and education retain 68-75% overlap between organic top-10 rankings and AI citations** (BrightEdge via Shadow, Jul 2026 -- ⚠️ secondary source only, verify before quoting publicly). In these YMYL verticals:

- Classic ranking work still feeds AI citations directly. Do NOT deprioritize traditional SEO.
- Fan-out coverage is additive, not a replacement: build the cluster AND keep ranking the head terms.
- If the site being audited is in one of these verticals, say so explicitly in the report and weight classic-SEO fixes accordingly.

---

## Output Format

Generate a file called `GEO-FANOUT-COVERAGE.md`:

```markdown
# Fan-Out Cluster Coverage: [Domain] -- [Topic]

**Analysis Date:** [Date]
**Head Term / Target Prompt:** [Prompt]
**Sub-Queries Mapped:** [N]
**Cluster Coverage:** [X]% ([Covered]/[Total] sub-queries with dedicated pages)

---

## Coverage Matrix

| Sub-Query | Axis | Mapped URL | Status | Action |
|---|---|---|---|---|
| [sub-query] | Cost | [URL or --] | Covered/Weak/Missing | [Build/Rewrite/None] |

## Title + Slug Engineering Queue

| Page | Target Sub-Query | Current Title | Proposed Title | Proposed Slug |
|---|---|---|---|---|
| [URL/new] | [sub-query] | [title] | [natural-language title] | [/natural-language-slug/] |

## Vertical Overlap Assessment

[Is this a 68-75% high-overlap vertical (insurance/healthcare/education)?
 If yes: classic SEO remains a primary lever -- note the ⚠️ secondary-source flag.]

## Recommended Build Order

1. [Highest-volume missing sub-query page -- required unique data noted]
2. [Next]
```

---

## Related Skills

- `skills/geo-citability/` -- once a page passes the title/slug gate, passage-level citability determines whether it gets quoted.
- `skills/geo-ai-index-access/` -- fan-out coverage is worthless if the pages are not in the retrieval index (Bing for ChatGPT, Google for AIO/Gemini).
- `skills/geo-youtube/` -- YouTube is the rank-free bypass for sub-queries the site cannot win with text pages.
- `skills/geo-measurement/` -- measure cluster-coverage gains as share-of-citation over a prompt panel, not rank.
