---
name: geo-ai-index-access
description: Index and access layer audit for AI search -- the hard prerequisites. Verifies Bing indexation (the ChatGPT entry ticket), audits robots.txt and CDN-level AI-crawler access, removes legacy nosnippet/max-snippet preview restrictions, and confirms key content is server-rendered. Use before any content-level GEO work, or when a site is invisible to ChatGPT despite good content.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# AI Index + Access Layer Skill

## Purpose

This skill audits the hard technical prerequisites for AI citation: being in the right index, being crawlable by AI agents, allowing content previews, and serving content in raw HTML. None of the content-level GEO work in this pack matters if these gates are closed. Run this audit FIRST, before `skills/geo-citability/`, `skills/geo-fanout/`, or any content strategy work.

## Core Insight

ChatGPT's retrieval pipeline runs on the **Bing index, not Google's**: 87% of ChatGPT citations match Bing top results, and Google appears nowhere in the pipeline (SubscribePR analysis, Jul 2026). A site can rank #1 on Google and be completely invisible to ChatGPT if Bing has not indexed it. Bing Webmaster Tools verification + sitemap submission + IndexNow is therefore the ChatGPT entry ticket -- and it also unlocks Bing WMT's AI Performance / Copilot citation data, one of the few first-party AI-visibility datasets available.

Beyond indexation, three access gates silently kill AI visibility:

1. **Crawler blocks** -- robots.txt or CDN/WAF rules blocking OAI-SearchBot, GPTBot, ChatGPT-User, PerplexityBot, or ClaudeBot. ~27% of B2B sites accidentally block AI agents at the CDN level (⚠️ industry estimate -- verify before quoting publicly).
2. **Preview restrictions** -- legacy `nosnippet` or restrictive `max-snippet` directives suppress AI citations. Scored 9.2/10 as a citation factor (Zyppy meta-analysis of 54 studies via DigitalApplied, Jun 2026).
3. **JavaScript-only content** -- ChatGPT-User reportedly performs no JavaScript rendering (⚠️ single source, SubscribePR Jul 2026). Content that only exists after client-side rendering is invisible to it.

---

## Audit Checklist (Execute in Order)

### Gate 1: Bing Indexation (ChatGPT Entry Ticket)

1. Check whether the site is verified in Bing Webmaster Tools. If not, that is the #1 finding -- verification + sitemap submission is the entry ticket.
2. Run `site:example.com` on Bing (WebFetch `https://www.bing.com/search?q=site:example.com`) and compare the indexed-page count against the sitemap count. A large gap = indexation problem.
3. Spot-check 5-10 money pages: is each one indexed on Bing?
4. Check whether IndexNow is implemented:
   - Look for an IndexNow key file at `[domain]/[key].txt`.
   - Check whether the CMS/build pipeline pings `https://api.indexnow.org/indexnow` (or the Bing equivalent) on publish/update.
   - If absent, recommend IndexNow integration -- it pushes new URLs to Bing (and other participating engines) at publish time instead of waiting for crawl.
5. Once verified, note that Bing WMT's **AI Performance (Copilot) report** becomes available -- first-party data on how often the site is cited in Copilot answers. This feeds `skills/geo-measurement/`.

### Gate 2: AI Crawler Access (robots.txt + CDN)

Full crawler-by-crawler procedure lives in `skills/geo-crawlers/`. The minimum viable checks for this audit:

1. Fetch `[domain]/robots.txt` and check for blocks on: `OAI-SearchBot`, `GPTBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot` -- plus wildcard (`User-agent: *`) disallow rules that catch them.
2. Check the CDN/WAF layer (Cloudflare, Akamai, etc.) -- robots.txt can be clean while the CDN blocks AI agents at the edge. ~27% of B2B sites have this problem accidentally (⚠️ industry estimate). Look for: managed bot-fight rules, AI-bot blocking toggles, WAF rules matching AI user-agents.
3. For each blocked Tier-1 crawler, record the exact rule and location (robots.txt line vs CDN config).

### Gate 3: Preview Control (nosnippet / max-snippet)

1. Fetch 5-10 key pages and check `<meta name="robots">` tags and `X-Robots-Tag` HTTP headers for:
   - `nosnippet` -- suppresses the text preview AI engines quote from. Remove unless there is a specific legal reason.
   - `max-snippet: [low number]` or `max-snippet: 0` -- a restrictive cap truncates what AI can extract. Remove or raise (e.g., `max-snippet: -1` for unlimited).
   - `noindex` on pages that should be cited -- sometimes inherited from staging or legacy SEO configs.
2. Also check for `noai`/`noimageai` tags (non-standard but some AI systems honor them).
3. Template-level check: grep the site's templates/theme for these directives -- one template rule can suppress the whole site. Factor weight: 9.2/10 (Zyppy via DigitalApplied, Jun 2026).

### Gate 4: Server-Rendered HTML

1. Fetch a key page with a plain HTTP client (curl/Bash) -- no JavaScript execution.
2. Check whether the key citable content (headings, answer paragraphs, data tables, prices) exists in the raw HTML response.
3. If the raw HTML is an empty shell (`<div id="root">` + script tags), flag it: ChatGPT-User reportedly does no JS rendering (⚠️ single source), and other AI crawlers have limited rendering (see `skills/geo-crawlers/` Step 5).
4. Recommend SSR/SSG or pre-rendering for content pages. App-like interactive pages matter less; content pages must render server-side.

### Gate 5: Google Side (AIO / AI Mode / Gemini)

1. Confirm the site is indexed on Google (`site:` query, Search Console coverage) -- Gemini grounding and AIO retrieval use Google's index.
2. Confirm no `Google-Extended` or `Googlebot` blocks that would limit AI-surface eligibility (see `skills/geo-crawlers/` for the nuance: Google-Extended controls training/AIO improvement, Googlebot controls indexing).
3. Note: llms.txt is NOT a substitute for any of this -- Google officially confirmed no machine-readable files are needed for generative AI search (Search Central, May 2026), and Zyppy scores llms.txt 2.0/10, lowest of 23 factors. Do not report llms.txt as an access fix.

---

## Scoring

| Gate | Weight | Pass Criteria |
|---|---|---|
| Bing indexation + IndexNow | 35% | Verified in Bing WMT, money pages indexed, IndexNow live |
| AI crawler access | 30% | All five Tier-1 AI crawlers allowed at robots.txt AND CDN level |
| Preview control | 20% | No nosnippet / restrictive max-snippet / stray noindex on citable pages |
| Server-rendered HTML | 15% | Key content present in raw HTML of all sampled pages |

Index + Access Score = weighted sum, 0-100. **Any Gate 1 or Gate 2 failure caps the score at 40** -- a site that is not indexed or not crawlable cannot be cited regardless of everything else.

---

## Output Format

Generate a file called `GEO-INDEX-ACCESS-AUDIT.md`:

```markdown
# AI Index + Access Audit: [Domain]

**Analysis Date:** [Date]
**Index + Access Score:** [X]/100
**Verdict:** [Ready / Blocked at Gate N]

---

## Gate Results

| Gate | Status | Findings |
|---|---|---|
| 1. Bing indexation + IndexNow | [Pass/Fail] | [WMT verified? indexed pages vs sitemap, IndexNow present?] |
| 2. AI crawler access | [Pass/Fail] | [Blocked crawlers + exact rule location: robots.txt line or CDN rule] |
| 3. Preview control | [Pass/Fail] | [nosnippet / max-snippet / noindex findings + template locations] |
| 4. Server-rendered HTML | [Pass/Fail] | [Sampled pages; which key content is missing from raw HTML] |
| 5. Google side | [Pass/Fail] | [Index coverage, Google-Extended status] |

## Fixes in Priority Order

1. [e.g., "Verify in Bing Webmaster Tools + submit sitemap + deploy IndexNow key" -- ChatGPT entry ticket]
2. [e.g., "Remove `User-agent: GPTBot / Disallow: /` at robots.txt line 12"]
3. [e.g., "Remove `nosnippet` from the base template -- suppresses AI citation previews sitewide"]
4. [e.g., "Move article body from client-rendered React into SSR output"]

## Unlocked Data Sources

- [ ] Bing WMT AI Performance (Copilot) report -- feeds geo-measurement panels
- [ ] Bing WMT keyword data -- feeds geo-fanout sub-query mapping
```

---

## Related Skills

- `skills/geo-crawlers/` -- the full 14-crawler reference, tiering, and robots.txt recommendation matrix. This skill runs the minimum viable subset; run geo-crawlers for the complete access map.
- `skills/geo-fanout/` -- once indexed, sub-query coverage determines what the engines retrieve.
- `skills/geo-citability/` -- content-level optimization; only worth doing after all five gates pass.
- `skills/geo-measurement/` -- Bing WMT's AI Performance data unlocked here feeds the measurement panels.
