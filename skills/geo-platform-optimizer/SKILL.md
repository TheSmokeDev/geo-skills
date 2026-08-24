---
name: geo-platform-optimizer
description: Platform-specific AI search optimization — audit and optimize for Google AI Overviews, ChatGPT, Perplexity, Gemini, and Bing Copilot individually
metadata:
  version: "1.0.0"
  author: geo-seo-claude
  tags: [geo, ai-search, platform-optimization, chatgpt, perplexity, gemini, aio]
---

# GEO Platform Optimizer

## Core Insight

Only **11% of domains** are cited by BOTH ChatGPT and Google AI Overviews for the same query. Each AI search platform uses different indexes, ranking logic, and source preferences. A page optimized for Google AI Overviews may be invisible to ChatGPT, and vice versa. Platform-specific optimization is not optional — it is the foundation of any serious GEO strategy.

## How to Use This Skill

1. Collect the target URL and the site's primary topic/industry
2. Run each platform checklist below against the site
3. Score each platform on the 0-100 rubric
4. Generate GEO-PLATFORM-OPTIMIZATION.md with per-platform scores, gaps, and action items

---

## Platform 1: Google AI Overviews (AIO)

### How AIO Selects Sources
- Only **38% of AIO-cited URLs rank in the organic top 10** — down from 76% (Ahrefs, 863K SERPs / 4M URLs, Mar 2026). 31% of citations come from positions 11-100 and 31% from beyond position 100. The cause is Gemini 3 (Jan 2026) query fan-out pulling from sub-query SERPs — page-3 organic is NOT disqualifying
- Fan-out coverage is the new meta-factor (Zyppy scores it 9.3/10, Jun 2026): engines rewrite one prompt into a cluster of sub-queries and retrieve per sub-query. Win the cluster, not the head term
- AIO strongly favors pages with **clean structure, direct answers, and scannable formatting**
- Featured snippet optimization has meaningful overlap with AIO optimization
- AIO prefers **concise, factual, unambiguous answers** — hedging and filler reduce citation probability
- **Google AI Mode is a separate surface, not a bigger AIO:** AIO↔AI Mode URL overlap is only 13.7%, and AI Mode has 1B MAU (AIO 2.5B) with scarcer citation slots — 4.3 citations per response vs 10.3 in classic search (Shadow, Jul 2026 — ⚠️ secondary source). Optimize for them as distinct targets

### 2026 Citation Surfaces Beyond the AIO Box

Google's citation real estate now extends beyond AIO and AI Mode themselves:

- **Preferred Sources** — users can star favorite outlets and get boosted Top Stories placement plus a dedicated "From your sources" section (Google Search blog, Aug 2025, US/India English launch; broader rollout through 2026). This is a Top Stories surface, NOT an AIO mechanism — but for news-adjacent queries it is part of the brand's total Google citation footprint. Earning a user's "preferred" star compounds like a subscription; publishers can link directly to a follow flow.
- **"Highly Cited" badges, Community Perspectives, and link carousels** — additional in-SERP citation modules attributed to the Google I/O May 2026 announcements. ⚠️ Thin-sourced: this comes from rival skill-pack I/O 2026 notes and we have NOT independently confirmed rollout status or the exact selection mechanics. Treat as watch items — if these modules appear in your SERPs, they are additional extractable surfaces — but do not score them in the rubric until the mechanics are verified.
- **Common thread:** every new surface still extracts from the same primitives — direct answers, tables, dated authorship, entity clarity. Optimizing the fundamentals covers surfaces that ship faster than any checklist can track.

### Optimization Checklist

1. **Question-Based Headings**: Use H2/H3 headings phrased as questions matching real user queries. Check Google's "People Also Ask" for the target topic and mirror those exact phrasings.
2. **Direct Answer in First Paragraph**: After each question heading, provide a clear 1-2 sentence answer immediately. Then expand with supporting detail. The first sentence should be a standalone citation candidate.
3. **Tables and Structured Comparisons**: AIO heavily cites tables. Convert any comparison, pricing, specification, or feature data into HTML tables. Use clear column headers.
4. **Ordered and Unordered Lists**: Step-by-step processes should use ordered lists. Feature lists should use unordered lists. AIO extracts these directly.
5. **FAQ Sections**: Add a dedicated FAQ section with 5-10 real questions. Use proper H3 headings for each question. While FAQPage schema rich results are restricted to govt/health sites since Aug 2023, the content pattern still helps AIO extraction.
6. **Definitions and Glossary Boxes**: For any industry-specific term, provide a clear definition. Format: "**[Term]** is [concise definition]." AIO frequently cites definitions.
7. **Statistics with Sources**: Include specific numbers with attribution. "According to [Source], [statistic]." AIO prefers citeable, specific claims over vague assertions.
8. **Publication Date**: Include a visible publication date and last-updated date. AIO deprioritizes undated content for time-sensitive queries.
9. **Author Byline**: Display author name with credentials. Link to an author page with bio, credentials, and sameAs links.
10. **Page Depth**: Keep target pages within 3 clicks of homepage. AIO rarely cites deep, orphaned content.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Ranks for target queries / covers fan-out sub-queries | 20 | 20 if top 10, 10 if top 100 or strong sub-query coverage, 0 if invisible |
| Question-based headings present | 10 | 2 points per question heading, max 10 |
| Direct answers after headings | 15 | 3 points per direct answer, max 15 |
| Tables present for comparison data | 10 | 10 if tables used appropriately, 5 if partial, 0 if absent |
| Lists for processes/features | 10 | 10 if present, 5 if partial |
| FAQ section with 5+ questions | 10 | 10 if 5+, 5 if 1-4, 0 if none |
| Statistics with citations | 10 | 2 points per cited stat, max 10 |
| Publication/updated date visible | 5 | 5 if both dates, 3 if one, 0 if none |
| Author byline with credentials | 5 | 5 if full byline, 3 if name only, 0 if none |
| Clean URL + heading hierarchy | 5 | 5 if H1>H2>H3 clean, 3 if minor issues, 0 if broken |

---

## Platform 2: ChatGPT Web Search

### How ChatGPT Selects Sources
- Retrieval runs on the **Bing index** — 87% of ChatGPT citations match Bing results, and there is NO Google anywhere in the pipeline (Subscribe PR, Jul 2026 — ⚠️ single source, but mechanism-consistent). Bing indexation + IndexNow is the hard prerequisite for ChatGPT visibility
- Citation ref_type hierarchy (Ahrefs, 1.4M prompts, Apr 2026): search 88.46%, news 12.01%, **reddit 1.93%**, youtube 0.51%, academia 0.40%
- **Reddit is consensus-shaping, not citation-earning.** Reddit is retrieved at scale but cited at only 1.93% of ref_types, and its citation share collapsed from ~60% to ~10% in Sept 2025 (5WPR State of AI Citations, May 2026). Reddit shapes what models SAY about your brand (training/consensus layer), not what they LINK to
- ChatGPT heavily weights **entity recognition** — if your brand exists as a structured entity (Wikipedia, Wikidata, Crunchbase), it is far more likely to be cited
- Branded web mentions are the strongest measured off-site signal (r=0.664 — Ahrefs 75K brands, Jul 2026); raw backlink counts are the weakest measured play (⚠️ precise 0.218 figure has no locatable primary source — directional only, never quote in client/public copy)
- Freshness bias is the strongest of any platform: cited URLs average 25.7% fresher than Google organic results (Ahrefs, 17M citations, 2025-26) — NOT the viral "4.3x" figure, which is untraceable
- Title and URL slug matter before content is even read: cited-URL titles score 0.656 cosine similarity to fan-out queries vs 0.484 for non-cited; natural-language slugs are cited at 89.78% vs 81.11% (Ahrefs, Apr 2026)

### Optimization Checklist

1. **Wikipedia Presence**: Check if the brand/person/product has a Wikipedia article. If not, assess notability criteria. If notable, create a draft. If an article exists, ensure it is accurate and current.
2. **Wikidata Entity**: Verify the entity exists on Wikidata (wikidata.org). If not, create a Wikidata item with key properties: instance of, official website, social media links, founding date, headquarters location.
3. **Bing Webmaster Tools**: Verify the site is registered in Bing Webmaster Tools. Submit sitemap. Check for crawl errors. Enable **IndexNow** so new and updated pages hit the Bing index in near-real-time — this is the hard prerequisite for ChatGPT citation (87% of citations match Bing results).
4. **Bing Index Coverage**: Use `site:domain.com` on Bing to verify key pages are indexed. Bing may have different indexed pages than Google — and Google indexation alone does nothing for ChatGPT.
5. **Reddit Consensus**: Check for brand mentions on Reddit. The goal is shaping what models SAY about the brand (Reddit feeds the consensus/training layer), not earning citations — Reddit is only 1.93% of ChatGPT ref_types (Ahrefs, Apr 2026). Assess whether the brand participates authentically; paid or seeded mentions are spam-filtered and do not correlate.
6. **YouTube Presence**: Verify YouTube channel exists with relevant content. Video descriptions should contain full URLs and entity information.
7. **Brand Mention Profile**: Audit branded web mentions across publications, forums, and reviews — branded mentions correlate at r=0.664 with AI visibility while raw backlink counts are far weaker (⚠️ the 0.218 figure has no locatable primary source — directional only) (Ahrefs 75K brands, Jul 2026). Do not pitch press-release wires: wire pickups are ~0.04% of citations (BuzzStream, 4M citations) and are spam-filtered.
8. **Entity Consistency**: Brand name, founding date, leadership, and key facts must be consistent across Wikipedia, Crunchbase, LinkedIn, and the official website.
9. **Comprehensive Content**: Pages targeting ChatGPT citation should be **2000+ words** with thorough topic coverage. ChatGPT prefers single authoritative sources over combining multiple thin pages.
10. **Clear Attribution**: Include "About" sections, company descriptions, and founding stories. ChatGPT uses these for entity grounding.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Wikipedia article exists and is accurate | 20 | 20 if exists, 10 if stub, 0 if none |
| Wikidata entity with 5+ properties | 10 | 10 if complete, 5 if basic, 0 if none |
| Bing index coverage of key pages | 10 | 10 if full, 5 if partial, 0 if poor |
| Reddit consensus presence (authentic) | 10 | 10 if active discussions, 5 if mentions, 0 if none — shapes model output, not citations |
| YouTube channel with relevant content | 10 | 10 if active, 5 if present but sparse, 0 if none |
| Branded web mentions (publications, forums, reviews) | 15 | 3 points per mention category with authentic coverage, max 15 |
| Entity consistency across platforms | 10 | 10 if consistent, 5 if minor discrepancies, 0 if major |
| Content comprehensiveness (2000+ words) | 10 | 10 if thorough, 5 if adequate, 0 if thin |
| Bing Webmaster Tools configured | 5 | 5 if verified, 0 if not |

---

## Platform 3: Perplexity AI

### How Perplexity Selects Sources
- Runs its **own index plus an L3 reranker**, so Bing is not the hard gate here the way it is for ChatGPT
- Historically Reddit-heavy, but Reddit's citation share collapsed from ~60% to ~10% in Sept 2025 (5WPR, May 2026) — treat community presence as consensus-shaping that influences what the model says, not as a citation farm
- Perplexity places the **heaviest emphasis on community validation** of all AI search platforms
- Cites **multiple sources per answer** (8.3 URLs on average), so there is more opportunity for mid-authority sites to appear
- Strong freshness weighting and a documented preference for page quality over domain authority — list and comparison pages dominate (May-2026 findings still hold)

### Optimization Checklist

1. **Active Reddit Presence**: The brand or its representatives should participate authentically in relevant subreddit discussions. Not promotional — helpful, specific, and community-oriented.
2. **Reddit AMAs and Threads**: Encourage or participate in AMAs, detailed discussion threads, and community Q&As. Perplexity treats these as high-signal content.
3. **Forum and Community Presence**: Beyond Reddit, check Hacker News, Stack Overflow, Quora, and niche industry forums. Perplexity indexes these heavily.
4. **Discussion-Friendly Content**: Publish content that invites discussion — opinion pieces, research findings, contrarian takes, original data. Content that gets shared and debated in communities ranks higher.
5. **Freshness Signals**: Publish content with clear dates. Update content regularly. Perplexity deprioritizes stale content more aggressively than other platforms.
6. **Multiple Source Validation**: Claims in your content should be supported by other sources. Perplexity cross-references and prefers claims it can verify from multiple origins.
7. **YouTube Video Content**: Create video content that Perplexity can reference. Ensure video titles, descriptions, and transcripts contain target information.
8. **Direct, Quotable Passages**: Write paragraphs that can stand alone as citations. Each paragraph should make one clear point with supporting evidence.
9. **Original Data and Research**: Publish original surveys, benchmarks, case studies, or datasets. Perplexity heavily favors primary sources.
10. **Perplexity Pages**: Check if Perplexity has created a "Page" about your topic/brand. These are curated summaries that influence future citations.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Active Reddit presence in relevant subreddits | 20 | 20 if active contributor, 10 if mentioned, 0 if absent — value is consensus-shaping, not direct citation share |
| Forum/community mentions (HN, SO, Quora) | 10 | 10 if multiple platforms, 5 if one, 0 if none |
| Content freshness (updated within 6 months) | 10 | 10 if recent, 5 if within year, 0 if older |
| Original research/data published | 15 | 15 if original research, 10 if case studies, 5 if some data, 0 if none |
| YouTube content with transcripts | 10 | 10 if active channel, 5 if some videos, 0 if none |
| Quotable, standalone paragraphs | 10 | 2 points per well-structured quotable paragraph, max 10 |
| Multi-source claim validation | 10 | 10 if claims well-sourced, 5 if some sourcing, 0 if none |
| Discussion-generating content | 10 | 10 if content gets shared/discussed, 5 if some engagement, 0 if none |
| Wikipedia/Wikidata presence | 5 | 5 if present, 0 if absent |

---

## Platform 4: Google Gemini

### How Gemini Selects Sources
- Grounded in **Google Search** (indexation is the entry ticket) but its own surface: Gemini↔AI Mode source overlap is only 27% (BrightEdge via Frase, Jun 2026) — do not assume AIO optimization covers the Gemini app
- Leans **entity/brand presence across Google's ecosystem** (YouTube, Google Business Profile, LinkedIn, Knowledge Graph); source mix skews LinkedIn, Medium, Quora, Reddit, Wikipedia
- YouTube content is weighted significantly more heavily than in standard Google Search
- Google Business Profile data is directly accessible to Gemini
- Gemini uses Google's Knowledge Graph directly — entity presence in Knowledge Graph is a major advantage
- Structured data helps Gemini parse entity facts, but per the Ahrefs controlled study (May 2026) markup alone does not lift citations — the extractable facts do
- Gemini multi-modal: can reference images, videos, and text together

### Optimization Checklist

1. **Google Knowledge Panel**: Check if the brand has a Google Knowledge Panel. If not, claim it through Google Business Profile or structured data. Ensure all information is accurate.
2. **Google Business Profile**: Complete and optimize GBP with all fields: hours, services, photos, posts, Q&A. Gemini pulls directly from GBP for local queries.
3. **YouTube Strategy**: Create YouTube content for every key topic. Optimize titles, descriptions, timestamps, and closed captions. Gemini cites YouTube more than any other AI platform.
4. **YouTube Chapters and Timestamps**: Use chapters (timestamps in description) so Gemini can reference specific segments of videos.
5. **Google Merchant Center**: For e-commerce, ensure products are in Google Merchant Center. Gemini references product data directly.
6. **Structured Data (Schema.org)**: Implement comprehensive Schema.org markup for entity clarity (Organization + sameAs). Frame expectations correctly: it keeps entity data unambiguous, but controlled testing (Ahrefs, May 2026) shows no direct citation lift from markup alone.
7. **Google Sites Ecosystem**: Ensure presence across Google ecosystem: Google Scholar (for research), Google News (for publishers), Google Maps (for local).
8. **Image Optimization**: Gemini is multi-modal. Use descriptive alt text, structured image filenames, and high-quality images. Include relevant images with every piece of content.
9. **Google E-E-A-T Signals**: All standard Google E-E-A-T signals apply with extra weight. Author pages, about pages, editorial policies, and expertise demonstrations.
10. **Chrome Web Store / Google Workspace Marketplace**: For software companies, presence on Google platforms adds entity signals.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Google Knowledge Panel exists | 15 | 15 if complete, 10 if partial, 0 if none |
| Google Business Profile complete | 10 | 10 if fully optimized, 5 if basic, 0 if none |
| YouTube channel with topic-relevant content | 20 | 20 if active with chapters, 10 if present, 0 if none |
| Schema.org structured data implemented | 15 | 15 if comprehensive, 10 if basic, 5 if minimal, 0 if none |
| Google ecosystem presence (Scholar, News, Maps) | 10 | 10 if 3+, 5 if 1-2, 0 if none |
| Image optimization (alt text, filenames) | 10 | 10 if all images optimized, 5 if partial, 0 if none |
| E-E-A-T signals (author pages, about, editorial) | 10 | 10 if strong, 5 if partial, 0 if weak |
| Google Merchant Center (if e-commerce) | 5 | 5 if applicable and active, N/A otherwise |
| Multi-modal content (text + images + video) | 5 | 5 if rich multi-modal, 3 if some, 0 if text-only |

---

## Platform 5: Bing Copilot

### How Copilot Selects Sources
- Uses **Bing's search index** (shared infrastructure with ChatGPT but different ranking/selection)
- Supports **IndexNow protocol** for near-instant indexing of new and updated content
- Copilot tends to cite **fewer sources per answer** (typically 3-5) but gives more prominent attribution
- Microsoft ecosystem integration: LinkedIn, GitHub, Microsoft Learn content is weighted
- Copilot prefers pages with clear, structured markup and fast load times

### Optimization Checklist

1. **Bing Webmaster Tools**: Register and verify site. Submit XML sitemap. Review and fix any crawl issues.
2. **IndexNow Implementation**: Implement the IndexNow protocol to notify Bing of content changes in real-time. Submit a key file at `/.well-known/indexnow-key.txt` and ping the IndexNow API on content publish/update.
3. **LinkedIn Company Page**: Ensure the company LinkedIn page is complete with accurate description, employee connections, and regular posts. Copilot indexes LinkedIn content.
4. **GitHub Presence**: For tech companies, maintain an active GitHub presence. Copilot references GitHub repos, documentation, and README files.
5. **Microsoft Learn / Documentation**: If relevant, contribute to Microsoft Learn or ensure documentation is compatible with Microsoft's documentation standards.
6. **Bing Places for Business**: Equivalent to Google Business Profile. Complete all fields for local search visibility in Copilot.
7. **Clear Meta Descriptions**: Bing/Copilot weights meta descriptions more heavily than Google does. Write compelling, keyword-rich meta descriptions for every page.
8. **Social Signals**: Bing has historically weighted social signals (shares, likes, engagement) more than Google. Maintain active social media presence.
9. **Exact-Match Keywords**: Bing's algorithm is more literal about keyword matching than Google. Include exact target phrases in titles, headings, and body content.
10. **Fast Page Load**: Copilot deprioritizes slow pages. Target sub-2-second load time. Optimize images, enable compression, minimize render-blocking resources.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Bing Webmaster Tools verified + sitemap | 15 | 15 if verified, 5 if partial, 0 if not |
| IndexNow protocol implemented | 15 | 15 if active, 0 if not |
| Bing index coverage of key pages | 10 | 10 if full, 5 if partial, 0 if poor |
| LinkedIn company page (complete) | 10 | 10 if complete, 5 if basic, 0 if none |
| GitHub presence (if applicable) | 5 | 5 if active, N/A if not applicable |
| Meta descriptions optimized | 10 | 10 if all key pages, 5 if partial, 0 if missing |
| Social media engagement signals | 10 | 10 if active engagement, 5 if present, 0 if none |
| Exact-match keywords in titles/headings | 10 | 10 if well-optimized, 5 if partial, 0 if not |
| Page load speed < 2 seconds | 10 | 10 if < 2s, 5 if < 4s, 0 if > 4s |
| Bing Places configured (if local) | 5 | 5 if complete, N/A if not local |

---

## Cross-Platform Summary

### Universal Optimization Actions (help ALL platforms)
1. Wikipedia/Wikidata entity presence
2. YouTube channel with relevant content
3. Comprehensive, well-structured content with clear headings
4. Schema.org structured data for entity clarity (Organization + sameAs) — rich results and unambiguous entities, not a citation lever
5. Fast page load and clean HTML
6. Author pages with credentials and sameAs links
7. Regular content updates with visible dates
8. Authentic branded web mentions across publications and communities (r=0.664 — the strongest measured off-site signal, Ahrefs 75K brands, Jul 2026)

### Platform-Specific Priorities
| Priority | Google AIO | ChatGPT | Perplexity | Gemini | Copilot |
|---|---|---|---|---|---|
| #1 | Fan-out sub-query coverage | Bing indexation + IndexNow | Original research | YouTube | IndexNow |
| #2 | Q&A structure | Entity graph | Page quality + freshness | Knowledge Panel | Bing WMT |
| #3 | Tables/lists | Brand mentions | Community consensus | Entity/brand presence | LinkedIn |
| #4 | Featured snippets | Title/slug match to fan-out queries | Discussion-friendly content | GBP | Meta descriptions |

---

## Output Format

Generate **GEO-PLATFORM-OPTIMIZATION.md** with the following structure:

```markdown
# GEO Platform Optimization Report — [Domain]
Date: [Date]

## Overall Platform Readiness
- Combined GEO Score: XX/100 (average of all platform scores)

## Platform Scores
| Platform | Score | Status |
|---|---|---|
| Google AI Overviews | XX/100 | [Strong/Moderate/Weak] |
| ChatGPT Web Search | XX/100 | [Strong/Moderate/Weak] |
| Perplexity AI | XX/100 | [Strong/Moderate/Weak] |
| Google Gemini | XX/100 | [Strong/Moderate/Weak] |
| Bing Copilot | XX/100 | [Strong/Moderate/Weak] |

Status thresholds: Strong = 70+, Moderate = 40-69, Weak = 0-39

## Platform Details
[Per-platform breakdown with score, gaps found, specific actions]

## Prioritized Action Plan
### Quick Wins (this week)
[Actions that improve multiple platform scores with minimal effort]

### Medium-Term (this month)
[Actions requiring content creation or technical changes]

### Strategic (this quarter)
[Actions requiring entity building, community development, or platform presence]
```
