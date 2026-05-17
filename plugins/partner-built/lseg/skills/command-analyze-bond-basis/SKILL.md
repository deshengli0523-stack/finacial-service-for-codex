---
name: command-analyze-bond-basis
description: "Analyze the bond futures basis with CTD identification, implied repo rate, and basis trade assessment"
---

# /analyze-bond-basis Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `<bond future RIC e.g. FGBLc1>`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

# Analyze Bond Futures Basis

> This command uses LSEG bond future pricing, bond pricing, yield curves, and historical data tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Analyze the bond futures basis by pricing the future, identifying the cheapest-to-deliver bond, computing gross and net basis, and assessing basis trade opportunities.

See the **bond-futures-basis** skill for domain knowledge on basis mechanics and trading strategies.

## Workflow

### 1. Gather Input

Ask the user for:
- Bond future RIC (required) — e.g., FGBLc1 (Euro Bund), TYc1 (US 10Y Note), FFIc1 (UK Gilt)
- Market data date (optional, defaults to today)

### 2. Price the Bond Future

Call `bond_future_price` with the future RIC.

Extract: fair price, CTD bond identifier, delivery basket with conversion factors, contract DV01, delivery dates.

### 3. Price the CTD Bond

Call `bond_price` for the CTD identifier from Step 2.

Extract: clean/dirty price, yield, duration, DV01, accrued interest, coupon.

Compute: gross basis, invoice price, carry, net basis.

### 4. Compute Implied Repo Rate

Call `interest_rate_curve` (list then calculate) for the future's currency. Use short-end rate as repo proxy.

Compute implied repo rate and compare to market repo.

### 5. Track Historical Basis

Call `tscc_historical_pricing_summaries` for both the future and CTD bond with `tenor: "3M"`, `interval: "P1D"`.

Assess: basis trend, volatility, and historical range.

### 6. Sovereign Credit Context

Call `credit_curve` for the relevant sovereign (e.g., "DE" for Bund, "US" for Treasury).

### 7. Synthesize the Report

Present: future summary table, CTD bond analytics, basis calculation table (gross/net basis, implied repo vs market repo), historical context, and trade recommendation (long basis / short basis / neutral).

## Output Format

Lead with the basis trade assessment (long/short/neutral) and implied repo comparison. Follow with detailed analytics tables.
