# DataForSEO Intelligence Prompt Pack

Seven paste-ready prompts for turning live SEO and AI-search data into decisions an
operator can verify. The source pack was operator-provided and has been rewritten to
be model-neutral, pagination-aware, evidence-first, and safe to publish.

## Requirements

- An MCP-capable agent.
- An active DataForSEO account connected through the
  [official DataForSEO MCP server](https://dataforseo.com/help-center/setting-up-the-official-dataforseo-mcp-server-simple-guide).
- Approval for the paid API calls the prompt will make.

The current official MCP exposes documentation discovery plus an authenticated API
request tool. The prompts therefore tell the agent to inspect the live docs before
choosing endpoints instead of depending on a frozen list of legacy tool names.

## Prompts

| Prompt | Decision it produces |
|---|---|
| [`01-site-explorer.md`](01-site-explorer.md) | Which existing pages have the strongest evidence-backed upside? |
| [`02-keyword-research.md`](02-keyword-research.md) | Which query clusters deserve one owner page, and in what order? |
| [`03-content-gap.md`](03-content-gap.md) | Which competitor gaps are real, relevant, and beatable? |
| [`04-technical-audit.md`](04-technical-audit.md) | Which verified defects block discovery, rendering, or conversion? |
| [`05-ai-visibility.md`](05-ai-visibility.md) | Where is the brand mentioned or cited across a fixed AI prompt panel? |
| [`06-community-demand.md`](06-community-demand.md) | What do public community discussions reveal, without manufacturing consensus? |
| [`07-owner-intent-map.md`](07-owner-intent-map.md) | Upgrade, create, consolidate, or hold before TokenMax generation. |

Replace every `{{PLACEHOLDER}}`, paste one prompt into the connected agent, and
approve only the calls that fit your budget. Start with `07-owner-intent-map.md`
before any programmatic page batch.

## Evidence states

Every report must keep these states separate:

- `OBSERVED`: returned by an API or read from a named public URL.
- `CALCULATED`: derived from observed values with the formula shown.
- `INFERRED`: analyst judgment with confidence and counterevidence.
- `PROPOSED`: a recommendation that has not been implemented.
- `DEPLOYED`, `INDEXED`, `RANKING`, `CITED`: allowed only with direct evidence for
  that exact state.

The prompts never deploy, publish, post to a community, submit URLs, or change a
provider account. They write local reports and handoffs only.

## Shared report contract

[`00-report-contract.md`](00-report-contract.md) is the canonical design and evidence
contract for extending this pack. Each shipped prompt repeats the critical rules so it
remains paste-ready on its own.

[`EXAMPLES.md`](EXAMPLES.md) shows a filled input and the expected decision artifact
for every prompt without inventing example API results.
