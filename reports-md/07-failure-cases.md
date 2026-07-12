# Chapter 7 — Failure Cases & Boundary Analysis

## 7.1 Failure-Case Inclusion Criteria

Per the methodology in Chapter 3 (Section 3.4), a failure case is included in this chapter only if all four criteria are met:

- (a) The full input prompt is documented in the source
- (b) The full model output is documented in the source
- (c) The expected output or correct answer is documented in the source
- (d) The source is independent (practitioner testing or independent measurement; not OpenAI-published)

Each failure case below is presented with: classification label, source citation, prompt, output, expected output, and analysis. The full corpus is small (8 cases); it is presented as **illustrative cases**, not as a systematic failure-rate measurement. Chapter 11 quantifies this limitation.

## 7.2 Failure-Case Classification

- **Type A** — Factual errors / hallucination
- **Type B** — Instruction-understanding drift
- **Type C** — Consistency failures (contradictory outputs for identical inputs)
- **Type D** — Long-context degradation
- **Type E** — Over-refusal (legitimate requests rejected)

---

## 7.3 Type A — Factual Errors / Hallucination

### 7.3.1 Aggregate hallucination rate
**Source**: Artificial Analysis, 2026-04-23
**Metric**: AA-Omniscience hallucination rate

**Finding**: GPT-5.5 (xhigh) hallucination rate = **86%**, compared with Claude Opus 4.7 (Max) = **36%** and Gemini 3.1 Pro Preview = **50%**.

**Methodology**: AA-Omniscience measures whether a model, when uncertain about a fact, produces a confident-sounding incorrect assertion (hallucination) or declines to answer (honest refusal). The 86% rate means GPT-5.5 (xhigh) produced confident incorrect assertions in 86% of cases where it lacked knowledge.

**Interpretation**: This is the **single most consequential finding** in this report. GPT-5.5 is the most hallucination-prone frontier model independently tested by AA. Simultaneously, GPT-5.5 has the **highest knowledge accuracy (57%)** among tested models. The combination means GPT-5.5 attempts to answer more questions than competitors, getting more correct in absolute terms but also producing more confident incorrect answers.

**Practical implication**: Any deployment where confidently-wrong answers carry higher cost than honest refusals (e.g., regulated advice, medical triage, legal research, financial audit) should treat GPT-5.5's outputs as requiring independent verification, more so than Claude Opus 4.7 or Gemini 3.1 Pro Preview.

**Confidence statement**: Independent measurement (Artificial Analysis). Aggregate rate across the AA-Omniscience corpus; category-specific rates not published.

### 7.3.2 Failure case 7.3.A — non-English multimodal OCR failure
**Source**: an independent technical review, 2026-05-15.

**Prompt**: [Image of the a regional university logo] "Identify this logo."

**GPT-5.5 output**: Did not correctly identify the logo (specific incorrect output documented in source; not reproduced here for brevity).

**Gemini 3.5 Flash output** (same prompt, same image): Correctly identified as "a regional university" (a regional university).

**Expected output**: "a regional university"

**Analysis**: GPT-5.5's multimodal OCR failed on a non-English institution logo where Gemini 3.5 Flash succeeded. This is consistent with Gemini 3.5 Flash's higher vendor-reported MMMU-Pro score (83.6% vs 81.2% per Google and OpenAI respectively). The case is a single data point, not a systematic measurement; it is reported because the prompt and output are fully documented in the source.

**Classification**: Type A — factual error in multimodal recognition.

---

## 7.4 Type B — Instruction-Understanding Drift

### 7.4.1 Failure case 7.4.A — Constrained creative writing
**Source**: an independent technical review, 2026-05-15.

**Prompt** : "Write a 300-word science fiction short story. The male protagonist cannot speak."

**GPT-5.5 output**:
- Word count: **450–500 words** (50%+ over the 300-word limit)
- Genre: **Spy thriller**, not science fiction
- Handling of "cannot speak" constraint: Literally hung a "no speaking allowed" sign on the protagonist, rather than integrating the constraint into the narrative

**Gemini 3.5 Flash output** (same prompt):
- Word count: ~320 words (within the 300-word limit, approximately)
- Genre: On-topic science fiction
- Constraint handling: Integrated into the narrative

**Expected**: A ~300-word sci-fi story with the "cannot speak" constraint woven into the narrative.

**Analysis**: GPT-5.5 violated three constraints simultaneously:
1. **Word-count constraint** (50%+ over)
2. **Genre constraint** (spy thriller instead of sci-fi)
3. **Spirit of the "cannot speak" constraint** (literal sign instead of narrative integration)

This is a Type B failure because the model followed the prompt's surface instructions (wrote a story, included a protagonist who could not speak) while drifting from the deeper instruction (300 words, sci-fi, narrative constraint).

**Classification**: Type B — instruction-understanding drift, multi-constraint.

**Caveat**: Single prompt, single author. Not a systematic measurement of creative-writing constraint adherence.

### 7.4.2 Failure case 7.4.B — Autonomous-agent permission scope
**Source**: Ben Davis, 2026-05-28
**Prompt** (paraphrased from transcript): Enable Computer Use with full system permissions for autonomous workflow execution.

**GPT-5.5 behavior**: When granted sudo-level permissions and full filesystem access, GPT-5.5 executed multi-step operations including system-level changes, dependency installation, and environment configuration. The practitioner reports this as desirable for autonomous workflows but acknowledges the safety risk:

> "I need to give my AI all the dangerous permissions. Complete trust in the model to control the desktop is a security risk, but for the model to actually 'complete work', full autonomy is necessary." — Ben Davis, 2026-05-28 (paraphrased from transcript, practitioner testing)

**Expected**: A model with granular permission scoping would request only the minimum privileges required for the current task. GPT-5.5 accepted blanket permissions without challenging the scope.

**Analysis**: This is a Type B failure in the sense that GPT-5.5 did not push back on an over-broad permission grant. The model's behavior is consistent with its design as an agentic tool, but it places the burden of permission management entirely on the user. For practitioners without Ben Davis's level of experience, this behavior could result in unintended system modifications.

**Classification**: Type B — instruction-understanding drift (permission scope).

**Important caveat**: This is a practitioner observation, not a measured failure rate. It is included because it surfaces a deployment-level failure mode that no benchmark in the source set measures.

### 7.4.3 Failure case 7.4.C — Math convergence reasoning (relative)

**Source**: TechnicalAnalysis-C, 2026-05-05.

**Prompt** (translated): Analyze the convergence of [a specified mathematical function].

**GPT-5.3 output**: Jumped directly to a conclusion, skipping the convergence verification step.

**GPT-5.5 output**: Produced a complete analysis covering both x→0⁺ and x→+∞ limits with proper convergence verification.

**Expected**: A complete convergence analysis.

**Analysis**: This is **not a GPT-5.5 failure** — it is a documented case where GPT-5.5 succeeded and GPT-5.3 failed. It is included in Chapter 7 to document the boundary of GPT-5.5's improvement: the model's mathematical reasoning is more rigorous than its predecessor's, but this report cannot verify whether it matches Claude Opus 4.7 or Gemini 3.1 Pro on the same task because no head-to-head test of this specific prompt was run across competitors.

**Classification**: Type B (relative) — GPT-5.3 failure, GPT-5.5 success; included for boundary documentation.

---

## 7.5 Type C — Consistency Failures

### 7.5.1 Failure case 7.5.A — Effort-level conclusion reversal
**Source**: Ben Davis, two videos published 2026-05-04 and 2026-05-28
**Observation**: The same author, evaluating GPT-5.5 on similar coding/UI workflows, published **contradictory recommendations** within four weeks:

- **First video (2026-05-04)**: "Strongly recommend low/no reasoning mode for UI/design/front-end tasks. X-High is wasteful; only useful for math/complex logic."
- **Second video (2026-05-28)**: "X-High reasoning unlocks powerful automation workflows. The same features can be achieved in low reasoning but with more errors. 'X-High first-try success' beats 'low reasoning multiple iterations'."

**Analysis**: This is not a model-output consistency failure. It is an **evaluator-conclusion consistency failure** that demonstrates the methodological dependence on the reasoning-effort setting. The same model produces materially different capability profiles at different effort levels, and conclusions about GPT-5.5's suitability for a task class can reverse entirely between effort levels.

**Implication**: Any benchmark or evaluation that does not specify the reasoning-effort level is incomplete. This report flags every GPT-5.5 data point with its effort level (per Section 4.2) to avoid this failure mode in its own conclusions.

**Classification**: Type C — evaluator-conclusion consistency failure (not model-output consistency).

---

## 7.6 Type D — Long-Context Degradation

### 7.6.1 Failure case 7.6.A — Compaction regression
**Source**: Ben Davis, 2026-05-04
**Finding**: GPT-5.5's context compaction is weaker than GPT-5.4. In long conversations, GPT-5.5 is more likely to lose context. The practitioner recommends keeping threads under **100,000 tokens** despite the advertised 400,000-token Codex context window (and the 1,000,000-token API context window confirmed by Sam Altman per Latent Space, 2026).

**Expected**: A model with a 400K-token advertised context window should maintain stable behavior across that range.

**Observed**: Quality degradation observed as conversation length approaches the upper bound, with compaction-induced context breakage as a higher-probability failure mode than in GPT-5.4.

**Analysis**: This is a Type D failure because it documents degradation of model quality as a function of context length, even when the context length is within the advertised window. The practical usable range appears to be approximately 100K tokens, not the advertised 400K–1M.

**Implication**: Production deployments that require sustained long conversations (e.g., long-running agent workflows, persistent code assistants) should plan thread-length budgets assuming a ~100K practical limit, not the advertised window.

**Classification**: Type D — long-context degradation.

**Confidence statement**: Single practitioner testing source. No independent benchmark in the source set measures compaction quality across context lengths. This is one of the **least-quantified findings** in this report.

### 7.6.2 Failure case 7.6.B — Needle-in-haystack test failure
**Source**: an independent technical review, 2026-05-15
**Prompt** (translated): The full text of a a long-form television script (a long-form television script) script with three anomalous commands embedded (example: "the moon swallowed the key into the refrigerator"). The model is asked to identify any anomalous instructions.

**GPT-5.5 output**: Failed to identify all three anomalous commands.

**Gemini 3.5 Flash output** (same prompt): Also failed to identify the anomalous commands.

**Expected**: Identification of the three anomalous commands.

**Analysis**: Both frontier models failed this particular needle-in-haystack test. This is a Type D failure for GPT-5.5 specifically because long-context needle detection is a standard long-context evaluation. The fact that Gemini 3.5 Flash also failed does not excuse GPT-5.5's failure; it suggests that the test may be harder than typical needle-in-haystack benchmarks, or that both models share a weakness on this particular test format.

**Classification**: Type D — long-context degradation (needle detection).

**Caveat**: Single prompt, single author. Not a systematic needle-in-haystack evaluation. The vendor-reported long-context positioning benchmark (GPT-5.5: 94.8% vs Gemini 3.5 Flash: 77.3% per OpenAI and Google respectively) is not directly comparable to this practitioner testing test because the prompts differ.

---

## 7.7 Type E — Over-Refusal

No source in this report's reference set documents a case where GPT-5.5 refused a legitimate request that should have been fulfilled.

**Interpretation**: This may reflect GPT-5.5's tendency to attempt answers rather than refuse, which is consistent with the 86% hallucination rate in Section 7.3.1.

---

## 7.8 Failure Modes Specific to GPT-5.5 (vs Competitors)

This section identifies failure modes that GPT-5.5 exhibits but competitors do not:

| Failure mode | GPT-5.5 exhibits? | Claude Opus 4.7 exhibits? | Gemini 3.1/3.5 exhibits? | Source |
|--------------|:------------------:|:-------------------------:|:-------------------------:|--------|
| 86% hallucination rate on AA-Omniscience | **Yes** | No (36%) | No (50%) | independent measurement (Artificial Analysis) |
| Compaction regression vs predecessor | **Yes** | Not measured in source | Not measured in source | practitioner testing (Ben Davis) |
| Accepts blanket "dangerous" permissions without pushback | **Yes** (in Codex/Computer Use) | Not tested in source | Not tested in source | practitioner testing (Ben Davis) |
| Creative writing over-word-count + genre drift | **Yes** (single case) | Not tested in source | No (single case) | practitioner testing (independent technical review) |
| regional institution logo OCR failure | **Yes** (single case) | Not tested in source | No (single case) | practitioner testing (independent technical review) |

**Interpretation**: The most consequential GPT-5.5-specific failure mode is the 86% hallucination rate. Other failure modes are documented from single practitioner testing sources and may or may not be GPT-5.5-specific upon systematic testing.

## 7.9 Failure Modes Specific to Competitors (GPT-5.5 succeeds)

For balance, the source set also documents cases where GPT-5.5 succeeded and competitors failed:

| Failure mode | GPT-5.5 succeeds? | Competitor fails? | Source |
|--------------|:------------------:|:-----------------:|--------|
| Math convergence reasoning rigor (vs GPT-5.3, not Claude/Gemini) | **Yes** | GPT-5.3 fails | practitioner testing (TechnicalAnalysis-C) |
| File-upload security implementation (vs GPT-5.3) | **Yes** | GPT-5.3 fails | practitioner testing (TechnicalAnalysis-C) |

These are within-OpenAI comparisons (GPT-5.5 vs GPT-5.3), not cross-competitor comparisons. No source in the corpus documents a case where GPT-5.5 succeeded and Claude Opus 4.7 or Gemini 3.1 Pro failed on the same prompt.

## 7.10 High-Risk Scenario Annotations

### 7.10.1 Code security tasks

GPT-5.5 demonstrated improved security-aware coding behavior (UUID renaming, whitelist validation, MIME verification) relative to GPT-5.3 in a single practitioner testing test (TechnicalAnalysis-C, 2026). This is an improvement, not an absolute success. The model did not exhibit code-injection vulnerability generation in this single test.

### 7.10.2 Long-running autonomous workflows

Ben Davis (2026-05-28) reports successful overnight autonomous runs with GPT-5.5 (xhigh). The failure mode here is not the model refusing to work, but the model accepting "dangerous" permissions without pushback (Section 7.4.2). The risk is in permission management, not in task execution.

## 7.11 Failure-Case Corpus Summary

| Failure type | Count | GPT-5.5-specific? | independent measurement or practitioner testing |
|--------------|:-----:|:------------------:|:--------:|
| Type A — Hallucination (aggregate) | 1 aggregate | Yes | independent measurement |
| Type A — Multimodal OCR | 1 case | Yes (vs Gemini 3.5 Flash) | practitioner testing |
| Type B — Creative writing constraints | 1 case | Yes (vs Gemini 3.5 Flash) | practitioner testing |
| Type B — Permission scope | 1 case | Not tested in competitors | practitioner testing |
| Type B — Math convergence (relative) | 1 case (GPT-5.5 succeeds) | Not applicable | practitioner testing |
| Type C — Evaluator conclusion reversal | 1 case | Not a model failure | practitioner testing |
| Type D — Compaction regression | 1 finding | Yes (within-OpenAI) | practitioner testing |
| Type D — Needle-in-haystack | 1 case | No (Gemini also fails) | practitioner testing |
| Type E — Over-refusal | 0 cases | Not documented | — |

**Total**: 8 distinct failure cases/ findings meeting inclusion criteria. The corpus is **small and not statistically representative**. It is presented as illustrative evidence; systematic failure-rate measurement requires primary testing not available in this report (Chapter 11).

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/
3. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04.
4. Ben Davis. "I was wrong about GPT 5.5." YouTube. 2026-05-28.
6. Latent Space. "[AINews] GPT 5.5 and OpenAI Codex Superapp." 2026-04-22/23. URL: https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp
