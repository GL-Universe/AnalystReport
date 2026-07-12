# Chapter 3 — Evaluation Methodology

## 3.1 Methodological Positioning

This white paper does **not** present newly self-executed API tests of GPT-5.5. The original research plan recommended a 5,000-prompt independently designed test campaign; this report substitutes a **meta-analysis and cross-validation** of independently published measurements, practitioner testing reports, and vendor-published data. The substitution is motivated by:

1. **Reproducibility.** Independent measurements by Artificial Analysis were already executed with documented methodology (AA Intelligence Index, AA-Omniscience, GDPval-AA) at the time of writing (Artificial Analysis, 2026). Re-running similar tests would not produce additional signal.
2. **Independence preservation.** The author has no API access relationship with OpenAI that would permit standardized 5,000-prompt runs at the time of writing. Claiming to have executed such runs without transparent access would itself violate the independence principle.
3. **Cross-validation focus.** The highest-value contribution this report can make is to systematically contrast vendor-reported benchmark figures with independently measured ones, and to surface failure cases documented by practitioners that standard benchmarks miss.

The methodological approach is therefore: **systematic source classification + cross-source contradiction detection + failure-case aggregation**. This is a weaker methodology than primary measurement, and Chapter 11 quantifies the resulting evidence gaps.

## 3.2 Source Classification

This report draws on three categories of source, each carrying a different level of evidential weight:

| Category | Description | Sources used in this report | Citation style |
|----------|-------------|----------------------------|----------------|
| **Independent measurement** | Third-party institutions running standardized evaluations with published methodology | Artificial Analysis (AA Intelligence Index, AA-Omniscience, GDPval-AA) | Author-year, e.g. "(Artificial Analysis, 2026)" |
| **Practitioner testing** | Independent practitioners and industry analysts conducting hands-on evaluations; typically smaller-scale, illustrative rather than systematic | YouTube practitioners, industry technical press, Latent Space | Author-year, e.g. "(Berman, 2026)", "(Ben Davis, 2026)" |
| **Vendor-reported data** | Benchmark figures and claims published directly by AI vendors; used only as stated assertions, not as primary evidence | OpenAI-published benchmarks, system card, Preparedness Framework | Author-year with explicit "vendor-reported" label, e.g. "(OpenAI, 2026)" |

## 3.3 Cross-Source Contradiction Detection Protocol

For each vendor-reported benchmark figure, the report applies the following protocol:

1. **Locate any independent measurement** of the same capability from independently published sources.
2. **If the independent measurement confirms** the vendor figure within 5 percentage points: mark as **"verified"**.
3. **If the independent measurement partially confirms** (same direction, different magnitude): mark as **"partially verified"** and report both numbers.
4. **If the independent measurement contradicts** the vendor figure: mark as **"contested"** and surface both numbers with the methodology difference noted.
5. **If no independent measurement exists**: mark as **"vendor assertion only"** and do not use as primary evidence for any conclusion.

This protocol is applied in Chapter 0 (Executive Summary's vendor-claim vs. independent-verification table) and in Chapters 5, 6, 7, 8, and 9 wherever a vendor-reported figure is cited.

## 3.4 Failure-Case Aggregation Method

Standard benchmarks (MMLU, SWE-Bench, etc.) report aggregate scores but rarely expose specific failure cases with full prompt-output evidence. This report aggregates failure cases from independent practitioner testing reports using the following inclusion criteria:

**Inclusion criteria** (all four required):
- (a) The full input prompt is documented in the source
- (b) The full model output is documented in the source
- (c) The expected output or correct answer is documented in the source
- (d) The source is independent (not OpenAI-published)

**Classification scheme**:
- Type A — Factual errors / hallucination
- Type B — Instruction-understanding drift
- Type C — Consistency failures (contradictory outputs for identical inputs)
- Type D — Long-context degradation
- Type E — Over-refusal (legitimate requests rejected)

Each aggregated failure case is presented in Chapter 7 with the full prompt, the full model output, and a classification label.

## 3.5 Competitor Selection Rationale

This report evaluates the following competitors against GPT-5.5:

| Competitor | Reason for inclusion | Primary sources |
|-----------|---------------------|----------------|
| **Claude Opus 4.7** (Anthropic) | Same-generation flagship; primary intelligence benchmark rival | Artificial Analysis, Ben Davis, Latent Space |
| **Gemini 3.1 Pro / 3.5 Flash** (Google) | Same-generation flagship; primary multimodal and tool-use rival | Artificial Analysis, independent technical review, Ben Davis |
| **DeepSeek-V4 Preview** (DeepSeek) | Open-weight rival released the same day; cost-pricing reference | Latent Space |

Note: Mistral Large 2 was considered as a comparator, but no reference source in the set evaluated Mistral against GPT-5.5. This report excludes Mistral rather than fabricate comparison data. Chapter 11 notes this as a coverage limitation.

## 3.6 Reasoning-Effort Ladder Treatment

A methodological novelty introduced by GPT-5.5 is the **five-level reasoning-effort ladder**: xhigh / high / medium / low / non-reasoning (OpenAI, 2026; Artificial Analysis, 2026). This means GPT-5.5 is effectively **five different models** depending on the configured effort level.

Artificial Analysis is the only independent measurement institution that tested all five levels (Artificial Analysis, 2026). This report:

1. **Always specifies the reasoning-effort level** when citing any GPT-5.5 figure (e.g., "GPT-5.5 (xhigh)" vs "GPT-5.5 (Medium)").
2. **Treats different effort levels as distinct data points** in cross-tier comparison.
3. **Does not aggregate across effort levels** without explicit weighting disclosure.

Practitioner reports (Ben Davis, 2026) demonstrate that conclusions about GPT-5.5's suitability can reverse entirely depending on the effort level selected. The author's first video recommended low/no-reasoning for UI/design work; the author's second video reversed this position after testing X-High on autonomous workflows (Ben Davis, 2026). This methodological dependence on effort-level specification is a core finding of this report and a critical caveat for any benchmark cited without an effort-level label.

## 3.7 Time Window

- **Vendor data cited**: published 2026-04-23 (GPT-5.5 launch) through 2026-05-28 (last Ben Davis follow-up video).
- **Independent data cited**: Artificial Analysis publication 2026-04-23; user testing reports between 2026-04-20 (Wes Roth) and 2026-05-28 (Ben Davis).
- **Report cutoff**: 2026-07-12. Any model update released after this date is not reflected.

GPT-5.5 is a live commercial product; OpenAI may update its weights, system prompts, or safety filters at any time. Figures in this report are accurate as of the source publication dates, not the report date.

## 3.8 Evidence Standards Observed

- Did not use subjective API playground impressions as evidence — all practitioner sources cited have documented prompts and outputs.
- Did not characterize any small-sample test as a systematic evaluation — sources testing fewer than 500 items are labeled as "illustrative case studies" rather than systematic evaluations.
- Did not omit temperature / sampling parameters — where parameters are specified in the source, they are reported; where they are not specified, this is flagged.

## 3.9 What This Methodology Cannot Establish

Honest disclosure of methodology limits (expanded in Chapter 11):

- This report **cannot** reproduce OpenAI's vendor-reported benchmarks through primary measurement
- This report **cannot** establish causal claims about why GPT-5.5 hallucinates more than competitors — it can only document the measured rate
- This report **cannot** evaluate any capability that no independent measurement or practitioner testing source tested (e.g., non-English-language specialized tasks underrepresented in reference sources)
- This report **cannot** verify OpenAI's "High" Preparedness rating through independent government-body evaluation, because no such evaluation has been published

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/
2. OpenAI. "GPT-5.5 system card and Preparedness Framework assessment." 2026-04-23.
3. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04.
4. Ben Davis. "I was wrong about GPT 5.5." YouTube. 2026-05-28.
