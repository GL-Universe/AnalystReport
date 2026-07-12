# Chapter 6 — Competitor Comparative Analysis

## 6.1 Overall Comparison Matrix

The matrix below summarizes GPT-5.5's position relative to its primary same-generation competitors. Each row is a capability dimension; each column is a model. Cells contain measured values with the source tier noted.

### 6.1.1 Intelligence & task performance

| Capability | GPT-5.5 (xhigh) | Claude Opus 4.7 (Max) | Gemini 3.1 Pro Preview | Source tier |
|------------|:---------------:|:---------------------:|:----------------------:|:-----------:|
| AA Intelligence Index | **Highest (+3)** | Tied at lower score | Tied at lower score | independent measurement (Artificial Analysis) |
| GDPval-AA Elo | **1,785** | ~1,755 | ~1,315 | independent measurement (Artificial Analysis) |
| AA-Omniscience knowledge accuracy | **57%** (highest) | Lower | Lower | independent measurement (Artificial Analysis) |
| AA-Omniscience hallucination rate | **86%** (worst) | **36%** (best) | 50% | independent measurement (Artificial Analysis) |
| Terminal-Bench Hard | **Leading** | Behind | Not tested in source | independent measurement (Artificial Analysis) |
| APEX-Agents-AA | **Leading** | Behind | Behind | independent measurement (Artificial Analysis) |

Source: Artificial Analysis, 2026.

### 6.1.2 Vendor-reported launch benchmarks (vendor-reported, partial independent verification)

| Benchmark | GPT-5.5 | Claude Opus 4.7 | Gemini 3.1 Pro Preview / 3.5 Flash | Verification |
|-----------|:-------:|:---------------:|:------------------------------------:|:------------:|
| Terminal-Bench 2.0 | 82.7% | (not cited) | (not cited) | vendor-reported only; independent measurement confirms relative lead |
| SWE-Bench Pro | 58.6% | (not cited; reported close per TechnicalAnalysis-A) | (not cited) | vendor-reported; contested |
| Expert-SWE | 73.1% | (not cited) | (not cited) | vendor-reported only |
| GDPval | 84.9% | 80.3% | 67.3% (3.1 Pro) | vendor-reported; relative order independently verified |
| OSWorld-Verified | 78.7% | (not cited) | (not cited) | vendor-reported only |
| CyberGym | 81.8% | (not cited) | (not cited) | vendor-reported only |
| BrowseComp | 84.4% | (not cited) | (not cited) | vendor-reported only |
| Tau2 Telecom | 98.0% | (not cited) | (not cited) | vendor-reported only; AA confirms +7 over GPT-5.4 |
| FrontierMath Tier 1–3 | 51.7% | (not cited) | (not cited) | vendor-reported only |
| MMMU-Pro | 81.2% | (not cited) | 83.6% (3.5 Flash) | vendor-reported; Gemini leads. Note: GPT-5.5 Instant separately reported 76.0 on MMMU-Pro (per TechnicalAnalysis-B) |
| MCP Atlas (tool use) | 75.3% | (not cited) | 83.6% (3.5 Flash) | vendor-reported; Gemini leads |
| Code execution | 78.2% | (not cited) | 76.2% (3.5 Flash) | vendor-reported; GPT-5.5 leads |
| Long-context positioning | 94.8% | (not cited) | 77.3% (3.5 Flash) | vendor-reported; GPT-5.5 leads |
| Abstract logical reasoning | 84.6% | (not cited) | 72.1% (3.5 Flash) | vendor-reported; GPT-5.5 leads |

Sources: OpenAI, 2026; Google, 2026; TechnicalAnalysis-D aggregating both vendors' published numbers.

### 6.1.3 Cost-efficiency matrix
| Configuration | Cost per AA Index run | Intelligence match | Cost ratio vs GPT-5.5 (Medium) |
|---------------|:---------------------:|:------------------:|:-------------------------------:|
| GPT-5.5 (Medium) | ~$1,200 | = Opus 4.7 (Max) | 1.0× (baseline) |
| Claude Opus 4.7 (Max) | ~$4,800 | = GPT-5.5 (Medium) | 4.0× |
| Gemini 3.1 Pro Preview | ~$900 | = GPT-5.5 (Medium) | 0.75× |
| GPT-5.5 (Low) | ~$500 | ≈ Opus 4.7 (Non-reasoning, High) | 0.42× |
| Claude Opus 4.7 (Non-reasoning, High) | ~$1,000 | ≈ GPT-5.5 (Low) | 0.83× |

Source: Artificial Analysis, 2026.

**Key finding**: Gemini 3.1 Pro Preview is **cheaper than GPT-5.5 at matched intelligence** (~$900 vs ~$1,200 per Index run), making GPT-5.5 **not the cost-efficiency leader** on the AA Intelligence Index. GPT-5.5's cost advantage is specific to the comparison with Claude Opus 4.7 (Max).

### 6.1.4 Token-level cost (vendor-reported list prices)

| Model | Input ($/M tokens) | Output ($/M tokens) | Notes |
|-------|:------------------:|:------------------:|-------|
| GPT-5.5 | $5 | $30 | 2× GPT-5.4 |
| GPT-5.5 Pro | $30 | $180 | For high-volume Pro users |
| GPT-5.5 Instant | Free in ChatGPT (ad-supported) | — | Ads: CPC $3–5, CPM $60 |
| Claude Opus 4.7 (Max) | (list price; AA cost data used) | — | AA-measured ~$4,800/Index |
| Gemini 3.1 Pro Preview | (list price; AA cost data used) | — | AA-measured ~$900/Index |
| DeepSeek-V4 Flash | $0.14 | $0.28 | Open-weight; MIT license |
| DeepSeek-V4 Pro | $1.74 | $3.48 | Open-weight; 1.6T params |

Sources: OpenAI 2026; Anthropic 2026; Google 2026; DeepSeek 2026; cross-validated by Artificial Analysis 2026 for Index-run costs.

## 6.2 GPT-5.5's Substantive Advantage Scenarios

Scenarios where GPT-5.5 exhibits statistically meaningful advantages, per independent measurement measurement:

### 6.2.1 Knowledge recall

GPT-5.5 (xhigh) achieved the highest knowledge accuracy (57%) on AA-Omniscience (Artificial Analysis, 2026). This is a +14-point gain over GPT-5.4 (xhigh), the largest single-dimension gain in the AA Intelligence Index.

### 6.2.2 Real-work tasks (GDPval-AA)

GPT-5.5 (xhigh) at 1,785 Elo leads Claude Opus 4.7 (Max) by ~30 points and Gemini 3.1 Pro Preview by ~470 points (Artificial Analysis, 2026).

### 6.2.3 Agentic capability (APEX-Agents-AA)

GPT-5.5 led the AA-hosted APEX-Agents-AA benchmark at launch (Artificial Analysis, 2026). This is consistent with the broader industry observation that Codex's platform integration (browser control, auto-review, multi-tool orchestration) gives GPT-5.5 an agentic-workflow advantage (Latent Space, 2026; Ben Davis, 2026-05-28).

### 6.2.4 Customer-service workflow (τ²-Bench Telecom)

GPT-5.5 gained +7 points over GPT-5.4 on τ²-Bench Telecom (Artificial Analysis, 2026). This is a substantive generational improvement, though the absolute 98.0% vendor-reported figure is not independently reproduced.

### 6.2.5 Cost-efficiency vs Claude Opus 4.7 (Max)

At the Medium effort level, GPT-5.5 matches Claude Opus 4.7 (Max) intelligence at one quarter the cost (Artificial Analysis, 2026). This is a 4× cost-efficiency advantage for users whose tasks fit within Medium reasoning.

### 6.2.6 Coding security awareness (practitioner testing case)

When asked to implement a file-upload feature, GPT-5.5 proactively included UUID renaming, whitelist validation, size limits, and MIME verification, while GPT-5.3 produced only basic file-type checking (TechnicalAnalysis-C, 2026). This is a single-prompt case study, not a systematic measurement.

## 6.3 GPT-5.5's Disadvantage Scenarios

GPT-5.5 exhibits the following disadvantages relative to specific competitors:

### 6.3.1 Hallucination rate — worst among frontier models tested

GPT-5.5 (xhigh) hallucination rate: **86%**. Claude Opus 4.7 (Max): **36%**. Gemini 3.1 Pro Preview: **50%** (Artificial Analysis, 2026). GPT-5.5 is the **most hallucination-prone** of the three frontier models independently tested by AA.

**Implication**: For any deployment where predictable refusal of uncertain questions is more important than breadth of attempted answers (e.g., legal compliance, medical triage, regulated advisory), Claude Opus 4.7 has a measurable advantage.

### 6.3.2 Three AA benchmarks led by Gemini 3.1 Pro Preview

Artificial Analysis reports that Gemini 3.1 Pro Preview led GPT-5.5 in **three additional evaluations** beyond the ones where GPT-5.5 led (Artificial Analysis, 2026). Specific benchmark names not enumerated in the source; this report notes the count but cannot name the three benchmarks.

### 6.3.3 Multimodal OCR (practitioner testing case)

In a head-to-head test with Gemini 3.5 Flash on a non-English logo (a regional university), GPT-5.5 failed to recognize the logo while Gemini 3.5 Flash succeeded (an independent technical review, 2026-05-15). This is a single-prompt case; it is not a systematic measurement but is consistent with Gemini 3.5 Flash's higher MMMU-Pro score (83.6% vs 81.2%, vendor-reported).

### 6.3.4 Tool use (MCP Atlas)

OpenAI-reported MCP Atlas: GPT-5.5 at 75.3% vs Gemini 3.5 Flash at 83.6% (OpenAI, 2026; Google, 2026). GPT-5.5 lags by 8.3 percentage points on this tool-use benchmark per vendor-reported data.

### 6.3.5 Constrained creative writing

In a 300-word sci-fi story test, GPT-5.5 produced 450–500 words (50%+ over limit) and wrote a spy thriller instead of sci-fi (an independent technical review, 2026). Gemini 3.5 Flash produced ~320 words of on-topic sci-fi. This is a single case but suggests GPT-5.5 may be weaker on tightly constrained creative tasks.

### 6.3.6 SWE-Bench Pro lead may be narrower than headline

TechnicalAnalysis-A (2026) observes that OpenAI did not cite Claude Opus 4.7's SWE-Bench Pro score in its launch materials, interpreting this as suggesting the gap is small. This is an interpretive judgment from a practitioner testing source, not a measured finding.

### 6.3.7 Compaction regression

GPT-5.5's compaction is reported to be weaker than GPT-5.4, with a recommended practical context of ~100K tokens despite a 400K–1M advertised window (Ben Davis, 2026-05-04). No competitor compaction data is available in the source set for direct comparison; this is flagged as a within-model regression rather than a cross-competitor disadvantage.

### 6.3.8 Safety filter regression (Instant variant)

OpenAI's own system card reports gore filtering regressed from 0.867 to 0.703 and sexual filtering from 0.857 to 0.806 for GPT-5.5 Instant, with jailbreak resistance also regressing (OpenAI, 2026; TechnicalAnalysis-B, 2026). These are **vendor-reported regressions** in OpenAI's own safety evaluation. Independent safety benchmarking data is not available in this report's source set.

### 6.3.9 Claude workflow switching cost

For users deeply integrated with Claude-specific agent workflows, tools, and skill ecosystems, switching to Codex-based GPT-5.5 workflows incurs a switching cost that may offset the model-level advantage (EveryTo, 2026; partial paywalled source).

## 6.4 Cost-Effectiveness Tradeoffs

### 6.4.1 Pareto frontier interpretation

The "intelligence per dollar" Pareto framework (popularized by Noam Brown, per Latent Space, 2026) places:

- **Gemini 3.1 Pro Preview** at the cost-efficiency frontier (~$900/Index run at matched intelligence)
- **GPT-5.5 (Medium)** at a 33% cost premium to Gemini 3.1 Pro Preview for matched intelligence
- **Claude Opus 4.7 (Max)** at a 4× cost premium to GPT-5.5 (Medium) for matched intelligence

**Interpretation**: GPT-5.5 is **not** the cost-efficiency leader. Gemini 3.1 Pro Preview is. GPT-5.5 is the cost-efficiency leader **only in comparison to Claude Opus 4.7 (Max)**.

### 6.4.2 Token efficiency vs price
GPT-5.5 uses **~40% fewer output tokens** than GPT-5.4 to reach the same Intelligence Index score, absorbing most of the 2× per-token price increase (Artificial Analysis, 2026). The net cost of running the AA Intelligence Index on GPT-5.5 increased by only **~20%** over GPT-5.4, and GPT-5.5 remained ~30% cheaper than Claude Opus 4.7 (Max) (Artificial Analysis, 2026).

### 6.4.3 Head-to-head cost comparison (practitioner testing cross-validated by independent measurement)

An independent technical review (2026-05-15) reports an Artificial-Analysis-derived comparison:

- **GPT-5.5 (Medium)**: ~22M tokens consumed, cost ~$1,199, Index score 57
- **Gemini 3.5 Flash**: ~73M tokens consumed, cost ~$1,522, Index score 55

**Key insight**: Gemini 3.5 Flash used **3.3× more tokens** to reach a slightly lower score than GPT-5.5 (Medium). Despite Gemini 3.5 Flash's lower per-token list price, its higher token consumption means **GPT-5.5 (Medium) is cheaper per quality-adjusted task** in this measured case.

**Important caveat**: This comparison is between Gemini 3.5 Flash (the faster, cheaper Gemini variant) and GPT-5.5 (Medium). It does not contradict Section 6.4.1, which notes that Gemini 3.1 Pro Preview is cheaper than GPT-5.5 at matched intelligence. The two findings coexist because they compare different Gemini variants.

### 6.4.4 DeepSeek-V4 — open-weight price floor

DeepSeek-V4 Preview, released the same day as GPT-5.5, lists V4-Flash at $0.14/$0.28 per million tokens and V4-Pro at $1.74/$3.48 (DeepSeek, 2026; Latent Space, 2026). At these prices, DeepSeek-V4 is an order of magnitude cheaper than GPT-5.5 at the per-token level. Independent Intelligence Index measurement of DeepSeek-V4 is not yet available in this report's source set. DeepSeek-V4's inclusion here is as a **price-floor reference point**, not as a directly compared model.

## 6.5 Competitor Summary

| Competitor | GPT-5.5's relative position |
|------------|----------------------------|
| Claude Opus 4.7 (Max) | GPT-5.5 leads on Intelligence Index, GDPval-AA, knowledge accuracy; lags on hallucination; 4× cost advantage at Medium reasoning |
| Gemini 3.1 Pro Preview | GPT-5.5 leads on Intelligence Index overall; Gemini leads on 3 additional AA evaluations; **Gemini is cheaper at matched intelligence** |
| Gemini 3.5 Flash | GPT-5.5 leads on code execution, long-context positioning, abstract reasoning; Gemini leads on MMMU-Pro, MCP Atlas, and the tested OCR case |
| DeepSeek-V4 | Not directly compared on Intelligence Index; DeepSeek-V4 is ~10× cheaper per token; open-weight MIT license |

**Bottom line**: GPT-5.5 is the **highest-scoring** model on the AA Intelligence Index at the time of writing, but it is **not the cheapest** (Gemini 3.1 Pro Preview is) and **not the most hallucination-resistant** (Claude Opus 4.7 is). The vendor-reported benchmarks are **partially verified** by independent measurement measurement but not fully reproduced at the headline magnitudes.

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/
3. Latent Space. "[AINews] GPT 5.5 and OpenAI Codex Superapp." 2026-04-22/23. URL: https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp
4. OpenAI. "GPT-5.5 launch announcement." 2026-04-23.
5. Anthropic. "Claude Opus 4.7 model card and pricing." 2026.
6. Google. "Gemini 3.1 Pro and 3.5 Flash launch and benchmarks." 2026.
7. DeepSeek. "DeepSeek-V4 Preview release." 2026-04-23.
9. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04.
10. EveryTo (Laura Entis). "Who Isn't Using GPT 5.5." 2026-04-30. URL: https://every.to/context-window/who-isnt-using-gpt-55
