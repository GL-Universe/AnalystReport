# Chapter 8 — Cost-Effectiveness Analysis

## 8.1 API Pricing Structure (vendor-reported list prices, dated 2026-04-23)

### 8.1.1 OpenAI GPT-5.5 list prices

| Variant | Input ($/M tokens) | Output ($/M tokens) | Source |
|---------|:------------------:|:------------------:|--------|
| GPT-5.5 | $5 | $30 | OpenAI, 2026-04-23 |
| GPT-5.5 Pro | $30 | $180 | OpenAI, 2026-04-23 |
| GPT-5.5 Instant | Free in ChatGPT (ad-supported for free users) | — | OpenAI, 2026; TechnicalAnalysis-C, 2026 |

**Pricing change vs GPT-5.4**: GPT-5.5 per-token list prices are **2× GPT-5.4's** prices (OpenAI, 2026; cross-cited by Berman, Ben Davis, TechnicalAnalysis-A, TechnicalAnalysis-E, all practitioner sources).

### 8.1.2 Competitor list prices (for comparison)

| Model | Input ($/M tokens) | Output ($/M tokens) | Source |
|-------|:------------------:|:------------------:|--------|
| Claude Opus 4.7 (Max) | Anthropic list price (specific figures not in source set) | — | Anthropic, 2026 |
| Gemini 3.1 Pro Preview | Google list price (specific figures not in source set) | — | Google, 2026 |
| DeepSeek-V4 Flash | $0.14 | $0.28 | DeepSeek, 2026-04-23 |
| DeepSeek-V4 Pro | $1.74 | $3.48 | DeepSeek, 2026-04-23 |

**Observation**: DeepSeek-V4 is **an order of magnitude cheaper per token** than GPT-5.5. However, per-token price alone does not determine task-level cost (see Section 8.4.2).

### 8.1.3 OpenAI Ads platform pricing (context for Instant variant)

GPT-5.5 Instant is free in ChatGPT, supported by the OpenAI Ads platform launched concurrently (OpenAI, 2026; TechnicalAnalysis-C, 2026):

- **CPC (cost per click)**: $3–5
- **CPM (cost per 1,000 impressions)**: $60
- **Relative to traditional search ads**: 3–4× Google Search rates (TechnicalAnalysis-C, 2026)

The Ads platform monetizes free-tier inference. For API users, this is **not a direct cost**; for ChatGPT users, it is an **attention-cost** rather than a dollar-cost. This report treats GPT-5.5 Instant as effectively free at the point of use for ChatGPT users, with the advertising subsidy noted as a structural condition.

## 8.2 Actual Task Cost (independent measurement measured)

### 8.2.1 Cost per Artificial Analysis Intelligence Index run

This is the primary cost-effectiveness metric used in this report (defined in Section 4.3.2). It measures the actual US-dollar cost of running the full AA Intelligence Index suite on each model at a specified effort level.

| Model configuration | Cost per Index run | Source |
|---------------------|:------------------:|--------|
| GPT-5.5 (Medium) | ~$1,200 | Artificial Analysis, 2026 |
| Claude Opus 4.7 (Max) | ~$4,800 | Artificial Analysis, 2026 |
| Gemini 3.1 Pro Preview | ~$900 | Artificial Analysis, 2026 |
| GPT-5.5 (Low) | ~$500 | Artificial Analysis, 2026 |
| Claude Opus 4.7 (Non-reasoning, High) | ~$1,000 | Artificial Analysis, 2026 |

**Key finding**: At Medium reasoning, GPT-5.5 matches Claude Opus 4.7 (Max) intelligence at **one quarter the cost**. This is a 4× cost-efficiency advantage vs Claude Opus 4.7 specifically.

### 8.2.2 Token efficiency
Artificial Analysis measured that GPT-5.5 uses **~40% fewer output tokens** than GPT-5.4 to reach the same Intelligence Index score (Artificial Analysis, 2026). This token-efficiency improvement absorbs most of the 2× per-token price increase.

**Cross-cited by practitioner testing**: Multiple practitioner testing sources (Berman 2026; Ben Davis 2026-05-04; TechnicalAnalysis-A 2026; TechnicalAnalysis-E 2026) cite the 20–40% token reduction, consistent with the AA-measured ~40% figure.

### 8.2.3 Net cost impact
The net cost of running the AA Intelligence Index on GPT-5.5 increased by only **~20%** over GPT-5.4, despite the 2× per-token price increase (Artificial Analysis, 2026). The token efficiency improvement absorbed approximately 80% of the price increase.

**Comparison with Claude Opus 4.7 (Max)**: GPT-5.5 is approximately **30% cheaper** than Claude Opus 4.7 (Max) on the same Intelligence Index workload (Artificial Analysis, 2026).

### 8.2.4 Head-to-head task cost — GPT-5.5 (Medium) vs Gemini 3.5 Flash (practitioner testing citing independent measurement)

An independent technical review (2026-05-15) reports an Artificial-Analysis-derived comparison that is particularly informative because it measures actual tokens consumed rather than list prices:

| Model | Tokens consumed | Cost | Index score |
|-------|:---------------:|:----:|:-----------:|
| GPT-5.5 (Medium) | ~22 million | ~$1,199 | 57 |
| Gemini 3.5 Flash | ~73 million | ~$1,522 | 55 |

Source: an independent technical review, 2026-05-15, citing Artificial Analysis data.

**Interpretation**: Gemini 3.5 Flash used **3.3× more tokens** than GPT-5.5 (Medium) to reach a slightly lower Intelligence Index score. Despite Gemini 3.5 Flash's lower per-token list price, its higher token consumption means **GPT-5.5 (Medium) is cheaper per quality-adjusted task** in this measured case.

**Important context**: This comparison is between Gemini 3.5 Flash (a faster, cheaper Gemini variant) and GPT-5.5 (Medium). It does **not** contradict the finding in Section 8.2.1 that **Gemini 3.1 Pro Preview** is cheaper than GPT-5.5 (Medium) at matched intelligence. The two findings coexist because they compare different Gemini variants:

- **Gemini 3.1 Pro Preview** (Section 8.2.1): cheaper than GPT-5.5 at matched intelligence (~$900 vs ~$1,200)
- **Gemini 3.5 Flash** (this section): uses 3.3× more tokens than GPT-5.5 to reach lower score (~$1,522 vs ~$1,199)

The comparison that matters depends on which Gemini variant a user would otherwise use.

## 8.3 Latency & Throughput

### 8.3.1 Speed observations
TechnicalAnalysis-E (2026) reports that GPT-5.5's end-to-end speed is "roughly on par with GPT-5.4" — a 20% speed improvement is attributed to Codex's optimized inference partitioning technique (OpenAI, 2026; TechnicalAnalysis-E, 2026).

### 8.3.2 Gemini 3.5 Flash speed advantage
Google reported that Gemini 3.5 Flash's output speed is **4× faster than other frontier models** (Google, 2026). This is a vendor-reported speed advantage.

## 8.4 Cost-Efficiency Ratio

### 8.4.1 Pareto frontier interpretation

Following the "intelligence per dollar" Pareto framework (popularized by Noam Brown; referenced in Latent Space, 2026):

| Position on Pareto frontier | Model | Implication |
|----------------------------|--------|-------------|
| **Cost-efficiency frontier** | Gemini 3.1 Pro Preview (~$900/Index run at matched intelligence) | Cheapest at matched intelligence |
| 33% cost premium to frontier | GPT-5.5 (Medium) (~$1,200/Index run) | Higher cost than Gemini 3.1 Pro Preview for same intelligence |
| 4× cost premium to GPT-5.5 (Medium) | Claude Opus 4.7 (Max) (~$4,800/Index run) | Most expensive at matched intelligence |

**Key conclusion**: GPT-5.5 is **not the Pareto-optimal model** on cost-efficiency. Gemini 3.1 Pro Preview is. GPT-5.5's cost advantage is specific to the comparison with Claude Opus 4.7 (Max).

### 8.4.2 Cost-efficiency ratio by use case

Different use cases favor different models on cost-efficiency:

| Use case pattern | Most cost-efficient model in source set | Rationale |
|-----------------|----------------------------------------|-----------|
| Matched-intelligence general tasks | **Gemini 3.1 Pro Preview** | $900 vs $1,200 vs $4,800 per Index run |
| Coding tasks requiring high reliability | **GPT-5.5 (Medium or higher)** | Higher code-quality consistency per practitioner testing; reports; lower error-correction overhead |
| Tasks requiring low hallucination | **Claude Opus 4.7 (Max or Non-reasoning High)** | 36% hallucination rate vs 86% for GPT-5.5 |
| Long-running autonomous workflows | **GPT-5.5 (X-High)** per Peter's $1.3M/month case | X-High required for first-try success; lower levels need multiple iterations |
| High-volume, low-complexity tasks | **DeepSeek-V4 Flash** | $0.14/$0.28 per million tokens; open-weight |
| Free-tier consumer use | **GPT-5.5 Instant** | Free in ChatGPT; ads-supported |

**Important**: These recommendations are conditional on the use case and on the user's tolerance for hallucination, switching cost, and tooling ecosystem. No single model is the cost-efficiency winner across all use cases.

### 8.4.3 Economic breakeven analysis

At what volume of usage does GPT-5.5's higher per-token price become economically unfavorable despite its token efficiency?

**Calculation**: Let GPT-5.5's per-token output price = $30/M. Let GPT-5.4's per-token output price = $15/M (2× ratio per OpenAI, 2026). Let GPT-5.5's token consumption = 0.6× GPT-5.4's (40% reduction per AA, 2026).

- GPT-5.5 cost per task = 0.6 × $30 = $18 per million output tokens equivalent
- GPT-5.4 cost per task = 1.0 × $15 = $15 per million output tokens equivalent

**Conclusion**: Per million output tokens equivalent, GPT-5.5 costs **$18 vs GPT-5.4's $15**, a net increase of ~20%. This matches the AA-measured net cost increase of ~+20% per Index run (Artificial Analysis, 2026). The breakeven point depends on whether the quality improvement (higher Intelligence Index score, more reliable task completion) is worth the 20% cost premium.

For tasks where GPT-5.4 produced unacceptable output quality and required human rework, the 20% premium is easily offset by labor savings. For tasks where GPT-5.4 was already adequate, the 20% premium is pure cost increase.

### 8.4.4 The Peter's $1.3M/month case
Ben Davis (2026-05-28) reports a case study of a practitioner ("Peter") spending **$1.3 million per month** on GPT-5.5 Pro (xhigh reasoning) API calls. The rationale:

> X-High reasoning's success rate on complex tasks is materially higher than other levels. Without X-High, certain tasks cannot be completed at all. This explains why Pro's $30/$180 pricing still has paying customers.

**Implication**: At extreme usage volumes ($1.3M/month), the cost is justified by task success that lower reasoning levels cannot achieve. This is a **vendor-side validation** of GPT-5.5's premium-tier pricing model: users with mission-critical tasks will pay 12× the standard output price ($180 vs $30 per million output tokens) for X-High reasoning.

**Caveat**: Single practitioner testing source; no independent verification of the $1.3M figure. The case is reported because it documents the economic logic of GPT-5.5 Pro's premium tier, not because the figure itself can be audited.

## 8.5 Cost Caveats and Limitations

### 8.5.1 List price vs negotiated price

All figures in this chapter use **list prices**. Enterprise agreements, volume discounts, and committed-use pricing can materially change the cost picture.

### 8.5.2 Cost data recency

All pricing figures are dated 2026-04-23 (GPT-5.5 launch) or the source publication date. AI vendor pricing changes frequently. The cost analysis in this chapter is a **point-in-time snapshot**, not a durable conclusion.

### 8.5.3 Vendor cost-saving claims excluded

This report does **not** cite OpenAI's own cost-saving claims (e.g., "GPT-5.5 reduces user cost by X%"). All cost findings in this chapter are either:
- independent measurement measured (Artificial Analysis Index runs)
- vendor-reported list prices (vendor-published, with date)
- practitioner testing practitioner reports (with named source)

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/
2. OpenAI. "GPT-5.5 launch announcement and pricing." 2026-04-23.
3. Anthropic. "Claude Opus 4.7 pricing." 2026.
4. Google. "Gemini 3.1 Pro Preview and 3.5 Flash pricing and speed." 2026.
5. DeepSeek. "DeepSeek-V4 Preview release and pricing." 2026-04-23.
6. Latent Space. "[AINews] GPT 5.5 and OpenAI Codex Superapp." 2026-04-22/23. URL: https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp
7. Ben Davis. "I was wrong about GPT 5.5." YouTube. 2026-05-28.
