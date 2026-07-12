# Chapter 2 — Evaluation Methodology

## 2.1 Methodological Positioning

This white paper does **not** present newly self-executed API tests of GPT-5.5. The chapter outline (`GPT5.5outline.md`) recommended a 5,000-prompt independently designed test campaign; this report substitutes a **meta-analysis and cross-validation** of independent third-party measurements (T3), user testing reports (T5), and vendor-published data (T6). The substitution is motivated by:

1. **Reproducibility.** Independent T3 measurements by Artificial Analysis were already executed with documented methodology (AA Intelligence Index, AA-Omniscience, GDPval-AA) at the time of writing (Artificial Analysis, 2026, T3). Re-running similar tests would not produce additional signal for journalists citing this report.
2. **Independence preservation.** The author has no API access relationship with OpenAI that would permit standardized 5,000-prompt runs at the time of writing. Claiming to have executed such runs without transparent access would itself violate the independence principle in `summary-white-paper-focus.md` Section VIII.
3. **Cross-validation focus.** The highest-value contribution this report can make is to systematically contrast vendor-reported figures (T6) with independently measured ones (T3), and to surface failure cases documented by practitioners (T5) that standard benchmarks miss.

The methodological approach is therefore: **systematic source-tiering + cross-tier contradiction detection + failure-case aggregation**. This is a weaker methodology than the outline's recommended primary measurement, and Chapter 11 quantifies the resulting evidence gaps.

## 2.2 Source-Tier Classification

Each data point cited in this report is classified by source tier per `summary-white-paper-focus.md` Section II:

| Tier | Type | Source in this report | Citation marker |
|------|------|----------------------|-----------------|
| **T3** | Independent measurement institution | Artificial Analysis (AA Intelligence Index, AA-Omniscience, GDPval-AA) | "(AA, 2026, T3)" |
| **T5** | Large-scale user testing / industry analysis | YouTube practitioners, industry technical press, Latent Space | "(Berman, 2026, T5)", "(TechnicalAnalysis-A, 2026, T5)", etc. |
| **T6** | Vendor internal data | OpenAI-published benchmarks, system card, Preparedness Framework | "(OpenAI, 2026, T6)" |

**Tiers absent from this report**: T1 (Stanford AI Index, Pew Research), T2 (peer-reviewed academic journals), T4 (government/regulatory body evaluations). No GPT-5.5-specific publications from these tiers existed as of 2026-07-12. The absence is itself a finding (Chapter 11).

## 2.3 Cross-Tier Contradiction Detection Protocol

For each vendor-reported benchmark figure (T6), the report applies the following protocol:

1. **Locate any independent measurement** of the same capability from T3 sources.
2. **If T3 confirms** the T6 figure within 5 percentage points: mark as **"verified"**.
3. **If T3 partially confirms** (same direction, different magnitude): mark as **"partially verified"** and report both numbers.
4. **If T3 contradicts** (different direction, or T3 measurement exists but does not reproduce T6 figure): mark as **"contested"** and surface both numbers with the methodology difference noted.
5. **If no T3 measurement exists**: mark as **"vendor assertion only"** and do not use as primary evidence for any conclusion.

This protocol is applied in Chapter 0 (Executive Summary's vendor-claim vs. independent-verification table) and in Chapters 5, 6, 7, 8, and 9 wherever a vendor-reported figure is cited.

## 2.4 Failure-Case Aggregation Method

Standard benchmarks (MMLU, SWE-Bench, etc.) report aggregate scores but rarely expose specific failure cases with full prompt-output evidence. This report aggregates failure cases from T5 user testing reports using the following inclusion criteria:

**Inclusion criteria** (all four required):
- (a) The full input prompt is documented in the source
- (b) The full model output is documented in the source
- (c) The expected output or correct answer is documented in the source
- (d) The source is independent (T5 or higher; not OpenAI-published)

**Classification scheme** (per `GPT5.5outline.md` Chapter 7):
- Type A — Factual errors / hallucination
- Type B — Instruction-understanding drift
- Type C — Consistency failures (contradictory outputs for identical inputs)
- Type D — Long-context degradation
- Type E — Over-refusal (legitimate requests rejected)

Each aggregated failure case is presented in Chapter 7 with the full prompt, the full model output, and a classification label.

## 2.5 Competitor Selection Rationale

Per `GPT5.5outline.md` Section 2.4 and the original outline's listed competitors:

| Competitor | Reason for inclusion | Source coverage |
|-----------|---------------------|-----------------|
| **Claude Opus 4.7** (Anthropic) | Same-generation flagship; primary intelligence benchmark rival | S11 (T3), S10 (T5+T3), S8 (T5) |
| **Gemini 3.1 Pro / 3.5 Flash** (Google) | Same-generation flagship; primary multimodal and tool-use rival | S11 (T3), S8 (T5), S10 (T5) |
| **DeepSeek-V4 Preview** (DeepSeek) | Open-weight rival released the same day; cost-pricing reference | S10 (T5) |
| **Mistral Large 2** | Outlined in `GPT5.5outline.md` but excluded due to insufficient source coverage in references | — |

Note: The outline (`GPT5.5outline.md`) listed Mistral Large 2 as a comparator, but no reference source in `reference/` evaluated Mistral against GPT-5.5. This report excludes Mistral rather than fabricate comparison data. Chapter 11 notes this exclusion as a coverage limitation.

## 2.6 Reasoning-Effort Ladder Treatment

A methodological novelty introduced by GPT-5.5 is the **five-level reasoning-effort ladder**: xhigh / high / medium / low / non-reasoning (OpenAI, 2026, T6; Artificial Analysis, 2026, T3). This means GPT-5.5 is effectively **five different models** depending on the configured effort level.

Artificial Analysis is the only T3 source that tested all five levels (Artificial Analysis, 2026, T3). This report:

1. **Always specifies the reasoning-effort level** when citing any GPT-5.5 figure (e.g., "GPT-5.5 (xhigh)" vs "GPT-5.5 (Medium)").
2. **Treats different effort levels as distinct data points** in cross-tier comparison.
3. **Does not aggregate across effort levels** without explicit weighting disclosure.

Practitioner reports (Ben Davis, 2026, T5) demonstrate that conclusions about GPT-5.5's suitability can reverse entirely depending on the effort level selected. The author's first video recommended low/no-reasoning for UI/design work; the author's second video reversed this position after testing X-High on autonomous workflows (Ben Davis, 2026, T5). This methodological dependence on effort-level specification is a core finding of this report and a critical caveat for any benchmark cited without an effort-level label.

## 2.7 Time Window

- **Vendor data cited**: published 2026-04-23 (GPT-5.5 launch) through 2026-05-28 (last Ben Davis follow-up video).
- **Independent data cited**: Artificial Analysis publication 2026-04-23; user testing reports between 2026-04-20 (Wes Roth) and 2026-05-28 (Ben Davis).
- **Report cutoff**: 2026-07-12. Any model update released after this date is not reflected.

GPT-5.5 is a live commercial product; OpenAI may update its weights, system prompts, or safety filters at any time. Figures in this report are accurate as of the source publication dates, not the report date.

## 2.8 Red Lines Observed in This Chapter

Per `GPT5.5outline.md`:

- ❌ Did not use API playground subjective impressions as evidence — all T5 sources cited have documented prompts and outputs
- ❌ Did not call any sample size "systematic evaluation" below 500 — where T5 sources test fewer than 500 items, they are labeled as "illustrative case studies" rather than systematic evaluations
- ❌ Did not omit temperature / sampling parameters — where parameters are specified in the source, they are reported; where they are not specified, this is flagged

## 2.9 What This Methodology Cannot Establish

Honest disclosure of methodology limits (expanded in Chapter 11):

- This report **cannot** reproduce OpenAI's vendor-reported benchmarks through primary measurement
- This report **cannot** establish causal claims about why GPT-5.5 hallucinates more than competitors — it can only document the measured rate
- This report **cannot** evaluate any capability that no T3 or T5 source tested (e.g., non-English-language specialized tasks underrepresented in reference sources)
- This report **cannot** verify OpenAI's "High" Preparedness rating through T4 government evaluation, because no T4 evaluation has been published

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/ — **T3 methodology reference**
2. OpenAI. "GPT-5.5 system card and Preparedness Framework assessment." 2026-04-23. — **T6 vendor methodology**
3. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04. — **T5 effort-level methodology demonstration**
4. Ben Davis. "I was wrong about GPT 5.5." YouTube. 2026-05-28. — **T5 effort-level reversal case**
5. an independent technical review. "Gemini 3.5 Flash vs GPT-5.5: a hands-on comparison." 2026-05-15. URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5 — **T5 failure-case methodology source**
6. `white-paper-research/summary-white-paper-focus.md` — citation standard reference
7. `reports-md/GPT5.5outline.md` — chapter outline reference
8. `reports-md/outline-reference.md` — source-to-chapter mapping reference
