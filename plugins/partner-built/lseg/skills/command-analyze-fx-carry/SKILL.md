---
name: command-analyze-fx-carry
description: "Evaluate FX carry trade opportunities with spot, forwards, vol surface, and historical context"
---

# /analyze-fx-carry Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `<currency pair e.g. USDJPY> [tenor e.g. 3M]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

# Analyze FX Carry Trade

> This command uses LSEG FX pricing, forward curves, volatility surfaces, and historical data tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Evaluate carry trade opportunities for a currency pair by combining spot rates, forward points, the carry term structure, volatility risk, and historical price context.

See the **fx-carry-trade** skill for domain knowledge on carry frameworks and risk metrics.

## Workflow

### 1. Gather Input

Ask the user for:
- Currency pair (required) — e.g., USDJPY, EURUSD, AUDUSD
- Target tenor (optional, default 3M)
- Valuation date (optional, defaults to today)

### 2. Get the Spot Rate

Call `fx_spot_price` with the currency pair.

Extract: mid/bid/ask rates, bid-ask spread.

### 3. Price the Forward at Target Tenor

Call `fx_forward_price` with the pair and target tenor.

Extract: forward rate, forward points. Compute annualized carry.

### 4. Map the Full Carry Curve

Call `fx_forward_curve` (list then calculate) for the pair.

Present carry profile across tenors (ON through 1Y): forward points, annualized carry, cumulative carry. Identify the sweet-spot tenor.

### 5. Assess Volatility Risk

Call `fx_vol_surface` for the pair.

Extract: ATM vol at target tenor, 25-delta risk reversal, 25-delta butterfly.

Compute carry-to-vol ratio = annualized carry / ATM implied vol.

### 6. Historical Spot Context

Call `tscc_historical_pricing_summaries` for the pair's RIC with `interval: "P1D"`, `tenor: "1Y"`.

Assess: 52-week range, current position in range, trend direction.

### 7. Synthesize the Report

Present: carry-to-vol ratio and overall assessment, spot & forward pricing, carry term structure table, vol surface snapshot, historical context.

## Output Format

Lead with the carry-to-vol ratio and overall assessment (attractive / moderate / unattractive). Follow with detailed supporting data in tables.
