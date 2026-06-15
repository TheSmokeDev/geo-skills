# Install

These are Agent Skills. Installing them means placing the skill folders where your agent looks for skills. Pick the section for your runtime.

```bash
git clone https://github.com/SmokeAlot420/geo-skills.git
cd geo-skills
```

### Claude Code

```bash
cp -r skills/* ~/.claude/skills/      # the skills
cp -r agents/* ~/.claude/agents/      # the orchestrator's subagents
```

PowerShell:

```powershell
Copy-Item -Recurse skills\* $HOME\.claude\skills\
Copy-Item -Recurse agents\* $HOME\.claude\agents\
```

### Codex

```bash
cp -r skills/* ~/.codex/skills/
```

### Other agents

Copy `skills/*` into whatever directory your agent loads skill / instruction files from. The skills are plain `SKILL.md` docs, so any agent that reads them can run the individual skills. The parallel-subagent fan-out in the `geo` orchestrator is Claude Code-specific; on other agents, invoke the skills directly (e.g. `geo-citability`, `geo-crawlers`, `geo-schema`).

Restart or reload your agent so it picks up the new skills.

## Use it

```
/geo audit https://yoursite.com
```

That runs the full audit and returns your GEO Score plus a prioritized fix list. Other entry points:

```
/geo page https://yoursite.com/specific-page
/geo llmstxt https://yoursite.com
/geo-audit https://yoursite.com
```

You can also call individual skills directly, e.g. `geo-citability`, `geo-crawlers`, `geo-schema`.

## Optional dependencies

The core audit needs nothing beyond Claude Code. A couple of skills use optional Python packages only if you invoke them:

- `geo-report-pdf` (PDF reports) - needs `reportlab`
- `geo-prospect` / the CRM dashboard in `geo` - needs `flask`

Install them only if you use those features:

```bash
pip install reportlab flask
```

No SEO API keys are required for any skill. Third-party data tools (rank trackers, backlink suites) are always optional and the skills degrade gracefully without them.
