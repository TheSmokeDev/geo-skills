---
name: geoskills-cli
description: Agent-native command surface for discovering, inspecting, and validating the geo-skills toolkit. Use when an operator or coding agent needs to run geoskills doctor, enumerate bundled skills or prompts, validate the full repository contract, validate an owner-intent handoff for TokenMax, or run the deterministic read-only page inspector and citability scorer.
---

# GEO Skills CLI

Use the installed `geoskills` command before reaching into bundled scripts directly.

## Start

```bash
geoskills --json doctor
geoskills --json validate
geoskills skills list --json
geoskills prompts list --json
```

Use `--json` for agent consumption. Omit it for human-readable output.

## Commands

- `geoskills skills show <name>`: print one canonical `SKILL.md`.
- `geoskills prompts show <name>`: print one paste-ready prompt.
- `geoskills owner-map validate <file> --json`: fail closed on an invalid GEO-to-TokenMax handoff.
- `geoskills inspect <url> --mode page|robots|llms|sitemap|blocks|full --json`: run the deterministic read-only web inspector. Install the `web` extra first.
- `geoskills citability <url> --json`: score extracted page passages. Install the `web` extra first.

## Rules

- Inspect before proposing changes.
- Preserve the distinction between observed data, calculated values, inference, and proposed action.
- Treat `doctor`, `validate`, discovery, owner-map validation, inspection, and citability as local/read-only commands.
- Do not represent a deterministic inspection as a full LLM audit.
- Do not deploy, publish, submit URLs, post to communities, mutate provider settings, or spend against a connected API from this skill.
- On nonzero exit, read the JSON error or stderr and repair the contract rather than bypassing the gate.
