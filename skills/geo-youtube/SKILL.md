---
name: geo-youtube
description: YouTube citation playbook for AI search. YouTube is the most-cited domain in Google AI Overviews and the strongest single brand-visibility signal measured. Optimizes videos for AI citation through transcripts, chapters, titles, and cross-posted text claims -- not views or subscribers. Use when planning video content for AI visibility or auditing an existing channel for citation readiness.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# YouTube Citation Playbook Skill

## Purpose

This skill turns a YouTube channel into an AI citation source. AI engines do not watch video -- they read the transcript, chapters, title, and description. That makes YouTube a **rank-free bypass lane**: a channel with no domain authority and few views can earn AI citations that the site's text pages cannot. This skill audits existing videos for citation readiness and produces a build spec for new ones.

## Core Insight

YouTube completed the flip in 2026 and is now the dominant non-text citation source:

- **Most-cited domain in Google AIOs overall**, with share up +34% over 6 months (Ahrefs Brand Radar, 2026).
- **#1 social citation source at 38.1%** of social citations, overtaking Reddit (5WPR State of AI Citations, May 2026).
- **~23% of finance-vertical citations** -- ahead of Wikipedia (7.3%) and LinkedIn (6.8%) (Surfer 46M-citation dataset, 2026).
- **18.2% of AIO citations from beyond the organic top 100 are YouTube URLs** (Ahrefs, 863K SERPs / 4M URLs, Mar 2026) -- the clearest rank-free lane in AI search.
- **YouTube mentions correlate r=0.737 with AI visibility -- the strongest single signal ever measured**, ahead of branded web mentions (0.664) and backlinks (0.218) (Ahrefs 75K-brand study via MachineRelations, Jul 2026).

The mechanism that matters: **AI reads the transcript, chapters, title, and description -- NOT the video itself.** Views and subscriber counts show near-zero correlation with citation (⚠️ single source, AIOCopilot Apr 2026 -- but mechanism-consistent, since engines have no visibility into watch metrics at retrieval time).

---

## Citation-Readiness Rubric (per video)

Score each video 0-100 across five components:

| Component | Weight | Full Marks | Zero Marks |
|---|---|---|---|
| Transcript quality | 30% | Human-corrected transcript with citable numeric/definitional sentences | Auto-captions left uncorrected, or no captions |
| Chapter structure | 25% | 6-12 chapters with descriptive, query-matching titles | No chapters, or generic titles ("Part 1", "Intro") |
| Title match | 20% | Title is verbatim (or near-verbatim) the target query | Clever/branded title with no query language |
| Length & depth | 15% | 10+ minutes, substantive per-chapter content | Under 3 minutes, or a Short |
| Cross-posting | 10% | Video's claims exist as a text page + community answer | Video exists in isolation |

Shorts are **never cited** -- exclude them from the audit entirely (AIOCopilot, Apr 2026).

---

## Audit Procedure (Existing Channel)

1. List the channel's long-form videos (10+ min candidates first).
2. For each video, fetch title, description, chapter list, and transcript (YouTube timedtext API or transcript endpoints).
3. Check the transcript for:
   - Auto-caption errors (numbers, brand names, and technical terms mangled) -- flag for human correction.
   - Citable sentences: numeric claims and definitional statements, especially within ~30 seconds of chapter boundaries (citations attach to timestamps).
4. Check chapter titles: each should read like an H2 that matches a fan-out sub-query (see `skills/geo-fanout/` for sub-query mapping). "How much does SR-22 cost in California?" beats "Pricing section".
5. Check title against the target query: verbatim or near-verbatim match is the goal.
6. Check cross-posting: do the video's core claims exist as a text page on the site and as a community answer (Reddit/Quora/forum)? **ChatGPT cites YouTube mainly when the video is discussed in text elsewhere** (AIOCopilot, Apr 2026).
7. Score per the rubric; produce the fix list ordered by transcript quality first.

## Build Spec (New Videos)

For each target query, spec a video as follows:

1. **Title:** verbatim the target query. "How Much Does SR-22 Insurance Cost in California? (2026)" -- not "Everything You Need to Know About SR-22!".
2. **Length:** 10+ minutes. Shorts never cited; long-form gives chapters room to work.
3. **Chapters:** 6-12, each titled like an H2 matching a fan-out sub-query (cost, eligibility, process, location, language variants -- see `skills/geo-fanout/`). Citations attach to timestamps, so chapter titles are the retrieval surface.
4. **Script for citable sentences:** place numeric and definitional claims near chapter boundaries. "The average SR-22 filing fee in California is $25, and SR-22 insurance raises premiums by 40-80% depending on the violation" is citable; "it can get pretty pricey" is not. Apply the `skills/geo-citability/` passage rules to the script.
5. **Transcript:** upload a human-corrected transcript. Do not rely on auto-captions -- mangled numbers destroy citability.
6. **Description:** front-load the same numeric/definitional claims; engines read it.
7. **Production:** a faceless explainer with a corrected transcript qualifies -- production value is not the ranking lever here (AIOCopilot, Apr 2026).
8. **Cross-post (mandatory):** publish the video's claims as (a) a text page on the site and (b) an authentic community answer (Reddit, Quora, niche forum) linking or naming the video. Text discussion is what makes ChatGPT surface the video.

---

## Caveat: Treat YouTube Citation Share as a Live Experiment

YMYL video-citation share **swung 50+ percentage points in 3 months** in BrightEdge's healthcare tracking (Jan 2026). Platforms are actively A/B testing how heavily they cite video. Do not promise a stable citation share to clients; track the channel's actual citation rate over time with `skills/geo-measurement/` and rebalance if the lane narrows.

---

## Output Format

Generate a file called `GEO-YOUTUBE-CITATION.md`:

```markdown
# YouTube Citation Audit: [Channel/Domain]

**Analysis Date:** [Date]
**Videos Audited:** [N] long-form (Shorts excluded -- never cited)
**Average Citation-Readiness Score:** [X]/100

---

## Per-Video Scores

| Video | Transcript (30) | Chapters (25) | Title (20) | Length (15) | Cross-Post (10) | Total |
|---|---|---|---|---|---|---|
| [Title] | [X] | [X] | [X] | [X] | [X] | [X]/100 |

## Priority Fixes

1. **[Video]** -- [e.g., "Auto-captions mangle every dollar figure; upload corrected transcript"]
2. **[Video]** -- [e.g., "Retitle to verbatim target query: '...'"]
3. **[Video]** -- [e.g., "Add 8 chapters titled as fan-out sub-queries"]

## New Video Build Specs

| Target Query | Title | Chapters | Key Citable Claims | Cross-Post Plan |
|---|---|---|---|---|
| [query] | [verbatim title] | [6-12 chapter titles] | [numeric/definitional sentences] | [text page + community answer] |

## Volatility Note

[Reminder: YMYL video-citation share swung 50+ points in 3 months (BrightEdge, Jan 2026).
 Track actual citations with geo-measurement; do not promise stable share.]
```

---

## Related Skills

- `skills/geo-fanout/` -- supplies the sub-queries that chapter titles and video titles should match.
- `skills/geo-citability/` -- passage rules apply verbatim to scripts, transcripts, and descriptions.
- `skills/geo-brand-mentions/` -- YouTube mentions are the strongest measured brand signal (r=0.737); the mention strategy and the citation strategy reinforce each other.
- `skills/geo-measurement/` -- track YouTube citation share over time given the documented volatility.
