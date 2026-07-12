# Chapter 4 — Evaluation Metrics System

## 4.1 Core Metric Definitions

This report uses the following metrics to evaluate GPT-5.5. Each metric is defined with its computation method and the reference standard it follows.

| Metric | Definition | Computation method | Reference standard |
|--------|------------|---------------------|---------------------|
| **Intelligence Index score** | Aggregate normalized score across multiple cognitive/task benchmarks | Weighted aggregation by Artificial Analysis (methodology public) | AA Intelligence Index (Artificial Analysis, 2026, T3) |
| **Knowledge accuracy** | Proportion of verifiable facts correctly recalled from a closed corpus | Per-item scoring against gold answers in AA-Omniscience corpus | AA-Omniscience (Artificial Analysis, 2026, T3) |
| **Hallucination rate** | Proportion of unverifiable or false assertions delivered with confidence, when uncertain | Forced-choice + human grading against corpus; lower is better | AA-Omniscience (Artificial Analysis, 2026, T3) |
| **GDPval-AA Elo** | Win-rate-derived rating on 44-profession real-work tasks | Elo computation from pairwise model comparisons on GDPval tasks | GDPval-AA (adapted from OpenAI GDPval; hosted by AA, T3) |
| **Terminal-Bench Hard pass rate** | Proportion of multi-step terminal/command-line tasks completed correctly | Automated test execution + graded outcome | Terminal-Bench Hard (AA-hosted, T3) |
| **SWE-Bench Pro pass rate** | Proportion of real-world software engineering issues successfully resolved | Repository-level test pass + diff validation | SWE-Bench Pro (vendor-reported; not independently verified) |
| **Instruction-following rate** | Proportion of complex instructions executed in full compliance with constraints | Structured rubric scoring; T5 sources document specific cases | MT-Bench-style rubric (per `GPT5.5outline.md`) |
| **Cost per Intelligence Index run** | US-dollar cost of running the full AA Intelligence Index suite per model | Token consumption × vendor list price | Vendor list prices (OpenAI 2026, Anthropic 2026, Google 2026) |
| **Token efficiency** | Output tokens consumed per unit of benchmark score achieved | Output tokens ÷ Index score (or task score) | Artificial Analysis methodology (T3) |
| **Preparedness Framework rating** | OpenAI's internal risk classification (Low / Medium / High) | OpenAI's internal red-team assessment | OpenAI Preparedness Framework (OpenAI, 2026, T6) |
| **Safety filter rate** | Proportion of flagged categories (gore, sexual, jailbreak) successfully filtered | Vendor-internal red-team scoring; lower scores indicate more leakage | OpenAI system card (T6) |

## 4.2 Reasoning-Effort Ladder as Evaluation Variable

A defining methodological feature of GPT-5.5 is the **five-level reasoning-effort ladder** (xhigh / high / medium / low / non-reasoning), which OpenAI exposes to users and which Artificial Analysis tested independently (OpenAI, 2026, T6; Artificial Analysis, 2026, T3).

This report treats the effort level as a **primary evaluation variable**. The same metric (e.g., hallucination rate) can produce materially different values depending on the effort level. Therefore:

- Every GPT-5.5 metric citation in this report **specifies the effort level** (e.g., "GPT-5.5 (xhigh) hallucination rate: 86%")
- Cross-competitor comparisons are made at **matched effort levels** where possible (e.g., GPT-5.5 (Medium) vs Claude Opus 4.7 (Max))
- Aggregations across effort levels are **not used** without explicit weighting disclosure

This metric design responds to the methodological observation from Ben Davis (2026, T5) that conclusions about GPT-5.5's suitability for a task can reverse entirely between effort levels. Any evaluation that omits the effort-level specification is treated as **methodologically incomplete** and flagged as such.

## 4.3 Cost-Effectiveness Metric Design

Cost-effectiveness is operationalized through three complementary metrics:

### 4.3.1 Per-token list price (USD per million tokens)

| Model | Input ($/M tokens) | Output ($/M tokens) | Source |
|-------|:-----------------:|:------------------:|--------|
| GPT-5.5 | $5 | $30 | OpenAI, 2026 (T6) |
| GPT-5.5 Pro | $30 | $180 | OpenAI, 2026 (T6) |
| GPT-5.5 Instant | Free in ChatGPT (ad-supported) | — | OpenAI, 2026 (T6) |
| Claude Opus 4.7 (Max) | (used for cost comparison baseline) | — | Anthropic, 2026 (T6) |
| Gemini 3.1 Pro Preview | (lower than GPT-5.5 at matched intelligence) | — | Google, 2026 (T6); AA, 2026 (T3) |
| DeepSeek-V4 Flash | $0.14 | $0.28 | DeepSeek, 2026 (T6) |
| DeepSeek-V4 Pro | $1.74 | $3.48 | DeepSeek, 2026 (T6) |

### 4.3.2 Cost per Intelligence Index run

This is the primary cost-effectiveness metric used in Chapter 8. It measures the US-dollar cost of running the full Artificial Analysis Intelligence Index suite on a given model at a given effort level.

| Model configuration | Cost per Index run | Source |
|---------------------|:------------------:|--------|
| GPT-5.5 (Medium) | ~$1,200 | AA, 2026 (T3) |
| Claude Opus 4.7 (Max) | ~$4,800 | AA, 2026 (T3) |
| Gemini 3.1 Pro Preview | ~$900 | AA, 2026 (T3) |
| GPT-5.5 (Low) | ~$500 | AA, 2026 (T3) |
| Claude Opus 4.7 (Non-reasoning, High) | ~$1,000 | AA, 2026 (T3) |

### 4.3.3 Cost-efficiency ratio (intelligence per dollar)

For Chapter 6's cost-effectiveness tradeoff analysis:

```
Cost-efficiency ratio = Intelligence Index score ÷ Cost per Index run
```

This ratio allows direct comparison of models at different price-performance points. The ratio is reported in Chapter 6 alongside the absolute scores to avoid the misleading impression that a cheaper model is necessarily better.

## 4.4 Safety Metric Design

Safety evaluation in this report uses three metric categories:

### 4.4.1 Vendor self-assessment metrics (T6)

- **OpenAI Preparedness Framework rating**: Low / Medium / High classification by domain (Cybersecurity, CBRN, Persuasion, Autonomy)
- **OpenAI system card safety filter rates**: Proportion of test prompts in each category (gore, sexual, jailbreak) that the model successfully refuses; reported as decimal scores where **lower indicates more leakage** (worse safety)

The system card's inverse-score convention (lower = worse) is preserved in this report. A regression from 0.867 to 0.703 in gore filtering therefore represents a **worsening** of safety, not an improvement.

### 4.4.2 Independent safety metrics (T3, not yet available)

Artificial Analysis does not currently host an independent safety benchmark for GPT-5.5. This report's Chapter 9 notes the absence of T3 safety verification as a key limitation.

### 4.4.3 Failure-case-derived safety indicators (T5)

Where T5 practitioners document safety-relevant failures (e.g., granting "sudo" permissions to autonomous agents, executing "dangerous" code), these are reported as qualitative indicators in Chapter 9 but are not aggregated into a safety score.

## 4.5 Inter-Rater Reliability Statement

This report aggregates existing measurements rather than running new human evaluations. Therefore, inter-rater reliability is determined by the underlying sources:

- **T3 (Artificial Analysis)**: published methodology includes inter-rater reliability metrics; users of this report should consult AA's methodology page for current values
- **T5 (user testing reports)**: typically single-author; no inter-rater reliability metric available. This report treats T5 findings as illustrative cases, not as systematic evaluations. Where multiple T5 sources converge on the same finding, this is noted as "inter-source convergence" and given more weight than single-source findings.
- **T6 (vendor)**: inter-rater reliability of OpenAI's internal red-team is not publicly disclosed; this report does not rely on T6 safety figures as primary evidence

## 4.6 Confidence Interval Reporting

Per `summary-white-paper-focus.md` Section V (Feature F: Balanced Conclusions) and `GPT5.5outline.md` Chapter 5 requirements, each quantitative finding in this report is reported with a confidence indicator where available:

- **AA Intelligence Index scores**: reported with the confidence band published by Artificial Analysis (consult AA methodology page)
- **T5 failure cases**: reported as cases, not rates; confidence intervals not applicable to illustrative examples
- **Vendor-reported benchmarks**: reported without confidence intervals because OpenAI does not publish them; the absence is flagged

Where confidence intervals are not available, the report uses language like "single measurement, no confidence interval published" rather than implying false precision.

## 4.7 Red Lines Observed in This Chapter

Per `GPT5.5outline.md`:

- ❌ Did not use absolute ("best", "leading") language in metric definitions — all metrics are operationalized with specific computation methods
- ❌ Did not design metrics that inherently favor one vendor — all metrics are applied uniformly across GPT-5.5, Claude Opus 4.7, and Gemini 3.1/3.5

## 4.8 Metric Limitations

- The **Intelligence Index** is a composite metric; its weighting is determined by Artificial Analysis and may not reflect all users' priorities
- **GDPval-AA Elo** measures performance on 44 specific professions; generalization to professions outside that set is uncertain
- **Cost per Index run** assumes list pricing; volume discounts and enterprise agreements can materially change the cost picture
- **Safety filter rates** use the vendor's own classification taxonomy; independent taxonomies (e.g., UK AISI's) may produce different scores
- **Token efficiency** is measured at the output level only; input-token efficiency is not separately reported in this report

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/ — **T3 metric definitions**
2. OpenAI. "GPT-5.5 system card and Preparedness Framework." 2026-04-23. — **T6 vendor metric definitions**
3. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04. — **T5 effort-level methodology demonstration**
4. an independent technical review. "Gemini 3.5 Flash vs GPT-5.5: a hands-on comparison." 2026-05-15. URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5 — **T5 cost-comparison data source**
5. Latent Space. "[AINews] GPT 5.5 and OpenAI Codex Superapp." 2026-04-22/23. URL: https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp — **T5+T3 cost data**
6. `white-paper-research/summary-white-paper-focus.md` — citation standards (feature F)
7. `reports-md/GPT5.5outline.md` — chapter outline reference
