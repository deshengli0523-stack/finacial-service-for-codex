# Financial Services For Codex

[English](README.md)

本仓库是 Anthropic Apache-2.0 许可的
[`financial-services`](https://github.com/anthropics/financial-services) 参考仓库的 Codex 可用移植版，包含面向金融服务工作流的 agents、plugins、skills、commands 以及 MCP connector 定义。

## 主要变更

- 将 Claude 插件清单从 `.claude-plugin/plugin.json` 转换为 `.codex-plugin/plugin.json`。
- 将 Claude marketplace 元数据转换为 `.agents/plugins/marketplace.json`。
- 将 Claude slash commands 转换为 `command-*` Codex skills。
- 将 Claude named agent prompts 转换为 `agent-*` Codex skills。
- 将现有 `SKILL.md` 文件规范化为 Codex 可读取的 front matter。
- 保留 Claude Managed Agent cookbooks 作为参考资料，路径为 `managed-agent-cookbooks/`；Codex 运行时使用 plugin 和 skill 布局。

## 在 Codex 中安装 / 使用

先克隆本仓库：

```bash
git clone https://github.com/deshengli0523-stack/finacial-service-for-codex.git
cd finacial-service-for-codex
```

安装 plugins 时，将本仓库添加为 Codex 的本地 plugin marketplace 来源。marketplace 文件位于：

```text
.agents/plugins/marketplace.json
```

添加 marketplace 后，可以按下方 Plugin Catalog 中的名称安装任意 plugin。安装 plugin 会同时启用该 plugin bundled skills。Agent plugins 还会包含对应的 `agent-*` orchestration skill。

如果只需要单个 workflow，可以单独安装 skill。所有 skill 都位于以下路径格式：

```text
plugins/<plugin-family>/<plugin-name>/skills/<skill-name>/
```

将整个 skill 文件夹复制到 Codex skills 目录即可。macOS/Linux 示例：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R plugins/vertical-plugins/financial-analysis/skills/comps-analysis "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Windows PowerShell 示例：

```powershell
$SkillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex\skills' }
New-Item -ItemType Directory -Force $SkillRoot
Copy-Item -Recurse -Force plugins\vertical-plugins\financial-analysis\skills\comps-analysis $SkillRoot
```

安装 agents 时，可以安装对应的 agent plugin，例如 `pitch-agent`，也可以只复制该 plugin 下的 `skills/agent-*` 文件夹到 Codex skills 目录。Managed Agent `agent.yaml` 文件仅作为参考保留；Codex 使用转换后的 `agent-*` skills。

本移植版包含 19 个 plugins、10 个 agent skills、174 个 total skills，以及 47 个已转换 command workflows。

## Plugin Catalog

| Plugin | 类型 | 功能 | 路径 |
| --- | --- | --- | --- |
| `earnings-reviewer` | Agent 插件 | 将 earnings call 和 filings 转换为模型更新与研究笔记草稿。 | `plugins/agent-plugins/earnings-reviewer` |
| `gl-reconciler` | Agent 插件 | 查找总账与子账差异，追踪根因，并准备复核材料。 | `plugins/agent-plugins/gl-reconciler` |
| `kyc-screener` | Agent 插件 | 解析 onboarding 文档，运行 KYC 规则，并标记缺口。 | `plugins/agent-plugins/kyc-screener` |
| `market-researcher` | Agent 插件 | 从行业或主题生成行业概览、竞争格局、peer comps 和想法清单。 | `plugins/agent-plugins/market-researcher` |
| `meeting-prep-agent` | Agent 插件 | 在客户会议前生成 briefing pack。 | `plugins/agent-plugins/meeting-prep-agent` |
| `model-builder` | Agent 插件 | 构建 DCF、LBO、三表模型和 comps 工作簿。 | `plugins/agent-plugins/model-builder` |
| `month-end-closer` | Agent 插件 | 处理 accruals、roll-forwards 和 variance commentary。 | `plugins/agent-plugins/month-end-closer` |
| `pitch-agent` | Agent 插件 | 端到端生成投行 pitch：comps、precedents、LBO、估值 workbook 和 pitch deck。 | `plugins/agent-plugins/pitch-agent` |
| `statement-auditor` | Agent 插件 | 在分发前审计 LP statements 并核对关键数据。 | `plugins/agent-plugins/statement-auditor` |
| `valuation-reviewer` | Agent 插件 | 读取 GP packages，运行估值模板，并准备 LP reporting 草稿。 | `plugins/agent-plugins/valuation-reviewer` |
| `lseg` | Partner 插件 | 使用 LSEG 数据分析债券 RV、swap curves、FX carry、options vol 和宏观利率。 | `plugins/partner-built/lseg` |
| `sp-global` | Partner 插件 | 使用 S&P Global / Capital IQ 风格数据生成 tear sheets、earnings previews 和 funding digests。 | `plugins/partner-built/spglobal` |
| `equity-research` | Vertical 插件 | 支持 earnings notes、initiations、model updates、thesis 和 catalyst 跟踪。 | `plugins/vertical-plugins/equity-research` |
| `financial-analysis` | Vertical 插件 | 核心金融建模与分析：DCF、comps、LBO、三表模型、竞争分析和 deck QC。 | `plugins/vertical-plugins/financial-analysis` |
| `fund-admin` | Vertical 插件 | 支持 fund administration 和 finance ops：GL recon、break tracing、accruals、roll-forwards、NAV tie-out。 | `plugins/vertical-plugins/fund-admin` |
| `investment-banking` | Vertical 插件 | 支持投行业务材料：CIM、teaser、buyer list、merger model、process letter 和 deal tracking。 | `plugins/vertical-plugins/investment-banking` |
| `operations` | Vertical 插件 | 支持运营流程：KYC 文档解析和规则表评估。 | `plugins/vertical-plugins/operations` |
| `private-equity` | Vertical 插件 | 支持私募股权工作流：deal sourcing、screening、diligence、IC memo 和 portfolio monitoring。 | `plugins/vertical-plugins/private-equity` |
| `wealth-management` | Vertical 插件 | 支持财富管理：client reviews、financial plans、rebalancing、client reports 和 TLH。 | `plugins/vertical-plugins/wealth-management` |

## Agent 安装与目录

安装 `Plugin` 列中的 plugin，或将 `Skill path` 文件夹复制到 Codex skills 目录进行单独使用。

| Agent skill | Plugin | 功能 | Skill path |
| --- | --- | --- | --- |
| `agent-earnings-reviewer` | `earnings-reviewer` | 处理 earnings call、filings 和模型更新，输出 earnings note 草稿。 | `plugins/agent-plugins/earnings-reviewer/skills/agent-earnings-reviewer` |
| `agent-gl-reconciler` | `gl-reconciler` | 协调 GL reconciliation，从差异发现到根因追踪和复核包准备。 | `plugins/agent-plugins/gl-reconciler/skills/agent-gl-reconciler` |
| `agent-kyc-screener` | `kyc-screener` | 处理 onboarding packet，解析文件、执行规则并标记升级事项。 | `plugins/agent-plugins/kyc-screener/skills/agent-kyc-screener` |
| `agent-market-researcher` | `market-researcher` | 围绕行业或主题生成 market primer、竞争格局、peer comps 和投资想法。 | `plugins/agent-plugins/market-researcher/skills/agent-market-researcher` |
| `agent-meeting-prep-agent` | `meeting-prep-agent` | 为客户会议生成包含客户、新闻和行动建议的 briefing pack。 | `plugins/agent-plugins/meeting-prep-agent/skills/agent-meeting-prep-agent` |
| `agent-model-builder` | `model-builder` | 端到端构建金融模型，包括数据拉取、模型搭建和审计。 | `plugins/agent-plugins/model-builder/skills/agent-model-builder` |
| `agent-month-end-closer` | `month-end-closer` | 支持月结流程，包括 ledger review、roll-forward、posting package 和 variance commentary。 | `plugins/agent-plugins/month-end-closer/skills/agent-month-end-closer` |
| `agent-pitch-agent` | `pitch-agent` | 端到端生成投资银行 pitch，包括估值 workbook 和 branded deck。 | `plugins/agent-plugins/pitch-agent/skills/agent-pitch-agent` |
| `agent-statement-auditor` | `statement-auditor` | 审计 LP statement batch，并与 NAV pack 及关键口径核对。 | `plugins/agent-plugins/statement-auditor/skills/agent-statement-auditor` |
| `agent-valuation-reviewer` | `valuation-reviewer` | 读取 portfolio company valuation packages，运行估值复核并准备 LP reporting。 | `plugins/agent-plugins/valuation-reviewer/skills/agent-valuation-reviewer` |

## Command Catalog

Codex 不会直接加载 Claude slash commands。下方每个 command 都已经转换为一个 `command-*` skill。你可以按 slash command 名称向 Codex 请求对应行为，也可以安装或复制对应 skill。

| Command | Plugin | 功能 | Codex skill |
| --- | --- | --- | --- |
| `/analyze-bond-basis` | `lseg` | 分析债券期货 basis，包括 CTD 识别、implied repo rate 和 basis trade 评估。 | `command-analyze-bond-basis` |
| `/analyze-bond-rv` | `lseg` | 结合收益率曲线、信用利差和情景压力测试分析债券相对价值。 | `command-analyze-bond-rv` |
| `/analyze-fx-carry` | `lseg` | 结合 spot、forwards、vol surface 和历史背景评估 FX carry 交易机会。 | `command-analyze-fx-carry` |
| `/analyze-option-vol` | `lseg` | 分析期权波动率，包括 vol surface、Greeks、implied vs realized vol 对比。 | `command-analyze-option-vol` |
| `/analyze-swap-curve` | `lseg` | 结合政府债与通胀曲线 overlay 分析 swap curve 并识别曲线交易机会。 | `command-analyze-swap-curve` |
| `/macro-rates` | `lseg` | 构建宏观与利率 dashboard，覆盖经济指标、收益率曲线、通胀和 swap spreads。 | `command-macro-rates` |
| `/research-equity` | `lseg` | 生成综合 equity research snapshot，包含 consensus estimates、fundamentals 和股价表现。 | `command-research-equity` |
| `/review-fi-portfolio` | `lseg` | 复核固定收益组合，覆盖 pricing、reference data、cashflows 和 scenario analysis。 | `command-review-fi-portfolio` |
| `/catalysts` | `equity-research` | 查看或更新 catalyst calendar。 | `command-catalysts` |
| `/earnings-preview` | `equity-research` | 生成包含情景分析的 pre-earnings preview。 | `command-earnings-preview` |
| `/earnings` | `equity-research` | 分析季度 earnings，并生成 earnings update report。 | `command-earnings` |
| `/initiate` | `equity-research` | 创建 initiating coverage report。 | `command-initiate` |
| `/model-update` | `equity-research` | 使用新数据更新 financial model。 | `command-model-update` |
| `/morning-note` | `equity-research` | 起草 morning meeting note。 | `command-morning-note` |
| `/screen` | `equity-research` | 运行 stock screen 或生成投资想法。 | `command-screen` |
| `/sector` | `equity-research` | 创建 sector overview report。 | `command-sector` |
| `/thesis` | `equity-research` | 创建或更新 investment thesis。 | `command-thesis` |
| `/3-statement-model` | `financial-analysis` | 填充三表 financial model 模板。 | `command-3-statement-model` |
| `/competitive-analysis` | `financial-analysis` | 创建 competitive landscape analysis。 | `command-competitive-analysis` |
| `/comps` | `financial-analysis` | 构建 comparable company analysis 和 trading multiples。 | `command-comps` |
| `/dcf` | `financial-analysis` | 构建 DCF valuation model，并结合 comps-informed terminal multiples。 | `command-dcf` |
| `/debug-model` | `financial-analysis` | 调试和审计 financial model 中的错误。 | `command-debug-model` |
| `/lbo` | `financial-analysis` | 为 PE acquisition 构建 LBO model。 | `command-lbo` |
| `/ppt-template` | `financial-analysis` | 从 PowerPoint 模板创建可复用 PPT template skill。 | `command-ppt-template` |
| `/buyer-list` | `investment-banking` | 为 sell-side process 构建 buyer universe。 | `command-buyer-list` |
| `/cim` | `investment-banking` | 起草 Confidential Information Memorandum。 | `command-cim` |
| `/deal-tracker` | `investment-banking` | 跟踪并复核 live deal pipeline。 | `command-deal-tracker` |
| `/merger-model` | `investment-banking` | 构建 accretion/dilution merger model。 | `command-merger-model` |
| `/one-pager` | `investment-banking` | 使用品牌 PPT 模板创建一页 company strip profile。 | `command-one-pager` |
| `/process-letter` | `investment-banking` | 起草 process letter 或 bid instructions。 | `command-process-letter` |
| `/teaser` | `investment-banking` | 起草匿名 one-page teaser。 | `command-teaser` |
| `/ai-readiness` | `private-equity` | 扫描 portfolio，寻找最高杠杆的 AI opportunity。 | `command-ai-readiness` |
| `/dd-checklist` | `private-equity` | 生成 due diligence checklist。 | `command-dd-checklist` |
| `/dd-prep` | `private-equity` | 准备 diligence meeting 或 expert call。 | `command-dd-prep` |
| `/ic-memo` | `private-equity` | 起草 investment committee memo。 | `command-ic-memo` |
| `/portfolio` | `private-equity` | 复核 portfolio company performance。 | `command-portfolio` |
| `/returns` | `private-equity` | 构建 IRR/MOIC sensitivity tables。 | `command-returns` |
| `/screen-deal` | `private-equity` | 筛选 inbound deal，包括 CIM 或 teaser。 | `command-screen-deal` |
| `/source` | `private-equity` | 发现目标公司并起草 founder outreach。 | `command-source` |
| `/unit-economics` | `private-equity` | 分析 unit economics，包括 ARR cohorts、LTV/CAC 和 retention。 | `command-unit-economics` |
| `/value-creation` | `private-equity` | 构建 post-acquisition value creation plan。 | `command-value-creation` |
| `/client-report` | `wealth-management` | 生成 client performance report。 | `command-client-report` |
| `/client-review` | `wealth-management` | 准备 client review meeting。 | `command-client-review` |
| `/financial-plan` | `wealth-management` | 构建或更新 financial plan。 | `command-financial-plan` |
| `/proposal` | `wealth-management` | 为潜在客户创建 investment proposal。 | `command-proposal` |
| `/rebalance` | `wealth-management` | 分析配置偏离并生成 rebalancing trades。 | `command-rebalance` |
| `/tlh` | `wealth-management` | 识别 tax-loss harvesting opportunities。 | `command-tlh` |

## MCP Connectors

如果上游仓库提供了 `.mcp.json` 文件，本移植版会保留对应的 MCP connectors。多数金融数据 connectors 需要单独的服务商订阅、凭证和网络访问权限。

## 安全说明

这些工作流用于起草供合格专业人士审核的分析师工作成果。它们不构成投资、法律、税务或会计建议，也不应在缺少你方控制流程的情况下执行交易、批准入职、登记账务或承担风险。

## 来源

- 上游仓库：https://github.com/anthropics/financial-services
- Codex 移植仓库：https://github.com/deshengli0523-stack/finacial-service-for-codex
- 许可证：Apache-2.0；见 `LICENSE`。
