# Financial Services For Codex

[中文](README.zh-CN.md)

This repository is a Codex-ready port of Anthropic's Apache-2.0
[`financial-services`](https://github.com/anthropics/financial-services) reference agents, plugins, skills,
commands, and MCP connector definitions.

## What Changed

- Claude plugin manifests were converted from `.claude-plugin/plugin.json` to
  `.codex-plugin/plugin.json`.
- Claude marketplace metadata was converted to `.agents/plugins/marketplace.json`.
- Claude slash commands were converted into `command-*` Codex skills.
- Claude named agent prompts were converted into `agent-*` Codex skills.
- Existing `SKILL.md` files were normalized to Codex-readable front matter.
- Claude Managed Agent cookbooks are preserved as reference material in
  `managed-agent-cookbooks/`, but Codex uses the plugin and skill layout.

## Install / Use In Codex

Clone this repository first:

```bash
git clone https://github.com/deshengli0523-stack/finacial-service-for-codex.git
cd finacial-service-for-codex
```

Install plugins by adding this repository as a local Codex plugin marketplace source.
The marketplace file is:

```text
.agents/plugins/marketplace.json
```

After the marketplace is added, install any plugin by name from the Plugin Catalog
below. Installing a plugin also makes its bundled skills available. Agent plugins
also include their `agent-*` orchestration skill.

Install an individual skill when you only want one workflow. Every skill lives at:

```text
plugins/<plugin-family>/<plugin-name>/skills/<skill-name>/
```

Copy that whole folder into your Codex skills directory. On macOS/Linux:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R plugins/vertical-plugins/financial-analysis/skills/comps-analysis "${CODEX_HOME:-$HOME/.codex}/skills/"
```

On Windows PowerShell:

```powershell
$SkillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex\skills' }
New-Item -ItemType Directory -Force $SkillRoot
Copy-Item -Recurse -Force plugins\vertical-plugins\financial-analysis\skills\comps-analysis $SkillRoot
```

Install agents either by installing the matching agent plugin, such as
`pitch-agent`, or by copying its `skills/agent-*` folder into the Codex skills
directory. Managed Agent `agent.yaml` files are retained for reference only;
Codex uses the converted `agent-*` skills.

This port contains 19 plugins, 10 agent skills, 174 total skills, and 47 converted command workflows.

## Plugin Catalog

| Plugin | Type | Function | Path |
| --- | --- | --- | --- |
| `earnings-reviewer` | Agent plugin | Earnings call and filings to model update to note draft | `plugins/agent-plugins/earnings-reviewer` |
| `gl-reconciler` | Agent plugin | Finds breaks, traces root cause, routes for sign-off | `plugins/agent-plugins/gl-reconciler` |
| `kyc-screener` | Agent plugin | Parses onboarding docs, runs the rules engine, flags gaps | `plugins/agent-plugins/kyc-screener` |
| `market-researcher` | Agent plugin | Sector or theme to industry overview, competitive landscape, peer comps, and ideas shortlist | `plugins/agent-plugins/market-researcher` |
| `meeting-prep-agent` | Agent plugin | Briefing pack before every client meeting | `plugins/agent-plugins/meeting-prep-agent` |
| `model-builder` | Agent plugin | DCF, LBO, 3-statement, comps - live in Excel | `plugins/agent-plugins/model-builder` |
| `month-end-closer` | Agent plugin | Accruals, roll-forwards, variance commentary | `plugins/agent-plugins/month-end-closer` |
| `pitch-agent` | Agent plugin | Comps, precedents, LBO to a branded pitch deck, end to end | `plugins/agent-plugins/pitch-agent` |
| `statement-auditor` | Agent plugin | Audits pre-generated LP statements before distribution | `plugins/agent-plugins/statement-auditor` |
| `valuation-reviewer` | Agent plugin | Ingests GP packages, runs valuation template, stages LP reporting | `plugins/agent-plugins/valuation-reviewer` |
| `lseg` | Partner plugin | Price bonds, analyze yield curves, evaluate FX carry trades, value options, and build macro dashboards using LSEG financial data and analytics. | `plugins/partner-built/lseg` |
| `sp-global` | Partner plugin | S&P Global - Financial data and analytics skills including company tearsheets, earnings previews, and transaction summaries | `plugins/partner-built/spglobal` |
| `equity-research` | Vertical plugin | Equity research tools: earnings analysis, initiating coverage reports, and research workflows | `plugins/vertical-plugins/equity-research` |
| `financial-analysis` | Vertical plugin | Core financial modeling and analysis tools: DCF, comps, LBO, 3-statement models, competitive analysis, and deck QC | `plugins/vertical-plugins/financial-analysis` |
| `fund-admin` | Vertical plugin | Fund administration and finance ops skills: GL reconciliation, break tracing, accruals, roll-forwards, variance commentary, NAV tie-out | `plugins/vertical-plugins/fund-admin` |
| `investment-banking` | Vertical plugin | Investment banking productivity tools: client and market insights, deck creation, financial analysis, and transaction management | `plugins/vertical-plugins/investment-banking` |
| `operations` | Vertical plugin | Operational workflows: KYC document parsing and rules-grid evaluation | `plugins/vertical-plugins/operations` |
| `private-equity` | Vertical plugin | Private equity deal sourcing and workflow tools: company discovery, CRM integration, and founder outreach | `plugins/vertical-plugins/private-equity` |
| `wealth-management` | Vertical plugin | Wealth management and financial advisory tools: client reviews, financial planning, portfolio analysis, and client reporting | `plugins/vertical-plugins/wealth-management` |

## Agent Installation And Catalog

Install the plugin listed in the `Plugin` column, or copy the `Skill path` folder
into your Codex skills directory for standalone use.

| Agent skill | Plugin | Function | Skill path |
| --- | --- | --- | --- |
| `agent-earnings-reviewer` | `earnings-reviewer` | Processes an earnings event end to end — reads the call transcript and filings, updates the coverage model, and drafts the post-earnings note. Use when a covered name reports; for a single name interactively, or fanned out across a coverage list as a managed agent. | `plugins/agent-plugins/earnings-reviewer/skills/agent-earnings-reviewer` |
| `agent-gl-reconciler` | `gl-reconciler` | Reconciles general ledger to subledger across asset classes for a trade date — finds breaks, traces root cause, and routes the exception report for sign-off. Use for daily or month-end recon runs; not for journal-entry posting (use month-end-closer for that). | `plugins/agent-plugins/gl-reconciler/skills/agent-gl-reconciler` |
| `agent-kyc-screener` | `kyc-screener` | Parses an onboarding document packet, runs the firm's KYC/AML rules engine, screens against sanctions and PEP lists, and flags gaps for escalation. Use for new-client onboarding or periodic refresh — not for transaction monitoring. | `plugins/agent-plugins/kyc-screener/skills/agent-kyc-screener` |
| `agent-market-researcher` | `market-researcher` | Produces sector or thematic market research — industry overview, competitive landscape, trading-comps spread of the peer set, and a thematic ideas shortlist — packaged as a research note with optional slides. Use when an analyst or PM asks for a primer on a sector or theme; not for single-name coverage updates (use earnings-reviewer for that). | `plugins/agent-plugins/market-researcher/skills/agent-market-researcher` |
| `agent-meeting-prep-agent` | `meeting-prep-agent` | Builds a briefing pack before a client or prospect meeting — relationship history from CRM, holdings and recent activity, market context, and a suggested agenda. Use ahead of any client meeting; pairs with a calendar event. | `plugins/agent-plugins/meeting-prep-agent/skills/agent-meeting-prep-agent` |
| `agent-model-builder` | `model-builder` | Builds DCF, LBO, three-statement, and trading-comps models live in Excel from a ticker and assumption set. Use when you need a clean model from scratch — not for updating an existing coverage model (use earnings-reviewer for that). | `plugins/agent-plugins/model-builder/skills/agent-model-builder` |
| `agent-month-end-closer` | `month-end-closer` | Runs the month-end close for an entity — accruals, roll-forwards, and variance commentary — and stages the close package for controller sign-off. Use for period-end close; not for daily reconciliation (use gl-reconciler for that). | `plugins/agent-plugins/month-end-closer/skills/agent-month-end-closer` |
| `agent-pitch-agent` | `pitch-agent` | End-to-end investment banking pitch agent. Given a target company and a strategic situation, such as "exploring strategic alternatives", autonomously pulls comps and precedents from market data, builds a DCF and football-field valuation in Excel, and generates a branded pitch deck on the bank's PowerPoint template. Use when an MD or senior banker asks for a first-draft pitch on a name; not for editing an existing deck. | `plugins/agent-plugins/pitch-agent/skills/agent-pitch-agent` |
| `agent-statement-auditor` | `statement-auditor` | Audits a batch of pre-generated LP capital-account statements against the fund NAV pack before distribution — ties out balances, allocations, and fees, and flags discrepancies. Use as the final check before statements go out. | `plugins/agent-plugins/statement-auditor/skills/agent-statement-auditor` |
| `agent-valuation-reviewer` | `valuation-reviewer` | Ingests GP valuation packages for a fund, runs them through the valuation template, and stages LP reporting. Use for quarter-end portfolio valuation review — not for deal-time underwriting (use model-builder for that). | `plugins/agent-plugins/valuation-reviewer/skills/agent-valuation-reviewer` |

## Command Catalog

Codex does not load Claude slash commands directly. Each command below is available
as a `command-*` skill. Ask Codex for the slash command behavior by name, or install
or copy the corresponding skill.

| Command | Plugin | Function | Codex skill |
| --- | --- | --- | --- |
| `/analyze-bond-basis` | `lseg` | Analyze the bond futures basis with CTD identification, implied repo rate, and basis trade assessment | `command-analyze-bond-basis` |
| `/analyze-bond-rv` | `lseg` | Analyze a bond's relative value vs yield curves and credit spreads with scenario stress testing | `command-analyze-bond-rv` |
| `/analyze-fx-carry` | `lseg` | Evaluate FX carry trade opportunities with spot, forwards, vol surface, and historical context | `command-analyze-fx-carry` |
| `/analyze-option-vol` | `lseg` | Analyze option volatility with vol surface, Greeks, and implied vs realized vol comparison | `command-analyze-option-vol` |
| `/analyze-swap-curve` | `lseg` | Analyze the swap curve with government and inflation overlays to identify curve trade opportunities | `command-analyze-swap-curve` |
| `/macro-rates` | `lseg` | Build a macro and rates dashboard with economic indicators, yield curves, inflation, and swap spreads | `command-macro-rates` |
| `/research-equity` | `lseg` | Generate a comprehensive equity research snapshot with consensus estimates, fundamentals, and price performance | `command-research-equity` |
| `/review-fi-portfolio` | `lseg` | Review a fixed income portfolio with pricing, reference data, cashflows, and scenario analysis | `command-review-fi-portfolio` |
| `/catalysts` | `equity-research` | View or update the catalyst calendar | `command-catalysts` |
| `/earnings-preview` | `equity-research` | Build a pre-earnings preview with scenarios | `command-earnings-preview` |
| `/earnings` | `equity-research` | Analyze quarterly earnings and create an earnings update report | `command-earnings` |
| `/initiate` | `equity-research` | Create an initiating coverage report | `command-initiate` |
| `/model-update` | `equity-research` | Update a financial model with new data | `command-model-update` |
| `/morning-note` | `equity-research` | Draft a morning meeting note | `command-morning-note` |
| `/screen` | `equity-research` | Run a stock screen or generate investment ideas | `command-screen` |
| `/sector` | `equity-research` | Create a sector overview report | `command-sector` |
| `/thesis` | `equity-research` | Create or update an investment thesis | `command-thesis` |
| `/3-statement-model` | `financial-analysis` | Fill out a 3-statement financial model template | `command-3-statement-model` |
| `/competitive-analysis` | `financial-analysis` | Create a competitive landscape analysis | `command-competitive-analysis` |
| `/comps` | `financial-analysis` | Build a comparable company analysis with trading multiples | `command-comps` |
| `/dcf` | `financial-analysis` | Build a DCF valuation model with comps-informed terminal multiples | `command-dcf` |
| `/debug-model` | `financial-analysis` | Debug and audit a financial model for errors | `command-debug-model` |
| `/lbo` | `financial-analysis` | Build an LBO model for a PE acquisition | `command-lbo` |
| `/ppt-template` | `financial-analysis` | Create a reusable PPT template skill from a PowerPoint template file | `command-ppt-template` |
| `/buyer-list` | `investment-banking` | Build a buyer universe for a sell-side process | `command-buyer-list` |
| `/cim` | `investment-banking` | Draft a Confidential Information Memorandum | `command-cim` |
| `/deal-tracker` | `investment-banking` | Track and review live deal pipeline | `command-deal-tracker` |
| `/merger-model` | `investment-banking` | Build an accretion/dilution merger model | `command-merger-model` |
| `/one-pager` | `investment-banking` | Create a one-page company strip profile using branded PPT template | `command-one-pager` |
| `/process-letter` | `investment-banking` | Draft a process letter or bid instructions | `command-process-letter` |
| `/teaser` | `investment-banking` | Draft an anonymous one-page teaser | `command-teaser` |
| `/ai-readiness` | `private-equity` | Scan the portfolio for the highest-leverage AI opportunities | `command-ai-readiness` |
| `/dd-checklist` | `private-equity` | Generate a due diligence checklist | `command-dd-checklist` |
| `/dd-prep` | `private-equity` | Prep for a diligence meeting or expert call | `command-dd-prep` |
| `/ic-memo` | `private-equity` | Draft an investment committee memo | `command-ic-memo` |
| `/portfolio` | `private-equity` | Review portfolio company performance | `command-portfolio` |
| `/returns` | `private-equity` | Build IRR/MOIC sensitivity tables | `command-returns` |
| `/screen-deal` | `private-equity` | Screen an inbound deal (CIM or teaser) | `command-screen-deal` |
| `/source` | `private-equity` | Source deals — discover companies and draft founder outreach | `command-source` |
| `/unit-economics` | `private-equity` | Analyze unit economics (ARR cohorts, LTV/CAC, retention) | `command-unit-economics` |
| `/value-creation` | `private-equity` | Build a post-acquisition value creation plan | `command-value-creation` |
| `/client-report` | `wealth-management` | Generate a client performance report | `command-client-report` |
| `/client-review` | `wealth-management` | Prep for a client review meeting | `command-client-review` |
| `/financial-plan` | `wealth-management` | Build or update a financial plan | `command-financial-plan` |
| `/proposal` | `wealth-management` | Create an investment proposal for a prospect | `command-proposal` |
| `/rebalance` | `wealth-management` | Analyze drift and generate rebalancing trades | `command-rebalance` |
| `/tlh` | `wealth-management` | Identify tax-loss harvesting opportunities | `command-tlh` |

## MCP Connectors

MCP connectors are preserved where the original repo provided `.mcp.json` files.
Most financial data connectors require separate provider subscriptions,
credentials, and network access.

## Safety

These workflows draft analyst work product for qualified human review. They do not
provide investment, legal, tax, or accounting advice, and they must not execute
transactions, approve onboarding, post to ledgers, or bind risk without your own
controls.

## Provenance

- Upstream: https://github.com/anthropics/financial-services
- Codex port repository: https://github.com/deshengli0523-stack/finacial-service-for-codex
- License: Apache-2.0; see `LICENSE`.
