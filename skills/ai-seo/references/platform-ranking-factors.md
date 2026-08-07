# How Each AI Platform Picks Sources

Each AI search platform has its own search index, ranking logic, and content preferences. This guide covers what matters for getting cited on each one.

Sources cited throughout: Princeton GEO study (KDD 2024), Ahrefs citation and brand-signal studies (2025-26), ZipTie content-answer fit analysis, 5WPR State of AI Citations (May 2026).

---

## The Fundamentals

Every AI platform shares three baseline requirements:

1. **Your content must be in their index** — Each platform uses a different search backend (Google, Bing, Brave, or their own). If you're not indexed, you can't be cited.
2. **Your content must be crawlable** — AI bots need access via robots.txt. Block the bot, lose the citation.
3. **Your content must be extractable** — AI systems pull passages, not pages. Clear structure and self-contained paragraphs win.

Beyond these basics, each platform weights different signals. Here's what matters and where.

---

## Google AI Overviews

Google AI Overviews pull from Google's own index and lean heavily on E-E-A-T signals (Experience, Expertise, Authoritativeness, Trustworthiness). They appear in roughly 45% of Google searches.

**What makes Google AI Overviews different:** They already have your traditional SEO signals — backlinks, page authority, topical relevance. The additional AI layer adds a preference for content with cited sources and structured data. Research shows that including authoritative citations in your content correlates with a 132% visibility boost, and writing with an authoritative (not salesy) tone adds another 89%.

**Importantly, AI Overviews don't just recycle the traditional Top 10 — and the overlap is shrinking.** Only **38% of AIO-cited URLs ranked in the organic top 10** in 2026, down from 76% (Ahrefs, 863K SERPs / 4M URLs, Mar 2026); 31% of citations come from positions 11-100 and 31% from beyond position 100. The cause is Gemini 3 query fan-out: one prompt is rewritten into a cluster of sub-queries and citations are pulled from sub-query SERPs. Pages that wouldn't crack page 1 in traditional search can still get cited if they cover the fan-out cluster with clear, extractable answers. Also note that **Google AI Mode is a separate surface** — only 13.7% URL overlap with AIO and 1B MAU (Shadow, Jul 2026 — ⚠️ secondary source).

**What to focus on:**
- Cover the query fan-out: own the sub-query space around your topic, not just the head term (Zyppy scores fan-out coverage 9.3/10, the top factor in its 23-factor meta-analysis, Jun 2026)
- Schema markup is for rich results and entity clarity, NOT citations — in the Ahrefs controlled study (1,885 pages adding JSON-LD, May 2026), citations moved ChatGPT +2.2%, AI Mode +2.4%, AIO -4.6%, all within noise
- Build topical authority through content clusters with strong internal linking
- Include named, sourced citations in your content (not just claims)
- Author bios with real credentials matter — E-E-A-T is weighted heavily
- Get into Google's Knowledge Graph where possible (an accurate Wikipedia entry helps)
- Target "how to" and "what is" query patterns — these trigger AI Overviews most often

---

## ChatGPT

ChatGPT's web search retrieves from the **Bing index** — 87% of citations match Bing results, with no Google anywhere in the pipeline (Subscribe PR, Jul 2026). It combines this with its training knowledge to generate answers, then cites the web sources it relied on. If Bing hasn't indexed you, ChatGPT can't cite you — Bing Webmaster Tools + IndexNow is the hard prerequisite.

**What makes ChatGPT different:** Brand signals outweigh traditional authority metrics. An Ahrefs analysis of 75,000 brands (Jul 2026) found branded web mentions correlate with AI visibility at r=0.664, brand search volume at 0.392, domain rating at only ~0.18-0.33, and raw backlink counts at r=0.218 — the weakest measured signal. YouTube mentions are the strongest single signal ever measured at r=0.737. Chasing backlink counts is the lowest-yield play; earning authentic brand mentions is the highest.

**Freshness is a real but modest differentiator.** Cited URLs average **25.7% fresher** than Google organic results, and ChatGPT's freshness bias is the strongest of any platform — cited URLs skew ~458 days newer than organic (Ahrefs, 17M citations, 2025-26). The viral "fresh content gets cited 4.3x more" figure is untraceable; don't quote it.

**The most important signal is content-answer fit** — a ZipTie analysis of 400,000 pages found that how well your content's style and structure matches ChatGPT's own response format accounts for about 55% of citation likelihood. This is far more important than domain authority (12%) or on-page structure (14%) alone. Write the way ChatGPT would answer the question, and you're more likely to be the source it cites.

**Where ChatGPT looks beyond your site:** its citation ref_types break down as search 88.46%, news 12.01%, Reddit 1.93%, YouTube 0.51%, academia 0.40% (Ahrefs, 1.4M prompts, Apr 2026). Reddit's small direct share is the reframe to internalize: Reddit shapes what the model SAYS (consensus/training layer) far more than what it LINKS — and Reddit's citation share collapsed from ~60% to ~10% in Sept 2025 (5WPR, May 2026).

**What to focus on:**
- Get indexed by Bing and keep it fresh via IndexNow — no Bing indexation, no ChatGPT citation
- Earn authentic branded web mentions (publications, reviews, communities) — r=0.664 vs 0.218 for backlinks
- Structure your content the way ChatGPT structures its answers (conversational, direct, well-organized)
- Include verifiable statistics with named sources
- Match titles and URL slugs to the questions engines fan out into — cited-URL titles score 0.656 cosine similarity to fan-out queries vs 0.484 for non-cited (Ahrefs, Apr 2026)
- Clean heading hierarchy (H1 > H2 > H3) with descriptive headings

---

## Perplexity

Perplexity always cites its sources with clickable links, making it the most transparent AI search platform. It runs its **own index plus an L3 reranker** — initial relevance retrieval, then traditional ranking factor scoring, then ML-based quality evaluation that can discard entire result sets if they don't meet quality thresholds. Because it doesn't depend on Bing, the Bing-indexation gate that applies to ChatGPT does not apply here.

**What makes Perplexity different:** It's the most "research-oriented" AI search engine, and its citation behavior reflects that. Perplexity maintains curated lists of authoritative domains (Amazon, GitHub, major academic sites) that get inherent ranking boosts. It uses a time-decay algorithm that evaluates new content quickly, giving fresh publishers a real shot at citation.

**Perplexity has unique content preferences:**
- **FAQ Schema (JSON-LD)** — Makes Q&A pairs trivially extractable. Frame it as parsability, not a citation guarantee: the Ahrefs controlled study (May 2026) found no citation lift from markup alone, though schema carrying concrete extractable facts may still correlate (SSRN, Feb 2026)
- **PDF documents** — Publicly accessible PDFs (whitepapers, research reports) are prioritized. If you have authoritative PDF content gated behind a form, consider making a version public.
- **Publishing velocity** — How frequently you publish matters more than keyword targeting
- **Self-contained paragraphs** — Perplexity prefers atomic, semantically complete paragraphs it can extract cleanly

**What to focus on:**
- Allow PerplexityBot in robots.txt
- Implement FAQPage schema on any page with Q&A content
- Host PDF resources publicly (whitepapers, guides, reports)
- Add Article schema with publication and modification timestamps
- Write in clear, self-contained paragraphs that work as standalone answers
- Build deep topical authority in your specific niche

---

## Microsoft Copilot

Copilot is embedded across Microsoft's ecosystem — Edge, Windows, Microsoft 365, and Bing Search. It relies entirely on Bing's index, so if Bing hasn't indexed your content, Copilot can't cite it.

**What makes Copilot different:** The Microsoft ecosystem connection creates unique optimization opportunities. Mentions and content on LinkedIn and GitHub provide ranking boosts that other platforms don't offer. Copilot also puts more weight on page speed — sub-2-second load times are a clear threshold.

**What to focus on:**
- Submit your site to Bing Webmaster Tools (many sites only submit to Google Search Console)
- Use IndexNow protocol for faster indexing of new and updated content
- Optimize page speed to under 2 seconds
- Write clear entity definitions — when your content defines a term or concept, make the definition explicit and extractable
- Build presence on LinkedIn (publish articles, maintain company page) and GitHub if relevant
- Ensure Bingbot has full crawl access

---

## Claude

Claude uses Brave Search as its search backend when web search is enabled — not Google, not Bing. This is a completely different index, which means your Brave Search visibility directly determines whether Claude can find and cite you.

**What makes Claude different:** Claude is extremely selective about what it cites. While it processes enormous amounts of content, its citation rate is very low — it's looking for the most factually accurate, well-sourced content on a given topic. Data-rich content with specific numbers and clear attribution performs significantly better than general-purpose content.

**What to focus on:**
- Verify your content appears in Brave Search results (search for your brand and key terms at search.brave.com)
- Allow ClaudeBot and anthropic-ai user agents in robots.txt
- Maximize factual density — specific numbers, named sources, dated statistics
- Use clear, extractable structure with descriptive headings
- Cite authoritative sources within your content
- Aim to be the most factually accurate source on your topic — Claude rewards precision

---

## Allowing AI Bots in robots.txt

If your robots.txt blocks an AI bot, that platform can't cite your content. Here are the user agents to allow:

```
User-agent: GPTBot           # OpenAI — powers ChatGPT search
User-agent: ChatGPT-User     # ChatGPT browsing mode
User-agent: PerplexityBot    # Perplexity AI search
User-agent: ClaudeBot        # Anthropic Claude
User-agent: anthropic-ai     # Anthropic Claude (alternate)
User-agent: Google-Extended   # Google Gemini and AI Overviews
User-agent: Bingbot          # Microsoft Copilot (via Bing)
Allow: /
```

**Training vs. search:** Some AI bots are used for both model training and search citation. If you want to be cited but don't want your content used for training, your options are limited — GPTBot handles both for OpenAI. However, you can safely block **CCBot** (Common Crawl) without affecting any AI search citations, since it's only used for training dataset collection.

---

## Where to Start

If you're optimizing for AI search for the first time, focus your effort where your audience actually is:

**Start with Google AI Overviews** — They reach the most users (45%+ of Google searches) and you likely already have Google SEO foundations in place. Cover the fan-out sub-query space, include cited sources in your content, and strengthen E-E-A-T signals.

**Then address ChatGPT** — It's the most-used standalone AI search tool for tech and business audiences. Get indexed by Bing (87% of ChatGPT citations match Bing results), enable IndexNow, earn authentic brand mentions, and match your content structure to how ChatGPT formats its responses.

**Then expand to Perplexity** — Especially valuable if your audience includes researchers, early adopters, or tech professionals. Publish original data, keep content fresh, and write in clear, self-contained paragraphs.

**Copilot and Claude are lower priority** unless your audience skews enterprise/Microsoft (Copilot) or developer/analyst (Claude). But the fundamentals — structured content, cited sources, clean entity data — help across all platforms.

**Actions that help everywhere:**
1. Allow all AI bots in robots.txt
2. Implement schema markup for rich results and entity clarity (FAQPage, Article, Organization at minimum) — not as a citation lever; controlled testing shows no direct citation lift (Ahrefs, May 2026)
3. Include statistics with named sources in your content
4. Update content regularly — monthly for competitive topics
5. Use clear heading structure (H1 > H2 > H3)
6. Keep page load time under 2 seconds
7. Add author bios with credentials
8. Earn authentic branded web mentions — the strongest measured off-site signal (r=0.664; YouTube mentions r=0.737 — Ahrefs 75K brands, Jul 2026)
