# A11yRatchet — WCAG 2.2 AA & EN 301 549 CI Baseline Ratchet for `axe-core`

![A11yRatchet & SpecGate Edge Platform](https://specgate.profalexandrezamboni.workers.dev/og-card.png)

[![GitHub Marketplace](https://img.shields.io/badge/GitHub%20Marketplace-A11yRatchet%20Action-7c3aed?logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/a11yratchet-wcag-2-2-aa-en-301-549-ci-regression-gate)
[![Glama MCP Connector](https://glama.ai/mcp/connectors/dev.workers.profalexandrezamboni.specgate/spec-gate/badges/score.svg)](https://glama.ai/mcp/connectors/dev.workers.profalexandrezamboni.specgate/spec-gate)
[![A11yRatchet Edge Gate](https://img.shields.io/badge/Live_Gate-A11yRatchet_Edge-purple)](https://specgate.profalexandrezamboni.workers.dev/tools/wcag-2-2-en-301-549-ci-gate?utm_source=github_repo)

**A11yRatchet** freezes legacy accessibility debt in brownfield web apps using a monotonic per-rule baseline ratchet while blocking net-new `axe-core` regressions mapped deterministically to **WCAG 2.2 AA** and **European Accessibility Act (`EN 301 549 V3.2.1` Chapter 9)** clauses.

- **Zero-Click Live WCAG 2.2 & EN 301 549 Demo (Runs Instantly):** https://specgate.profalexandrezamboni.workers.dev/?demo=a11yratchet&utm_source=github_repo
- **Official GitHub Marketplace Action (`v1.2.0`):** https://github.com/marketplace/actions/a11yratchet-wcag-2-2-aa-en-301-549-ci-regression-gate
- **Free Zero-Login Remote MCP Server (`/mcp`) for Cursor, Claude Code & VS Code:** https://specgate.profalexandrezamboni.workers.dev/integrations/mcp-server-cursor-claude-code?utm_source=github_repo
- **Next.js App Router + Playwright + `@axe-core/playwright` CI Gate:** https://specgate.profalexandrezamboni.workers.dev/integrations/nextjs-playwright-axe-wcag-ci-gate?utm_source=github_repo
- **Native OASIS SARIF v2.1.0 Export for GitHub Code Scanning:** https://specgate.profalexandrezamboni.workers.dev/integrations/github-code-scanning-sarif-ci-gate?utm_source=github_repo
- **Interactive WCAG 2.2 & EN 301 549 Evaluator:** https://specgate.profalexandrezamboni.workers.dev/tools/wcag-2-2-en-301-549-ci-gate?utm_source=github_repo
- **Comparison: A11yRatchet vs. axe-linter vs. pa11y-ci:** https://specgate.profalexandrezamboni.workers.dev/compare/a11yratchet-vs-axe-linter-vs-pa11y-ci?utm_source=github_repo
- **Full Technical Reference (`llms-full.txt`):** https://specgate.profalexandrezamboni.workers.dev/llms-full.txt

## Direct Engineering Comparison

| Capability | `axe-linter` | `pa11y-ci` | **A11yRatchet** |
| :--- | :--- | :--- | :--- |
| **Rendered CSS Contrast & Target Size** | No (static AST) | Yes | **Yes (ingests rendered `axe-core` JSON)** |
| **Legacy Adoption** | Changed lines | Coarse global `--threshold` | **Zero-noise per-rule monotonic ratchet** |
| **EN 301 549 `9.x.y.z` Clause Table** | WCAG tags | WCAG codes | **Native WCAG 2.2 AA + EN 301 549 Mapper** |

> *Compliance Scope Note:* Automated DOM checks detect ~30–40% of WCAG 2.2 / EN 301 549 criteria and complement manual assistive-technology testing.
