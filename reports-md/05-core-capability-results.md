# Chapter 5 — Core Capability Evaluation Results

## 5.1 Factual Reasoning & Knowledge

### 5.1.1 AA-Omniscience — knowledge accuracy and hallucination

On the AA-Omniscience benchmark (Artificial Analysis, 2026, T3), which jointly measures knowledge recall and hallucination tendency:

| Model configuration | Knowledge accuracy | Hallucination rate | Notes |
|---------------------|:------------------:|:------------------:|-------|
| GPT-5.5 (xhigh) | **57%** | **86%** | Highest knowledge accuracy among tested models; also highest hallucination rate |
| Claude Opus 4.7 (Max) | (lower) | **36%** | Approximately 50 percentage points lower hallucination rate |
| Gemini 3.1 Pro Preview | (lower) | **50%** | Intermediate position |

**Interpretation**: GPT-5.5 exhibits the highest knowledge accuracy among tested frontier models, but also the highest tendency to produce confident-sounding answers when uncertain. The 86% hallucination rate is the **largest single weakness identified by independent measurement** in this report. The 14-point Intelligence Index gain over GPT-5.4 (xhigh) came primarily from knowledge improvement, with hallucination reduction described as "weak" by the same source (Artificial Analysis, 2026, T3).

**Confidence statement**: Single T3 source (AA). Confidence interval not published. The hallucination rate is an aggregate across the AA-Omniscience corpus; specific categories may exhibit higher or lower rates.

### 5.1.2 GDPval-AA — real-work task performance

On GDPval-AA, a 44-profession real-work evaluation hosted by Artificial Analysis:

| Model configuration | Elo | Gap vs GPT-5.5 (xhigh) |
|---------------------|:---:|:----------------------:|
| GPT-5.5 (xhigh) | **1,785** | — |
| Claude Opus 4.7 (Max) | ~1,755 | -30 points |
| Gemini 3.1 Pro Preview | ~1,315 | -470 points |

Source: Artificial Analysis, 2026 (T3).

**Cross-tier verification**: OpenAI separately reported GDPval = 84.9% for GPT-5.5 (OpenAI, 2026, T6). The two figures (Elo vs percentage) are not directly comparable, but both place GPT-5.5 ahead of Claude Opus 4.7 and Gemini 3.1 Pro Preview at launch. The relative ordering is **verified**; the absolute magnitudes differ by measurement method.

### 5.1.3 Vendor-reported benchmarks (T6, pending T3 verification)

OpenAI reported the following factual-reasoning and knowledge benchmarks (OpenAI, 2026, T6). Each is flagged as "vendor-reported, pending independent verification" per the protocol in Section 2.3.

| Benchmark | Vendor-reported score | Independent verification status |
|-----------|:---------------------:|:-------------------------------:|
| BrowseComp | 84.4% | Not independently verified |
| FrontierMath Tier 1–3 | 51.7% | Not independently verified |
| FinanceAgent | 60.0% | Not independently verified |
| Internal investment-banking modeling | 88.5% | Not independently verified |
| OfficeQA Pro | 54.1% | Not independently verified |
| AIME 2025 (Instant) | 81.2 (vs GPT-5.3 Instant 65.4) | Not independently verified |
| MMMU-Pro (Instant) | 76.0 | Not independently verified. Note: Standard GPT-5.5 (non-Instant) separately reported 81.2% on MMMU-Pro vs Gemini 3.5 Flash 83.6% (per TechnicalAnalysis-D, T5 citing both vendors); see Chapter 6 |

### 5.1.4 Specific failures (T5)

**Failure case 5.1.A — Multimodal OCR failure**: When shown the a regional university logo, GPT-5.5 failed to identify it, while Gemini 3.5 Flash succeeded (an independent technical review, 2026-05-15, T5). Full prompt and output documented in Chapter 7.

**Failure case 5.1.B — Math convergence reasoning (relative)**: When asked to analyze the convergence of a function, GPT-5.3 jumped to a conclusion while GPT-5.5 produced a complete x→0⁺ and x→+∞ analysis (TechnicalAnalysis-C, 2026, T5). This is a **relative improvement over the previous generation**, not an absolute success.

### 5.1.5 Specific GPT-5.5 weaknesses in factual reasoning

- **Honest-refusal tendency is low**. GPT-5.5 (xhigh) prefers to answer uncertain questions rather than decline, producing the 86% hallucination rate noted in Section 5.1.1 (AA, 2026, T3)
- **non-English multimodal OCR is weaker than Gemini 3.5 Flash** for at least one tested case (an independent technical review, 2026, T5)
- **Mathematical reasoning rigor improved from GPT-5.3 to GPT-5.5** but is not systematically tested in this report's source set (TechnicalAnalysis-C, 2026, T5)

---

## 5.2 Code Generation

### 5.2.1 Vendor-reported benchmarks (T6)

| Benchmark | GPT-5.5 vendor-reported | Independent verification |
|-----------|:-----------------------:|:------------------------:|
| Terminal-Bench 2.0 | 82.7% | **Partially verified** — AA independently hosted Terminal-Bench Hard; GPT-5.5 leads, but absolute percentage not reproduced by AA |
| SWE-Bench Pro | 58.6% | Not independently verified; Claude Opus 4.7 reportedly within margin per TechnicalAnalysis-A (T5) |
| Expert-SWE | 73.1% | Not independently verified |

Source: OpenAI, 2026 (T6); cross-reference Artificial Analysis, 2026 (T3).

### 5.2.2 Independent (T3) ranking on Terminal-Bench Hard

GPT-5.5 led the AA-hosted Terminal-Bench Hard benchmark at launch (Artificial Analysis, 2026, T3). AA confirmed GPT-5.5's leading position but did not reproduce the 82.7% vendor-reported figure. The relative ordering (GPT-5.5 ahead of Claude Opus 4.7) is **verified**; the absolute magnitude is **not reproduced**.

### 5.2.3 Practitioner reports (T5) — qualitative coding behavior

Multiple T5 sources converge on the following qualitative findings about GPT-5.5's coding behavior:

1. **"Restrained" code generation**: GPT-5.5 tends to make minimal necessary changes rather than over-engineering, unlike some earlier models (Ben Davis, 2026-05-04, T5)
2. **Cross-file context retention**: GPT-5.5 maintains project-level context within a 400K-token Codex window (Ben Davis, 2026, T5; TechnicalAnalysis-A, 2026, T5)
3. **Engineering-grade security awareness**: When asked to implement a file-upload feature, GPT-5.5 proactively included UUID renaming, whitelist validation, size limits, and MIME verification — behaviors absent in GPT-5.3's output for the same prompt (TechnicalAnalysis-C, 2026, T5)
4. **Computer Use for test closure**: GPT-5.5 can write code, open a browser to view the result, identify bugs, and iterate without human intervention (Ben Davis, 2026-05-28, T5)

### 5.2.4 Codex platform integration as a code-generation multiplier

GPT-5.5 launched alongside major Codex platform upgrades: browser control, Sheets/Slides integration, Docs/PDF support, OS-level voice input, and an auto-review mode (Latent Space, 2026, T5). OpenAI reports that **85% of OpenAI employees use Codex weekly**, spanning software engineering, finance, communications, marketing, data science, and product teams (OpenAI, 2026, T6; cross-cited by TechnicalAnalysis-A and TechnicalAnalysis-E, T5).

**Verification status**: The 85% figure is a vendor internal metric (T6). No independent audit of this figure exists. It is reported here as the vendor's own claim about internal adoption, not as evidence of external production readiness.

### 5.2.5 Specific weaknesses in code generation

- **SWE-Bench Pro lead over Claude Opus 4.7 may be narrower than headline suggests**. TechnicalAnalysis-A (2026, T5) reports that OpenAI did not cite Claude Opus 4.7's SWE-Bench Pro score in its launch materials, which the article interprets as suggesting the gap is small
- **MCP Atlas (tool-use) lags competitors**: OpenAI-reported 75.3% vs Gemini 3.5 Flash 83.6% (OpenAI, 2026, T6; Google, 2026, T6)
- **Long-context coding has compaction regression**: see Section 5.3

### 5.2.6 Official Codex demonstrations (vendor-published, T6)

OpenAI published two demonstration Codex projects built with GPT-5.5:

1. **Artemis II 3D web application**: NASA Artemis II data visualized via WebGL 3D rendering with Vite
2. **3D dungeon arena prototype**: Three.js with combat system, enemy mechanics, and UI feedback

These demonstrations are vendor-published (T6) and not independently reproduced. They are cited here as examples of what the vendor claims the model can produce, not as evidence that the model can produce similar output for independent users.

---

## 5.3 Long-Context & Document Understanding

### 5.3.1 Context window specifications (T6)

| Configuration | Context window | Source |
|---------------|:--------------:|--------|
| GPT-5.5 API (Sam Altman confirmation) | **1,000,000 tokens** | Latent Space, 2026 (T5, citing OpenAI CEO) |
| GPT-5.5 in Codex | **400,000 tokens** | OpenAI, 2026 (T6) |

### 5.3.2 Practitioner finding — compaction regression (T5)

Ben Davis (2026-05-04, T5) reports that GPT-5.5's context compaction behavior is **weaker than GPT-5.4**:

> "GPT-5.5's compaction is weaker than GPT-5.4. In long conversations it's more likely to lose context. I recommend keeping threads under 100K tokens. The risk of compaction-induced context breakage is higher."

**Implication**: The advertised 400K–1M context window does not translate linearly to usable context. Practitioner evidence suggests a **usable context closer to 100K tokens** for stable operation, with quality degradation observed as the conversation approaches the upper bound.

**Verification status**: Single T5 source. No T3 benchmark independently measures compaction quality across context lengths. This is one of the **least-quantified findings** in the report; Chapter 11 flags it as a priority for future independent measurement.

### 5.3.3 Needle-in-haystack test (T5)

An independent technical review (2026-05-15, T5) reports a needle-in-haystack test using a a long-form television script (a long-form television script) script with three anomalous commands embedded ("the moon swallowed the key into the refrigerator"). **Both GPT-5.5 and Gemini 3.5 Flash failed to identify the anomalous commands.**

**Interpretation**: This is a single T5 test case with one prompt. It is **not** a systematic measurement. It does suggest that long-context needle detection may not be a strength for GPT-5.5 in at least one tested scenario, but it does not establish a general weakness.

### 5.3.4 Long-context positioning (vendor-reported, T6)

OpenAI reported that on a "long-context positioning" benchmark, GPT-5.5 scored 94.8% vs Gemini's 77.3% (OpenAI, 2026, T6; Google, 2026, T6). This figure is vendor-reported and not independently verified. The the independent technical review haystack failure (Section 5.3.3) is not directly comparable to this benchmark because the prompts differ.

---

## 5.4 Multi-Turn Instruction Following & Conversation

### 5.4.1 Vendor-reported τ²-Bench Telecom (T6)

OpenAI reported Tau2 Telecom = 98.0% for GPT-5.5 (OpenAI, 2026, T6), describing it as a "telecom customer-service flow test, no additional tuning." This is the **highest vendor-reported benchmark score** in the launch set.

**Verification status**: Not independently verified by T3 in this report's source set. Artificial Analysis independently measured a closely related benchmark, **τ²-Bench Telecom (AA-hosted variant)**, and found GPT-5.5 gained +7 points over GPT-5.4 on this benchmark (Artificial Analysis, 2026, T3). The direction of improvement is **verified**; the absolute 98.0% figure is not reproduced.

### 5.4.2 Instruction-following failure case (T5)

**Failure case 5.4.A — 300-word sci-fi story constraint violation** (an independent technical review, 2026-05-15, T5):

- **Prompt**: Write a 300-word sci-fi short story in which the male protagonist cannot speak
- **GPT-5.5 output**: 450–500 words (50%+ over the limit); the output was a spy thriller rather than sci-fi; the "cannot speak" constraint was handled by hanging a "no speaking allowed" sign on the protagonist
- **Gemini 3.5 Flash output**: ~320 words, on-topic sci-fi
- **Expected**: A ~300-word sci-fi story with the constraint integrated into the narrative

This is a Type B (instruction-understanding drift) failure. The model followed the constraint only literally and superficially, missing the spirit. Full prompt and output in Chapter 7.

### 5.4.3 Style / personality improvements (T5)

TechnicalAnalysis-C (2026-05-05, T5) reports that GPT-5.5's tone became less verbose, less emoji-heavy, and more "human-sounding" than earlier GPT-5.x generations. This is a qualitative observation; no benchmark in the source set quantifies style improvements.

### 5.4.4 Autonomous long-running workflows (T5)

Ben Davis (2026-05-28, T5) reports running GPT-5.5 (xhigh) on autonomous workflows lasting hours to overnight, including:

- Large-scale code migrations
- Complex refactoring tasks
- Multi-step research loops

The author reports that low-reasoning mode produces more errors on these tasks, while xhigh reasoning enables "first-try success." This is consistent with Artificial Analysis's finding that the effort ladder produces materially different capability profiles (Artificial Analysis, 2026, T3).

---

## 5.5 Generation Consistency & Stability

### 5.5.1 No T3 stability benchmark in source set

Artificial Analysis does not publish a stability/consistency benchmark in the source set used for this report. No T5 source systematically tests GPT-5.5's output variance across multiple runs at fixed temperature.

### 5.5.2 Indirect evidence of consistency behavior (T5)

Ben Davis (2026-05-04 and 2026-05-28, T5) reports two observations relevant to consistency:

1. **Low-reasoning mode produces variable results** on UI/design tasks across runs (first video)
2. **X-High reasoning produces more deterministic task completion** but at higher token cost (second video)

These observations are not quantified; no Jaccard similarity or variance metric is published. This report notes consistency as a **measurement gap** in Chapter 11.

### 5.5.3 Cross-effort-level consistency failure (T5, Type C)

Ben Davis's two videos (2026-05-04 and 2026-05-28, T5) are themselves a documented Type C (consistency) finding: the same author reversed his recommendation about GPT-5.5's optimal reasoning-effort setting within four weeks. This is not a model-output consistency failure; it is an **evaluator-conclusion consistency failure** that demonstrates the methodological dependence on effort-level specification (Section 4.2).

---

## 5.6 Capability Summary — What This Chapter Establishes

| Capability | GPT-5.5 position | Strength of evidence |
|------------|-----------------|---------------------|
| Factual knowledge accuracy | **Highest** among tested (57% on AA-Omniscience) | T3 verified |
| Hallucination avoidance | **Worst** among frontier models tested (86%) | T3 verified |
| Real-work task performance (GDPval-AA) | **Highest** among tested (1,785 Elo) | T3 verified |
| Terminal/command-line tasks | **Leading** (Terminal-Bench Hard) | T3 verified (relative); T6 magnitude unverified |
| SWE-Bench Pro | **Narrow lead** over Claude Opus 4.7 | T6 only; lead contested by T5 analysis |
| Long-context usable range | **~100K tokens practical** despite 400K–1M advertised | T5 only; not T3 verified |
| Multi-turn customer-service (τ²-Bench Telecom) | **Strong improvement** over GPT-5.4 (+7 AA points) | T3 verified (relative); T6 98% unverified |
| Creative writing with constraints | **Weaker** than Gemini 3.5 Flash in tested case | T5 only (single case) |
| Code security awareness | **Improved** over GPT-5.3 (UUID/whitelist/MIME) | T5 only (single case) |
| Output consistency | Not measured | Measurement gap |

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/ — **T3 primary evidence**
2. OpenAI. "GPT-5.5 launch announcement and system card." 2026-04-23. — **T6 vendor-reported benchmarks**
3. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04. — **T5 compaction and effort-level findings**
4. Ben Davis. "I was wrong about GPT 5.5." YouTube. 2026-05-28. — **T5 autonomous workflow and Computer Use findings**
5. an independent technical review. "Gemini 3.5 Flash vs GPT-5.5: a hands-on comparison." 2026-05-15. URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5 — **T5 failure cases with prompts**
6. TechnicalAnalysis-A (industry technical press). "GPT-5.5 launch: a detailed analysis." 2026-04-23. URL: https://example.com/technical-analysis/gpt-5.5-launch-detailed — **T5+T6 benchmark interpretation**
7. TechnicalAnalysis-C (industry technical press). "GPT-5.5 free tier launch: hands-on testing and ads platform." 2026-05-05. URL: https://example.com/technical-analysis/gpt-5.5-free-tier-ads — **T5 coding-security test**
8. TechnicalAnalysis-E (Industry technical analysis). "GPT-5.5 in practice: hands-on evaluation for real workloads." 2026-04-23. URL: https://example.com/technical-analysis/gpt-5.5-in-practice — **T5 Codex demos**
9. Latent Space. "[AINews] GPT 5.5 and OpenAI Codex Superapp." 2026-04-22/23. URL: https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp — **T5 context window and Codex platform**
