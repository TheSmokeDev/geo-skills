# site.yaml — full annotated schema

One file per target site at `<factory>/sites/<site_id>/site.yaml`. Unknown
top-level keys are REJECTED (typo protection). `bootstrap` snapshots the
resolved config into the run's artifacts dir, so in-flight runs are immune to
edits. Start from `sites/example/site.yaml` in the engine repo.

```yaml
site_id: mysite                      # must match the directory name
domain: mysite.com
canonical_host: https://www.mysite.com
target_repo_root: /path/to/mysite-repo   # used by install + scan only; runs use cwd

# --- output ---
page_format: markdown                # markdown | html | nextjs_content
output_template: "content/{entity}/{topic_file_key}.md"    # repo-relative; html sites: final .html path
route_template: "/{entity}/{topic_route_segment}"          # extensionless if the host uses cleanUrls
staging_template: ""                 # html/nextjs sites ONLY: where the writer's markdown goes
html_template: ""                    # html sites ONLY: repo-relative template with slots
                                     #   {{TITLE}} {{META_DESCRIPTION}} {{CANONICAL}} {{JSONLD}} {{BODY_HTML}} {{LANG}}
build_verify_command: ""             # optional post-emit check run by the emit node
locales: [en]                        # v1 generates en only
batch_kind: mysite-token-max         # ledger identity; keep stable across runs

provider: codex                      # claude requires install --allow-claude
model_reasoning_effort: xhigh
artifacts_dir: .token-max-artifacts/mysite/pilot   # repo-relative, inside the worktree

inventory:
  entities:                          # WHO the pages are about (cities, locations, products...)
    adapter: static_list             # static_list (csv/json: name,slug + free columns) | ts_array (TS export regex)
    path: sites/mysite/facts/entities.csv   # sites/... = factory-relative; else target-repo-relative
  topics:                            # WHAT each page covers — topics × entities = the page matrix
    - key: my-service
      aliases: [service]             # accepted in run inputs
      file_key: my-service           # filename slot
      route_segment: my-service      # URL slot
      label: my service              # prose label
      title_label: My Service        # Title Case slot
      intent: who this page serves and why
      primary_decision: the one decision the page enables
      must_answer: [q1, q2, q3]      # goes into the writer packet
  pilot_entities: [slug-a, slug-b]   # ordered first; rest sort by population desc, then name
  sitemap_url: ""                    # scan override; default <canonical_host>/sitemap.xml
  crawl: { max_pages: 200, delay_seconds: 1.0, timeout_seconds: 15 }
  facts_files: []                    # extra source-facts csv/json (listed in page sources)

phases:                              # named presets — these are the run-input vocabulary
  pilot:       { topics: "my-service", entities: pilot, limit: 10 }
  core:        { aliases: [phase2], topics: "my-service,other", entities: all, limit: 500 }
  # run inputs: "pilot", "pilot-25", "core", "core-tranche-300", "--dry-run", "--limit N",
  #             "--topics a,b", "--entities x,y", "all-entities"
default_phase: pilot                 # what a bare/empty run input does

frontmatter:                         # .format() slots: {entity_<field>}, {topic_label},
  title_template: "{topic_title_label} in {entity_name}"        # {topic_title_label}, {domain}...
  description_template: "{entity_name} {topic_label} guide."
  published: ""                      # empty = blank in frontmatter
  updated: ""

prompt_profile: local-service-seo    # prompts/profiles/<name>.md (regulated-insurance | local-service-seo | ...)
claim_rules_md: |                    # site-specific rules appended to the materialized writer prompt
  - Never invent prices, statistics, office locations, or local events.

authority_sources:                   # cited official sources handed to the writer
  - { label: "...", url: "https://...", use: "what it's for" }

quality:                             # ALL default to the proven production values — override sparingly
  target_words_min: 2800
  target_words_max: 3400
  hard_min_words: 2700
  min_h2: 8
  min_faq_questions: 5
  min_ai_citable_passages: 4
  min_text_html_ratio: 0.15
  max_pairwise_overlap: 0.10
  max_cross_overlap: 0.10
  shingle_size: 9
  max_retries: 3

prohibited_patterns:                 # vertical regexes (compiled re.I|re.S); base set
  my_banned_claim: 'guarantee[ds]?\s+(outcome|result)'   # (em_dash/guarantee/template_admission) always on

utility_section_patterns:            # stripped before overlap scoring (sources/related sections)
  - '##\s+Sources[\s\S]*?(?=\n## |\Z)'

cross_corpus_roots: [content, other/corpus]   # anti-rhyme corpora; .html files are tag-stripped
cross_corpus_glob: "**/*.md"

writer_contract:                     # prose musts injected into every packet
  must_include: [...]
  must_not_include: [...]

comparison_corpus: {}                # informational paths shown to the writer

live_mutation:                       # preflight asserts ALL false — do not touch
  allow_deploy: false
  allow_dns: false
  allow_gsc: false
  allow_indexing: false
```

## Batch ledger vocabulary (state/batch.json)

Page fields keep the original production lane's names for parity: `city` =
entity slug, `product` = topic key. Statuses: `pending_generation → generated
/ regenerated / held_back`. `held_back` pages carry `validation_failures[]` +
a `regenerate_with` hint and re-enter the writer loop until clean or
`max_retries` exhausted.

## Engine CLI (all take --site <id>; batch/output paths default from artifacts_dir)

`new-site` `scan [--allow-network]` `install [--run-input ...] [--allow-claude]`
`bootstrap --input "..."` `preflight` `prepare` `prepare-from-input`
`next-page` `packet --page-id X` `remaining [--exit-zero-when-done]`
`pending-ids` `mark-generated --page-id X [--status regenerated]`
`validate [--mark-held-back --no-fail] [--min-* overrides]` `validation-ok`
`emit` `report` `scan-local-content`
