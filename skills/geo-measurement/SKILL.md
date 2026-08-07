---
name: geo-measurement
description: Volatility-aware AI-visibility measurement. Designs fixed prompt panels, computes share-of-citation per engine, tracks citation position and turn-1 concentration, and reports trends without overreacting to structural platform swings. Use when measuring whether GEO work is actually increasing AI citations, or when monthly citation counts look alarming.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Volatility-Aware AI-Visibility Measurement Skill

## Purpose

This skill measures AI visibility correctly. Raw citation counts are structurally volatile -- platforms change citation behavior wholesale, and a month-over-month drop often means the platform moved, not the site. This skill designs prompt panels, computes share-of-citation, tracks citation position, and produces trend reports that separate signal from platform noise. Use it to evaluate any GEO work done with the other skills in this pack.

## Core Insight

**Citation volume is structurally volatile.** ChatGPT's citation volume fell >90% in March-April 2026, then rebounded (seoClarity, Jun 2026). Google-side citation churn runs 8-10x ChatGPT's (same analysis). A site that did nothing wrong can lose most of its measured citations in a month; a site that did nothing right can gain them.

The consequence: **monthly citation counts mislead.** The valid metric is **share-of-citation over repeated runs of a fixed 60-100+ prompt panel** (SparkToro methodology) -- of all citations the engine gives for your prompt set, what fraction point to you versus competitors? Share-of-citation is self-normalizing: when a platform cuts citations sitewide, everyone's counts drop but shares stay comparable.

---

## Step 1: Panel Design

1. **Fixed prompt set.** Define 60-100+ prompts that represent the site's target sub-query space (use `skills/geo-fanout/` to generate them across eligibility/cost/process/location/language axes). Freeze the set -- never edit prompts mid-trend, or you break comparability. Version the panel file instead (add new prompts as `panel-v2`, keep v1 running for continuity).
2. **Repeated runs.** Run the full panel on a fixed cadence (weekly or biweekly). A single run is a sample, not a measurement -- AI answers are non-deterministic, so each prompt should ideally be run multiple times per cycle or across cycles to smooth variance.
3. **Per-engine split.** Measure each engine separately -- ChatGPT, Google AIO/AI Mode, Gemini, Perplexity behave differently and move on different schedules. Never blend engines into one number. Note that ChatGPT retrieval is Bing-index-based while Gemini/AIO use Google (see `skills/geo-ai-index-access/`) -- engine-level swings often trace back to index or pipeline changes.
4. **Competitor set.** Fix 3-10 competitor domains per panel. Share-of-citation is meaningless without the denominator.
5. **Instrumentation.** Where available, pull first-party data to corroborate: Bing WMT's AI Performance (Copilot) report (unlocked by `skills/geo-ai-index-access/`), and AI referral traffic in analytics.

## Step 2: Metrics to Compute Per Run

| Metric | Definition | Why |
|---|---|---|
| **Share-of-citation** | Your citations / all citations across the panel, per engine | The core metric; self-normalizing against platform volume swings (SparkToro) |
| **Citation rate** | % of panel prompts where you are cited at all | Breadth of cluster coverage |
| **Citation position** | Ordinal position of your citation within each answer | Position-1 citation gets ~4-5x the CTR of position 5 (⚠️ single vendor source, AuthorityTech Jun 2026 -- treat the magnitude as directional) |
| **Turn-1 capture** | % of citations earned on opening questions vs follow-ups | Opening questions are 2.5-4x more likely to produce citations (Profound, 700K conversations, Feb 2026) -- panel prompts should mostly simulate turn-1 |
| **Co-citation cluster** | Which domains are cited alongside yours | Citations travel in packs: a cited conversation carries ~6 unique citations on average (Profound, Feb 2026). Your cluster neighbors reveal who the engine considers your peer set |

## Step 3: Co-Citation Cluster Analysis

1. For every answer citing the site, record ALL cited domains, not just yours.
2. Build the co-citation matrix: domain pairs that appear together across answers.
3. Use it to:
   - Identify the real competitive set (often not who the client expects -- .gov and institutional domains over-index in YMYL verticals).
   - Spot pack-entry opportunities: if competitors A and B are consistently co-cited for a sub-query cluster and you are absent, that cluster is the build target for `skills/geo-fanout/`.
   - Detect displacement early: your share stable but a new domain entering your cluster = future pressure.

## Step 4: Reporting Without Overreacting

Rules for trend interpretation:

1. **Never report raw citation counts as the headline.** Lead with share-of-citation and citation rate over the panel.
2. **Annotate platform events.** Before attributing any movement to site work, check whether the whole panel moved. If all competitors' counts dropped together, the platform changed (like the >90% ChatGPT drop and rebound, Mar-Apr 2026, seoClarity Jun 2026) -- report it as a platform event, not a loss.
3. **Use rolling windows.** Report 4-8 week rolling share, not week-over-week deltas. Google-side churn of 8-10x ChatGPT means weekly deltas on Google surfaces are mostly noise.
4. **Demand persistence.** Treat a trend as real only if it holds across 3+ consecutive panel runs. Single-run spikes and drops are sampling variance plus platform churn.
5. **Separate position from presence.** Losing position 1 while keeping citations is a different problem (title/slug gate -- see `skills/geo-fanout/`) than losing citations entirely (index/access -- see `skills/geo-ai-index-access/`).
6. **Expect the YouTube lane to swing.** Video-citation share moved 50+ points in 3 months in YMYL tracking (BrightEdge, Jan 2026) -- report YouTube citations as their own series (see `skills/geo-youtube/`).

---

## Output Format

Generate a file called `GEO-MEASUREMENT-PANEL.md` (panel definition + latest results):

```markdown
# AI Visibility Panel: [Domain]

**Panel Version:** [vN -- prompts frozen at definition]
**Panel Size:** [N] prompts | **Competitors:** [list]
**Cadence:** [weekly/biweekly] | **Engines:** [ChatGPT / AIO / AI Mode / Gemini / Perplexity]
**Latest Run:** [Date] | **Runs to Date:** [N]

---

## Headline Metrics (Rolling 4-8 Week Window)

| Engine | Share-of-Citation | Citation Rate | Avg Position | Trend (3+ runs?) |
|---|---|---|---|---|
| ChatGPT | [X]% | [X]% | [X.X] | [Up/Flat/Down -- persistent?] |
| Google AIO | [X]% | [X]% | [X.X] | [...] |
| Perplexity | [X]% | [X]% | [X.X] | [...] |

## Platform-Event Log

| Date | Engine | Event | Panel-Wide Impact |
|---|---|---|---|
| [date] | [engine] | [e.g., citation volume drop] | [all domains -X% = platform move, not site loss] |

## Co-Citation Clusters

| Sub-Query Cluster | Domains Cited With Us | Absent Competitor | Action |
|---|---|---|---|
| [cluster] | [domains] | [domain] | [fan-out build target / watch] |

## Notes for Stakeholders

- Raw counts are NOT reported as performance; share-of-citation is the metric (SparkToro).
- Position-1 citations carry ~4-5x position-5 CTR (⚠️ single vendor source).
- Trends require 3+ consecutive runs before action.
```

---

## Related Skills

- `skills/geo-fanout/` -- generates the panel's prompt set and consumes co-citation gap findings.
- `skills/geo-ai-index-access/` -- a sudden citation-rate collapse to zero usually means an index/access failure, not a content problem; check gates first.
- `skills/geo-youtube/` -- YouTube citations are a separate, high-volatility series.
- `skills/geo-compare/` -- monthly delta reports should consume this skill's share-of-citation series rather than raw counts.
