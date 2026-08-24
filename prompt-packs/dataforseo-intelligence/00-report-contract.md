# Shared report contract

Use this contract when adding a prompt to the pack.

## API and evidence rules

1. Inspect the live DataForSEO documentation through the connected MCP before making
   calls. Use current endpoints and fields; do not guess a legacy tool name.
2. Respect the prompt's task and row caps. Ask before exceeding either. Never hide a
   truncated response, failed task, unsupported market, or unavailable engine.
3. Preserve raw returned values. Label every statement `OBSERVED`, `CALCULATED`,
   `INFERRED`, or `PROPOSED`. Show formulas for calculated values.
4. Never upgrade a recommendation to deployed, indexed, ranking, or cited without
   direct proof of that state.
5. Record endpoint path, task status, requested rows, returned rows, pagination,
   location/language, collection time, and API-reported cost when available.
6. Make no external mutation. Do not publish, deploy, post, vote, submit URLs, or
   change provider settings.

## HTML report rules

- Write one self-contained HTML file at the requested output path. If file writes are
  unavailable, return only the complete HTML document.
- Put all CSS in a `<style>` block. Use no CDN, remote font, tracking script, or
  externally fetched image.
- Use a dark neutral surface, one warm accent, readable 16px body text, keyboard-safe
  links, semantic headings, and text labels in addition to color.
- Lead with 3-5 decision metrics, then the evidence, then "The 3 things I would do
  first."
- End with "Data sources and coverage": endpoints, URLs inspected, row/task counts,
  date, cost when returned, missing data, confidence limits, and what the report does
  not prove.
- Cap visible tables at 25 rows and state the full returned count. Do not hide material
  exceptions in an appendix.
