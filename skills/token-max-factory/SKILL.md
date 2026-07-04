---
name: token-max-factory
description: Point-and-shoot programmatic SEO/GEO page factory — scan ANY website, then expand it into hundreds of validated token-max pages (2,800-3,400 words, 90%+ unique, GEO answer-first) via a universal Archon workflow. Use when the user says "token max", "site factory", "point and shoot", "expand this site", "generate city pages", "scan and expand", "programmatic pages for a site", "onboard a site to the factory", or "run the factory". Covers onboarding new sites, running and resuming batches, the Archon 0.5.0 gotchas, and verification. Requires the free Archon CLI (>= 0.5.0) and the token-max-site-factory engine repo.
---

# token-max-factory — Universal Point-and-Shoot Content Factory

Drives the [token-max-site-factory](https://github.com/TheSmokeDev/token-max-site-factory)
engine through [Archon](https://archon.diy). Most programmatic SEO fails as
thin duplicate content or hallucinated local "facts" — this factory attacks
both with hard validation gates and a packet system where the packet is the
ONLY fact source.

**Hard boundary (never violate):** the factory NEVER deploys, touches DNS,
Search Console, sitemaps, or indexing. Generation ends at a clean validation
report in the target repo's worktree. Shipping is a separate human-approved
lane. A preflight node re-verifies this contract on every run.

## Prerequisites (one-time)

```bash
# Archon CLI (free, MIT) — macOS/Linux:
curl -fsSL https://archon.diy/install | bash
# Windows PowerShell:  irm https://archon.diy/install.ps1 | iex

# The engine (free, MIT):
git clone https://github.com/TheSmokeDev/token-max-site-factory
# or, via the Archon marketplace:  archon workflow install token-max-site-factory
```

The writer runs on YOUR coding-agent subscription: codex at `xhigh` reasoning
by default; claude via explicit `install --allow-claude`. No SEO APIs, no
paid data vendors.

## Quality contract (defaults, per page)

2,800-3,400 words (hard fail <2,700) · pairwise + cross-corpus shingle/Jaccard
overlap ≤0.10 · ≥8 H2 · ≥4 AI-citable blockquotes · ≥5 FAQ questions ·
text-to-HTML ≥0.15 · unique title/meta · packet = only fact source ·
vertical prohibited-claim regexes.

## Point-and-shoot: onboard a new site

```bash
cd token-max-site-factory

python engine/token_max_site_factory.py new-site --site <id> --target-repo <path>   # 1. scaffold config
python engine/token_max_site_factory.py scan --site <id> --allow-network            # 2. scan live site + local repo (the ONLY network step, manual)
# 3. edit sites/<id>/site.yaml — start from sites/example/site.yaml; see references/site-config.md
python engine/token_max_site_factory.py install --site <id> --run-input "pilot-10"  # 4. stamp workflow shim + marker into target repo
cd <target-repo> && archon workflow run token-max-site-factory-<id> --no-worktree   # 5. run
```

Pilot (10-25 pages) BEFORE any tranche. Tranches ≤300 pages (pairwise overlap
is O(n²)). Review the worktree diff + report, merge, deploy through the
site's own lane.

## Running on Archon 0.5.0 — CRITICAL gotchas

1. **Run input is BAKED at install time** (`install --run-input "..."`).
   0.5.0 bash nodes do NOT receive the user message (regression; fixed on
   Archon's dev branch). To change what a run does, re-run `install` with a
   new `--run-input`. Input grammar: `pilot-10`, `<phase>`,
   `<phase>-tranche-300`, `--topics a,b --entities x,y --limit 20`,
   `--dry-run`.
2. **Never put dollar-sign shell variables in workflow YAML** — 0.5.0 blanks
   EVERY dollar token in inline node scripts. On-disk scripts
   (`engine/tmsf.sh`) are safe. The template is already dollar-free; keep it
   that way.
3. **Archon's bash may be WSL bash** — the template's if/else picks the
   Windows vs `/mnt/c/...` path form automatically.
4. **Prefer `--detach` for long runs**: `archon workflow run <name>
   --no-worktree --detach` — survives the launching shell. Track via the
   batch ledger, not the console.
5. **Stale "running" rows block relaunch** ("Workflow already active on this
   path"). Fix: `archon workflow status` → `archon workflow abandon <run-id>`
   (DB-only; safe when the process is dead).
6. **`until_bash` exit-1 "error" log lines during loops are normal** — that's
   the "not done yet" signal; the loop is fine.

## Resume & recovery (state is on disk, always resume-safe)

- **Resume anything:** re-run the same `archon workflow run` command.
  `prepare --resume --resume-existing-outputs` folds in every page already on
  disk. Never delete `<artifacts>/state/batch.json`.
- **Run died after generation finished?** Finish deterministically, no Archon:
  ```bash
  cd <target-repo>
  python <factory>/engine/token_max_site_factory.py validate --site <id>   # hard gate
  python <factory>/engine/token_max_site_factory.py emit --site <id>       # html sites; noop for markdown
  python <factory>/engine/token_max_site_factory.py report --site <id>
  ```
- Ledger check: `remaining --site <id>` or read `<artifacts>/state/batch.json`
  statuses (`pending_generation → generated/regenerated/held_back`).

## Verification checklist (after every batch)

1. `<artifacts>/reports/validation.json` → `ok: true`, 0 held back, 0 overlaps.
2. `<artifacts>/reports/batch-report.md` — word counts in band, "Live
   mutations: none".
3. HTML sites: spot-open an emitted page; confirm canonical + FAQPage JSON-LD;
   if the site has its own head-baking tooling, prove it changes NOTHING on
   factory pages (emitted heads carry rel=canonical → skipped).
4. Confirm pre-existing content lanes untouched (`git status` on the live tree).

## Prompt profiles

`regulated-insurance` (compliance-heavy verticals; California insurance rules
as the worked example) and `local-service-seo` (non-regulated local service).
New vertical = new profile in `prompts/profiles/` + site `claim_rules_md`.

No images are generated anywhere — text-forward by design (GEO extraction
favors extractable text).

## References

- `references/site-config.md` — the full site.yaml schema, annotated
- Engine `README.md` — runbook + troubleshooting
- Engine `WORKFLOW.md` — the Archon marketplace package doc
