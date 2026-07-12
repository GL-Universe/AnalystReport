# Chapter 12 — Appendix

## Appendix A — Conflict of Interest (COI) Declaration

```
This report is an independent evaluation research synthesis.
The author has no commercial affiliation with OpenAI, Anthropic, Google, DeepSeek, or any
other AI model vendor.
No AI company provided financial support, computing resources, or pre-release access for this research.
The author has no equity position in any company whose product is evaluated in this report.
The author has no consulting relationship with any company whose product is evaluated in this report.
Funding source: [Institution Name to be inserted before publication].
Methodology and original data: all cited sources are publicly accessible; URLs are provided in each
chapter's "References for This Chapter" section.
```

Per `summary-white-paper-focus.md` Section VIII, this declaration is mandatory. Omission would cause BBC to mark the report as "company claims...".

## Appendix B — Evaluation Metrics Scoring Rubric

The scoring rubric used by Artificial Analysis (the T3 source relied on in this report) is published at the AA methodology page. This report references the AA rubric rather than reproducing it, because:

1. The AA rubric may be updated independently of this report
2. The AA methodology page is the authoritative source for current scoring rules
3. Reproducing the rubric here risks divergence from the current AA methodology

For the failure-case aggregation methodology (Chapter 7), the rubric is documented in Chapter 2 (Section 2.4) of this report and consists of:

- Inclusion criteria: full prompt, full output, expected output, independent source
- Classification scheme: Type A (hallucination), Type B (instruction drift), Type C (consistency failure), Type D (long-context degradation), Type E (over-refusal)
- Reporting format: source citation, prompt, output, expected output, analysis

## Appendix C — Test Prompt Sample (Publicly Disclosed Part)

This report does not introduce new test prompts. It aggregates prompts documented in the source set. The most fully-documented prompts are reproduced below for reference.

### C.1 Creative writing constraint test (an independent technical review, 2026, T5)

```
Prompt: Write a 300-word science fiction short story. The male protagonist cannot speak.

GPT-5.5 output: [450-500 words, spy thriller genre, "no speaking allowed" sign on protagonist]
Gemini 3.5 Flash output: [~320 words, sci-fi genre, integrated narrative constraint]
Expected: A ~300-word sci-fi story with the "cannot speak" constraint integrated.
```

Source URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5

### C.2 regional institution logo OCR test (an independent technical review, 2026, T5)

```
Prompt: [Image of a regional university logo] "Identify this logo."

GPT-5.5 output: [Failed to identify / incorrect identification]
Gemini 3.5 Flash output: "a regional university" (correctly identified)
Expected: "a regional university"
```

Source URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5

### C.3 Needle-in-haystack test (an independent technical review, 2026, T5)

```
Prompt: [Full text of a long-form television script script with three anomalous commands embedded,
e.g., "the moon swallowed the key into the refrigerator". The model is asked to identify
any anomalous instructions.]

GPT-5.5 output: [Failed to identify all three anomalous commands]
Gemini 3.5 Flash output: [Also failed to identify the anomalous commands]
Expected: Identification of the three anomalous commands.
```

Source URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5

### C.4 File-upload security coding test (TechnicalAnalysis-C, 2026, T5)

```
Prompt: Implement a file-upload feature. Ensure security.

GPT-5.3 output: [Basic file-type checking only]
GPT-5.5 output: [UUID renaming, whitelist validation, size limits, MIME verification]
Expected: Engineering-grade file-upload security implementation.
```

Source URL: https://example.com/technical-analysis/gpt-5.5-free-tier-ads

## Appendix D — Evaluation Scripts

This report does not introduce new evaluation scripts. It synthesizes published evidence from:

- Artificial Analysis (T3) — AA's evaluation scripts are available at the AA website
- T5 sources — scripts not published in the source set

For practitioners wishing to reproduce the T5 tests, the prompts in Appendix C can be run against the model APIs directly. No additional scripts are required for the failure-case tests; the prompts are fully documented.

## Appendix E — Raw Score Data (Public Download Sources)

| Data type | Source | URL |
|-----------|--------|-----|
| AA Intelligence Index scores | Artificial Analysis | https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/ |
| AA-Omniscience scores | Artificial Analysis | (AA methodology page) |
| GDPval-AA Elo rankings | Artificial Analysis | (AA GDPval page) |
| Terminal-Bench Hard scores | Artificial Analysis | (AA Terminal-Bench page) |
| OpenAI launch benchmarks | OpenAI | (OpenAI GPT-5.5 announcement page) |
| OpenAI system card | OpenAI | (OpenAI system card PDF) |
| Ben Davis hands-on reports | YouTube | (URLs in each chapter's references) |
| Independent technical review head-to-head tests | industry technical article | https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5 |
| TechnicalAnalysis-A–5 analyses | industry technical article | (URLs in each chapter's references) |
| Latent Space analysis | Substack | https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp |
| EveryTo switching-cost article | Every.to | https://every.to/context-window/who-isnt-using-gpt-55 |

All cited evidence is traceable to public sources. This report does not introduce proprietary data.

## Appendix F — Evaluator Qualifications & Inter-Rater Reliability

This report aggregates existing measurements rather than running new human evaluations. Therefore:

- **T3 (Artificial Analysis)**: AA publishes its evaluator qualifications and inter-rater reliability metrics on its methodology page. Users of this report should consult AA's current methodology page for up-to-date inter-rater reliability values.
- **T5 (user testing reports)**: Typically single-author. No inter-rater reliability metric available. This report treats T5 findings as illustrative cases, not as systematic evaluations.
- **T6 (vendor)**: OpenAI's internal red-team qualifications are not publicly disclosed in this report's source set.

## Appendix G — Version History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 (draft) | 2026-07-12 | AnalystReport | Initial draft based on `GPT5.5outline.md` and `outline-reference.md` source mapping |

This is the first version of this report. Subsequent updates will be triggered by:

- Publication of T1 (Stanford AI Index, etc.) GPT-5.5-specific evaluations
- Publication of T2 (NeurIPS, ACL, arXiv) GPT-5.5-specific peer-reviewed papers
- Publication of T4 (NIST AI RMF, EU AI Office, UK AISI) GPT-5.5-specific regulatory evaluations
- OpenAI model updates (weight changes, system-prompt changes, safety filter changes)
- New T3 independent evaluations (LMSYS, Stanford HELM) cross-validating AA findings

## Appendix H — Reference List (Tier-Classified)

### H.1 T3 sources (independent measurement institutions)

1. **Artificial Analysis**. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23.
   URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/
   — Provides: Intelligence Index scores, AA-Omniscience (knowledge accuracy + hallucination rate), GDPval-AA Elo, Terminal-Bench Hard rankings, cost per Index run, reasoning-effort ladder analysis, cross-competitor comparisons.

### H.2 T5 sources (user testing reports and industry analysis)

1. **Berman, Matthew**. "OpenAI just dropped GPT-5.5.. (WOAH)." YouTube. 2026-04-23.
   — Provides: Launch-day benchmark interpretation, Visual Inspection improvement, GB200/GB300 co-design, Box AI integration.

2. **Ben Davis**. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04.
   — Provides: Four-week Early Access experience, compaction regression finding, Pi harness recommendation, 100K token practical limit, reasoning-mode selection guidance.

3. **Ben Davis**. "I was wrong about GPT 5.5." YouTube. 2026-05-28.
   — Provides: Computer Use automation, autonomous workflow with dangerous permissions, X-High reasoning justification, Peter's $1.3M/month case, Codex mobile integration.

4. **Wes Roth**. "OpenAI's GPT 5.5 is wild.." YouTube. 2026-04-20.
   — Provides: "Anthropic effect" industry analysis, NSA/Claude/Mythos defense context, Google Sergey Brin strike team, Elon Grok computer use.

5. **an independent technical review**. "Gemini 3.5 Flash vs GPT-5.5: a hands-on comparison." 2026-05-15.
   URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5
   — Provides: Head-to-head GPT-5.5 vs Gemini 3.5 Flash tests across four dimensions (front-end, reasoning, context, writing), full prompts and outputs, AA cost data citation.

6. **TechnicalAnalysis-A (industry technical press)**. "GPT-5.5 launch: a detailed analysis." 2026-04-23.
   URL: https://example.com/technical-analysis/gpt-5.5-launch-detailed
   — Provides: 9 core benchmark data table, known weaknesses (SWE-Bench Pro behind Claude, MCP Atlas behind competitors, HLE regression), Bio Bug Bounty.

7. **TechnicalAnalysis-B (industry technical press)**. "GPT-5.5 Instant: the first instant-tier model rated High." 2026-04-23.
   URL: https://example.com/technical-analysis/gpt-5.5-instant-high-rating
   — Provides: Hallucination -52.5% (high-risk domains, vendor-claimed), AIME 2025 81.2, Memory Sources, safety filter regressions (gore/sexual/jailbreak), Gmail integration.

8. **TechnicalAnalysis-C (industry technical press)**. "GPT-5.5 free tier launch, hands-on testing, and ads platform." 2026-05-05.
   URL: https://example.com/technical-analysis/gpt-5.5-free-tier-ads
   — Provides: OpenAI Ads platform pricing (CPC $3-5, CPM $60), coding security comparison (GPT-5.3 vs GPT-5.5), math convergence reasoning test.

9. **TechnicalAnalysis-E (Industry technical analysis)**. "GPT-5.5 in practice: hands-on evaluation for real workloads." 2026-04-23.
   URL: https://example.com/technical-analysis/gpt-5.5-in-practice
   — Provides: Evaluation paradigm shift analysis, GPT-4o→GPT-5.5 evolution, Codex demos (Artemis II, dungeon arena), 85% internal Codex usage.

10. **Latent Space**. "[AINews] GPT 5.5 and OpenAI Codex Superapp." 2026-04-22/23.
    URL: https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp
    — Provides: AA Intelligence Index cost data (GPT-5.5 Medium vs Opus 4.7 Max vs Gemini 3.1 Pro), Codex super-app strategy, DeepSeek-V4 same-day release, agent infrastructure analysis.

11. **EveryTo (Laura Entis)**. "Who Isn't Using GPT 5.5." 2026-04-30.
    URL: https://every.to/context-window/who-isnt-using-gpt-55
    — Provides: CTO→Anthropic IC career trend, GPT-5.5 one-week pulse check, Claude workflow switching cost (partial paywall).

### H.3 T6 sources (vendor internal data, used only as vendor claims)

1. **OpenAI**. "GPT-5.5 launch announcement and system card." 2026-04-23.
   — Provides: 9 benchmark scores, Preparedness Framework "High" rating (Cybersecurity, biological/chemical), Bio Bug Bounty $25,000, API pricing, context window (1M token Altman confirmation), 85% internal Codex usage.

2. **Anthropic**. "Claude Opus 4.7 model card and pricing." 2026.
   — Provides: Claude Opus 4.7 specifications (used as competitor reference).

3. **Google**. "Gemini 3.1 Pro Preview and 3.5 Flash launch and benchmarks." 2026.
   — Provides: Gemini specifications, MMMU-Pro scores, MCP Atlas scores, 4× speed advantage claim.

4. **DeepSeek**. "DeepSeek-V4 Preview release." 2026-04-23.
   — Provides: V4-Flash and V4-Pro specifications, MIT license, pricing ($0.14/$0.28 and $1.74/$3.48), 1M-token context window.

### H.4 Absent source tiers (evidence gaps)

| Tier | Specific source | Status |
|------|----------------|--------|
| T1 | Stanford AI Index 2026 | No GPT-5.5-specific publication as of 2026-07-12 |
| T1 | Pew Research AI report | No GPT-5.5-specific publication |
| T2 | NeurIPS / ACL / ICLR | No GPT-5.5 peer-reviewed paper as of report date |
| T2 | Nature / Science / JAMA | No GPT-5.5 peer-reviewed paper |
| T3 | LMSYS Chatbot Arena | No GPT-5.5-specific leaderboard data in source set |
| T3 | Stanford HELM | No GPT-5.5-specific evaluation in source set |
| T4 | NIST AI RMF evaluation | No GPT-5.5-specific evaluation published |
| T4 | EU AI Office | No GPT-5.5-specific evaluation published |
| T4 | UK AISI | No GPT-5.5-specific evaluation published |
| T5 | Harmonic Security / TrendForce / Omdia | No formal large-scale industry survey of GPT-5.5 in source set |

## Appendix I — Source-to-Chapter Cross-Reference

The source-to-chapter mapping is documented in `reports-md/outline-reference.md`. This appendix provides a quick reference for journalists seeking the source of a specific chapter's claims:

| Chapter | Primary source | Secondary source(s) |
|---------|---------------|----------------------|
| Ch0 Executive Summary | AA (T3) | OpenAI (T6), Berman (T5), independent technical review (T5), Ben Davis (T5), TechnicalAnalysis-E (T5) |
| Ch1 Research Background | TechnicalAnalysis-E (T5), Latent Space (T5) | OpenAI (T6), AA (T3), Wes Roth (T5), TechnicalAnalysis-C (T5) |
| Ch2 Methodology | AA (T3) | OpenAI (T6), Ben Davis (T5), independent technical review (T5) |
| Ch3 Dataset Description | AA (T3) | independent technical review (T5), Ben Davis (T5), Berman (T5), OpenAI (T6) |
| Ch4 Evaluation Metrics | AA (T3) | OpenAI (T6), Ben Davis (T5), independent technical review (T5), Latent Space (T5) |
| Ch5 Core Capability Results | AA (T3) | OpenAI (T6), Ben Davis (T5), independent technical review (T5), TechnicalAnalysis-A (T5), TechnicalAnalysis-C (T5), TechnicalAnalysis-E (T5), Latent Space (T5) |
| Ch6 Competitor Comparison | AA (T3), independent technical review (T5) | OpenAI (T6), Anthropic (T6), Google (T6), DeepSeek (T6), TechnicalAnalysis-A (T5), Ben Davis (T5), EveryTo (T5), Latent Space (T5) |
| Ch7 Failure Cases | AA (T3), independent technical review (T5), Ben Davis (T5), TechnicalAnalysis-C (T5) | Latent Space (T5) |
| Ch8 Cost-Effectiveness | AA (T3), independent technical review (T5), Latent Space (T5) | OpenAI (T6), Anthropic (T6), Google (T6), DeepSeek (T6), Ben Davis (T5), TechnicalAnalysis-C (T5), TechnicalAnalysis-E (T5) |
| Ch9 Safety & Alignment | OpenAI (T6), AA (T3), TechnicalAnalysis-B (T5) | TechnicalAnalysis-A (T5), Berman (T5), TechnicalAnalysis-C (T5), Ben Davis (T5) |
| Ch10 Practical Recommendations | AA (T3), Ben Davis (T5), independent technical review (T5) | TechnicalAnalysis-A (T5), TechnicalAnalysis-C (T5), Berman (T5), Latent Space (T5), EveryTo (T5), DeepSeek (T6) |
| Ch11 Limitations | (synthesis of all chapters' evidence gaps) | — |
| Ch12 Appendix | (this file) | — |

## Appendix J — Related Files in This Report

| File | Purpose |
|------|---------|
| `reports-md/GPT5.5outline.md` | Chapter outline (458 lines, the structural guide for this report) |
| `reports-md/outline-reference.md` | Source-to-chapter mapping (the meta-index that guided source selection) |
| `reports-md/00-executive-summary.md` | Chapter 0 |
| `reports-md/01-research-background.md` | Chapter 1 |
| `reports-md/02-methodology.md` | Chapter 2 |
| `reports-md/03-dataset-description.md` | Chapter 3 |
| `reports-md/04-evaluation-metrics.md` | Chapter 4 |
| `reports-md/05-core-capability-results.md` | Chapter 5 |
| `reports-md/06-competitor-comparison.md` | Chapter 6 |
| `reports-md/07-failure-cases.md` | Chapter 7 |
| `reports-md/08-cost-effectiveness.md` | Chapter 8 |
| `reports-md/09-safety-alignment.md` | Chapter 9 |
| `reports-md/10-practical-recommendations.md` | Chapter 10 |
| `reports-md/11-limitations.md` | Chapter 11 |
| `reports-md/12-appendix.md` | Chapter 12 (this file) |
| `white-paper-research/summary-white-paper-focus.md` | Citation standards reference (248 lines) |
| `reference/` directory | Source outlines and original transcripts (12 references) |

## Appendix K — Methodology Transparency Statement

Per `summary-white-paper-focus.md` Section VIII, the following methodology disclosures are made:

- **Data collection method**: Meta-analysis of publicly available evaluation evidence; no new API tests executed
- **Sample size**: 3 T3 datasets (AA-hosted); 8 failure cases aggregated from T5 sources; 12 reference articles
- **Time period**: Source publication dates range from 2026-04-20 to 2026-05-28; report cutoff 2026-07-12
- **Sampling parameters**: Varies by source; T5 sources often do not specify temperature/top-p; T3 (AA) uses documented fixed configuration
- **Limitations**: Documented in Chapter 11 (file `11-limitations.md`)
- **Confidence**: Where confidence intervals are available (T3), they are referenced from the source; where unavailable (T6, most T5), they are noted as absent
- **Inter-rater reliability**: Not applicable for T3 (AA publishes its own); not available for T5 (single-author)

---

*This appendix completes the white paper. The full report is structured into 13 chapter files (00 through 12), each independently citable. The author recommends that journalists cite specific chapters for specific claims rather than citing the report as a monolithic whole.*
