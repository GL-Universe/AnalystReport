# Chapter 3 — Test Dataset Description

## 3.1 Dataset Provenance

This report does not introduce a new test dataset. It synthesizes evidence from three categories of existing datasets, each described below with provenance, composition, and control measures.

### 3.1.1 Primary independent datasets (T3)

| Dataset | Operator | Composition | Access |
|---------|---------|-------------|--------|
| **AA Intelligence Index** | Artificial Analysis | Aggregate of multiple cognitive/task benchmarks; normalized scoring | Public methodology at artificialanalysis.ai |
| **AA-Omniscience** | Artificial Analysis | Knowledge-recall corpus with paired hallucination detection; measures both accuracy and refusal tendency | Public benchmark |
| **GDPval-AA** | Artificial Analysis (adapted from OpenAI GDPval) | 44 real professions' tasks: data analysis, report writing, judgment calls; not multiple-choice | Public Elo rankings |
| **Terminal-Bench Hard** | Artificial Analysis (hosted) | Terminal/command-line multi-step debugging and system administration | Public benchmark |
| **APEX-Agents-AA** | Artificial Analysis (hosted) | Agentic capability benchmark measuring multi-step task completion | Public benchmark |

These datasets are used in this report as the **primary independent evidence** for GPT-5.5's intelligence ranking, knowledge accuracy, and hallucination rate (Chapter 5.1) and for cross-competitor comparison (Chapter 6).

### 3.1.2 User testing corpora (T5)

| Corpus | Author | Composition | Public availability |
|--------|--------|-------------|---------------------|
| Berman test set | Matthew Berman | Benchmark interpretation + targeted hands-on tasks (UI inspection, Box AI integration) | YouTube video + cited OpenAI figures |
| Ben Davis test set (two rounds) | Ben Davis | Four weeks of Early Access use; UI/front-end tasks, Pi-harness workflows, X-High autonomous runs, worktree parallelization | YouTube videos with partial prompt disclosure |
| Independent technical review comparison set | an independent technical review | Head-to-head GPT-5.5 vs Gemini 3.5 Flash tests: front-end design (3 scenarios), reasoning (OCR, prediction), context (haystack), writing (300-word constraint) | industry technical article with full prompts and outputs |
| TechnicalAnalysis-C coding test | TechnicalAnalysis-C (industry technical press) | File-upload security coding task: GPT-5.3 vs GPT-5.5 comparison; math convergence analysis | industry technical article with prompts and code outputs |
| Wes Roth industry test | Wes Roth | UI layout generation, Codex integration demo | YouTube video |
| TechnicalAnalysis-E demonstration set | TechnicalAnalysis-E (Industry technical analysis) | Codex demos (Artemis II 3D web app, dungeon arena); basic physics/visualization tasks | industry technical article |

**Inclusion criterion**: A T5 source is included only if the prompts are documented in the source (not merely summarized). Sources that only cite vendor benchmark numbers without showing prompts are excluded from the failure-case aggregation but retained for context-setting.

### 3.1.3 Vendor datasets (T6)

| Dataset | Vendor | Composition | Verification status |
|--------|--------|-------------|---------------------|
| OpenAI GPT-5.5 launch benchmark suite | OpenAI | Terminal-Bench 2.0, SWE-Bench Pro, Expert-SWE, GDPval, OSWorld-Verified, CyberGym, BrowseComp, Tau2 Telecom, FrontierMath Tier 1–3 | **Vendor-reported; partial T3 verification only** |
| OpenAI Preparedness Framework evaluations | OpenAI | Internal + external red-team testing; ~200 real-world safety scenarios | **Vendor assertion only** |
| OpenAI Bio Bug Bounty findings | OpenAI | External researcher submissions, max reward $25,000 | **Program ongoing; no published findings as of report date** |
| OpenAI internal usage metrics | OpenAI | "85% of OpenAI employees use Codex weekly"; team coverage | **Vendor assertion; no independent audit** |

T6 datasets are cited in this report **only** as "vendor-reported, pending independent verification" and never as primary evidence for any conclusion.

## 3.2 Dataset Composition Statistics

### 3.2.1 Aggregate benchmark coverage

Counting unique benchmark evaluations cited in this report:

| Capability dimension | # of distinct benchmarks cited | T3 verification coverage |
|---------------------|:------------------------------:|--------------------------|
| Factual reasoning / knowledge | 3 (AA-Omniscience, GDPval-AA, FrontierMath) | 2 of 3 independently verified |
| Code generation | 4 (Terminal-Bench Hard, SWE-Bench Pro, Expert-SWE, AA code-execution comparison) | 1 of 4 independently verified (Terminal-Bench Hard) |
| Long-context understanding | 1 (long-context needle-in-haystack via T5) | 0 of 1 independently verified |
| Multi-turn instruction following | 2 (τ²-Bench Telecom, AA instruction-following) | 1 of 2 independently verified |
| Generation consistency / stability | 0 | Not covered |
| Agentic / tool use | 2 (APEX-Agents-AA, MCP Atlas) | 1 of 2 independently verified |
| Multimodal / vision | 2 (MMMU-Pro, Visual Inspection) | 0 of 2 independently verified |
| Safety | 3 (CyberGym, gore/sexual filtering, jailbreak) | 0 of 3 independently verified |

**Key observation**: Independent (T3) verification is **concentrated in cognitive/agentic dimensions**. Safety, multimodal, and long-context dimensions have **no independent T3 verification** in this report's source set — a limitation disclosed in Chapter 11.

### 3.2.2 Failure-case corpus composition

Failure cases aggregated from T5 sources meeting the inclusion criteria in Section 2.4:

| Failure type | # of cases | Sources |
|--------------|:----------:|---------|
| Type A — Factual error / hallucination | 2 (AA-Omniscience aggregate + a regional university OCR) | S11 (T3 aggregate), S8 (T5 specific) |
| Type B — Instruction drift | 3 (300-word sci-fi story, math convergence, computer-use permission scope) | S8, S7, S3 (all T5) |
| Type C — Consistency failure | 1 (effort-level reversal of conclusions) | S3 (T5) |
| Type D — Long-context degradation | 2 (compaction regression, haystack test) | S2 (T5), S8 (T5) |
| Type E — Over-refusal | 0 documented cases in source set | — |

Total: **8 distinct failure cases** meeting inclusion criteria. This is a small corpus; it is **not** a statistically representative sample and is presented in Chapter 7 as illustrative cases, not as a systematic failure-rate measurement.

## 3.3 Contamination Controls

A core methodological concern is whether public benchmark figures reflect training-data contamination. OpenAI has not published contamination controls for GPT-5.5's training set. This report addresses contamination risk through the following measures:

1. **Preference for independent re-hosted benchmarks.** Where Artificial Analysis re-hosts or re-executes a benchmark (e.g., GDPval-AA, Terminal-Bench Hard, APEX-Agents-AA), this report cites the AA variant rather than the OpenAI-published variant, on the grounds that AA's versioning and methodology are independently documented.
2. **Flagging of potentially contaminated benchmarks.** Where the only available data is OpenAI's self-reported score on a public benchmark (e.g., BrowseComp, Tau2 Telecom, FrontierMath), the figure is flagged with "vendor-reported; contamination controls not disclosed."
3. **Reliance on T5 failure cases with novel prompts.** The failure cases in Chapter 7 use prompts that the practitioner authors invented (e.g., the independent technical review's "a regional university logo" OCR test, the "300-word sci-fi story" constraint), reducing contamination likelihood.

This report does **not** claim that contamination is absent. The absence of OpenAI-published contamination controls is itself a finding (Chapter 11).

## 3.4 Data Quality Control

For T5 user testing sources, the following quality controls were applied during aggregation:

- **Prompt reproducibility**: Only sources with full prompt text are included in failure-case aggregation
- **Output documentation**: Only sources with full model output text are included
- **Cross-validation**: Where two independent T5 sources tested similar capabilities, the report notes convergence or divergence
- **Practitioner disclosure**: Author identity and publication date are documented for each T5 source

For T3 sources, the report relies on Artificial Analysis's own published methodology, which is publicly accessible at artificialanalysis.ai.

## 3.5 Open-Access Declaration

- **T3 source data**: Publicly accessible at artificialanalysis.ai; this report provides URLs in each chapter
- **T5 source data**: Publicly accessible via YouTube video URLs and industry technical article URLs; full prompt/output text is reproduced in Chapter 7 where directly relevant
- **T6 source data**: OpenAI's launch announcement, system card, and Preparedness Framework documentation are publicly accessible; specific URLs are provided in each citation
- **Aggregation scripts**: Not applicable — this report does not run new code; it synthesizes published figures
- **Source-tier classification table**: Publicly available in `reports-md/outline-reference.md`

Per `summary-white-paper-focus.md` Section V (Feature C: Reproducibility), this report does not introduce proprietary data. All cited evidence is traceable to public sources.

## 3.6 Sample Example Format

To illustrate the dataset format used in Chapter 7 (failure cases), an example entry:

```
Failure Case #1 — Multimodal OCR failure
Classification: Type A (factual error)
Source: an independent technical review, 2026-05-15 (T5)
Prompt: [Image of a regional university logo] "Identify this logo."
GPT-5.5 output: [Did not recognize / incorrect identification]
Gemini 3.5 Flash output: [Correctly identified as a regional university]
Expected output: "a regional university"
Methodology note: Both models tested under default settings; no temperature specified.
```

The full set of failure cases with prompts and outputs is presented in Chapter 7 (`07-failure-cases.md`).

## 3.7 Dataset Card Summary

Following the Hugging Face Dataset Card format, the aggregated dataset used by this report has the following characteristics:

- **Dataset name**: GPT-5.5 Independent Evaluation Synthesis Corpus (2026-04 to 2026-07)
- **Composition**: 3 T3 independent benchmarks + 6 T5 user test corpora + 4 T6 vendor datasets (only used for cross-validation, not as primary evidence)
- **Language coverage**: English (Berman, Ben Davis, Wes Roth, AA) + additional industry technical analyses (TechnicalAnalysis-A through E, independent technical review)
- **Time coverage**: 2026-04-20 to 2026-05-28 (source publication dates)
- **Quality control**: Inclusion criteria per Section 2.4; T5 sources with undocumented prompts excluded from failure-case corpus
- **Known biases**: English-language over-representation in failure cases; vendor benchmarks over-represented in headline numbers; no T1/T2/T4 source coverage
- **Update policy**: Static as of 2026-07-12; future model updates will require a new version

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/ — **T3 dataset source**
2. an independent technical review. "Gemini 3.5 Flash vs GPT-5.5: a hands-on comparison." 2026-05-15. URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5 — **T5 failure-case corpus**
3. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04. — **T5 practitioner test set**
4. Ben Davis. "I was wrong about GPT 5.5." YouTube. 2026-05-28. — **T5 effort-level test set**
5. Matthew Berman. "OpenAI just dropped GPT-5.5.. (WOAH)." YouTube. 2026-04-23. — **T5 launch-day benchmark interpretation**
6. OpenAI. "GPT-5.5 launch announcement and system card." 2026-04-23. — **T6 vendor benchmark suite**
7. `white-paper-research/summary-white-paper-focus.md` — citation standards (Dataset Card reference)
