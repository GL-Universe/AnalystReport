# Chapter 11 — Research Limitations

## 11.1 Evidence-Gap Inventory

This report relies on a meta-analysis methodology (Chapter 3) rather than primary API testing. The following evidence gaps are quantified:

### 11.1.1 Evidence source coverage

| Source category | Available in source set? | Coverage |
|-----------------|:------------------------:|----------|
| Independent measurement institutions (Artificial Analysis, LMSYS, HELM) | Artificial Analysis only | Only one institution; no LMSYS or HELM GPT-5.5 data |
| Large-scale industry surveys (Harmonic Security, TrendForce, Omdia) | Partial | YouTube practitioners and industry technical press substitute; no formal large-scale industry survey |
| Vendor-published data (OpenAI) | Available | Used only as vendor claim, cross-validated by Artificial Analysis where possible |

**Critical implications of evidence coverage**:
- The **cost-effectiveness chapter (Chapter 8)** has only one independent measurement source (Artificial Analysis); cross-validation with a second institution would strengthen the findings.
- The **failure-case chapter (Chapter 7)** has only 8 cases meeting inclusion criteria. This is an illustrative corpus, not a systematic measurement.

### 11.1.2 Capability coverage gaps

| Capability dimension | Independent verification status | Specific gap |
|----------------------|:----------------------:|--------------|
| Factual reasoning / knowledge | ✅ 2 of 3 benchmarks verified | BrowseComp, FrontierMath not independently verified |
| Code generation | ⚠️ 1 of 4 benchmarks verified | SWE-Bench Pro, Expert-SWE not independently verified |
| Long-context understanding | Compaction regression is practitioner testing only | No independent benchmark |
| Multi-turn instruction following | ⚠️ 1 of 2 verified | τ²-Bench Telecom relative improvement verified; absolute 98% not reproduced |
| Agentic / tool use | ⚠️ 1 of 2 verified | APEX-Agents-AA verified; MCP Atlas not independently verified |
| Multimodal / vision | MMMU-Pro, Visual Inspection are vendor-reported only | 0 of 2 independently verified |

### 11.1.3 Source language coverage

- Practitioner testing sources: 4 YouTube practitioner evaluations (Berman, Ben Davis ×2, Wes Roth), 1 industry newsletter with regional context (Latent Space), 1 industry observer (EveryTo)
- Independent measurement sources: English (Artificial Analysis)
- **Under-represented languages**: No source in the set evaluates GPT-5.5 in French, German, Spanish, Arabic, Japanese, Korean, or other languages beyond English and the additional industry technical sources
- **Implication**: Findings about GPT-5.5's behavior in non-English contexts are extrapolations; the report cannot make claims about multilingual performance beyond these two languages.

## 11.2 Methodological Limitations

### 11.2.1 No primary API testing

This report did not execute a new 5,000-prompt test campaign. The original research plan recommended this; the substitution is documented in Chapter 3 (Section 3.1). The methodological substitution has three consequences:

1. **Cannot reproduce vendor benchmarks**: This report cannot independently verify OpenAI's headline benchmark figures (e.g., Terminal-Bench 82.7%, SWE-Bench Pro 58.6%). It can only cross-reference them against independent relative-rankings (which confirm GPT-5.5's lead without reproducing the absolute magnitudes).
2. **Cannot establish causal claims**: This report cannot determine *why* GPT-5.5 hallucinates more than competitors (e.g., training data, RLHF choices, or model architecture). It can only document the measured rate.
3. **Cannot measure dimensions absent from existing sources**: For example, no source in the set measures GPT-5.5's output variance at fixed temperature, so this report cannot fill that gap.

### 11.2.2 Single independent measurement source dependency

For the most consequential findings in this report (Intelligence Index ranking, AA-Omniscience hallucination rate, GDPval-AA Elo, cost per Index run), **only one independent measurement institution is available: Artificial Analysis**. Cross-validation with a second independent source (LMSYS, Stanford HELM) is not possible within this report's source set. Findings resting on a single independent measurement source are more fragile than findings resting on multiple independent sources.

### 11.2.3 Effort-level specification incomplete in practitioner sources

Multiple practitioner sources do not specify the reasoning-effort level used in their tests. This report flags every GPT-5.5 citation with its effort level where specified (per Section 4.2), but practitioner sources with unspecified effort levels are inherently less reproducible.

### 11.2.4 Sampling parameters incomplete in practitioner sources

Practitioner sources typically do not specify temperature, top-p, or other sampling parameters. The report notes in Chapter 3 (Section 3.8) that unspecified parameters are flagged rather than assumed. Practitioners attempting to reproduce these findings may not be able to do so exactly because the underlying sampling configuration is not documented.

### 11.2.5 Time window narrow

- Vendor data cited: published 2026-04-23 through 2026-05-28
- Independent data cited: Artificial Analysis publication 2026-04-23; user testing between 2026-04-20 and 2026-05-28
- Report cutoff: 2026-07-12

GPT-5.5 is a live commercial product; OpenAI may update weights, system prompts, or safety filters at any time. Findings in this report are accurate as of source publication dates, not the report date. Any model update after the source publication dates is not reflected.

### 11.2.6 Inter-source convergence not always available

Where two independent practitioner sources converge on the same finding (e.g., compaction regression noted by both Ben Davis videos), this report notes the convergence as strengthening the finding. Where practitioner testing sources test different capabilities with different prompts, no convergence test is possible. The 8 failure cases in Chapter 7 are mostly single-source; only the compaction regression has inter-source convergence.

## 11.3 Specific Findings That Should Be Treated With Caution

The following findings are based on thinner evidence than others in the report and should be cited with appropriate hedging:

| Finding | Evidence base | Cautious citation form |
|---------|---------------|------------------------|
| Compaction regression vs GPT-5.4 | Single practitioner testing source (Ben Davis, 2026-05-04) | "Per Ben Davis (2026), GPT-5.5's compaction appears weaker than GPT-5.4; this report could not independently verify the regression." |
| Long-context practical usable range ~100K tokens | Single practitioner testing source (Ben Davis, 2026-05-04) | "Practitioner evidence suggests a practical context of approximately 100K tokens despite the advertised 400K–1M window." |
| Creative-writing constraint drift | Single practitioner testing source (an independent technical review, 2026-05-15), single prompt | "In one tested case, GPT-5.5 produced 50%+ over a 300-word limit and wrote in the wrong genre." |
| non-English multimodal OCR weakness | Single practitioner testing source (an independent technical review, 2026-05-15), single prompt | "GPT-5.5 failed on one tested regional institution logo where Gemini 3.5 Flash succeeded." |
| Peter's $1.3M/month API spend | Single practitioner testing source (Ben Davis, 2026-05-28), single case study | "One documented practitioner case reports $1.3M/month API spend on GPT-5.5 Pro (xhigh); no independent verification of the figure." |
| Ads platform CPC $3–5 / CPM $60 | Single practitioner testing source (TechnicalAnalysis-C, 2026-05-05) | "OpenAI's Ads platform reportedly charges $3–5 CPC and $60 CPM, approximately 3–4× Google Search rates, per industry technical press." |
| Claude workflow switching cost | Single practitioner testing source (EveryTo, 2026-04-30), partial paywalled | "Per one industry observer, users with deeply-integrated Claude workflows face switching costs in migrating to Codex-based GPT-5.5 workflows." |

## 11.4 Source-Bias Acknowledgment

### 11.4.1 YouTube practitioner source bias

YouTube practitioners (Berman, Ben Davis, Wes Roth) derive income from views and may have incentives to emphasize dramatic findings or reversals (e.g., Ben Davis's two videos published four weeks apart reach opposite conclusions about optimal effort level). This report mitigates this bias by:
- Citing full prompt/output where available (per inclusion criteria in Section 2.4)
- Noting inter-source convergence where it exists
- Flagging single-source findings per Section 11.3
- Cross-validating practitioner testing findings against Artificial Analysis (independent measurement institution) data wherever possible

### 11.4.2 industry technical press source bias

industry technical press sources are published on industry trade platforms and may have different editorial incentives than English-language sources (e.g., regional audience expectations, platform moderation policies). This report does not assume that independent technical sources have the same bias profile; it cites both with full attribution and lets the reader evaluate.

### 11.4.3 Artificial Analysis independence

Artificial Analysis is an independent evaluation institution. However, the report notes that OpenAI provided AA with "pre-release access to test all five reasoning-effort levels" (Artificial Analysis, 2026). This pre-release access is a standard industry practice but introduces a potential timing asymmetry: AA's evaluation was conducted before public release, which may affect certain dynamic behaviors (e.g., server load, system-prompt tuning) without affecting static model capabilities.

## 11.5 Reporting Limitations

### 11.5.1 No confidence intervals on vendor-reported benchmarks

OpenAI does not publish confidence intervals or variance estimates for its launch-day benchmarks (e.g., Terminal-Bench 82.7%, SWE-Bench Pro 58.6%). This report cites these figures as point estimates; the true values may vary. Where Artificial Analysis provides its own confidence statements, this report references AA's methodology page rather than reproducing specific interval values that may have changed since publication.

### 11.5.2 No inter-rater reliability for practitioner testing sources

Practitioner sources are typically single-author. No inter-rater reliability metric (e.g., Kappa) is available. This report treats practitioner testing findings as illustrative cases, not as systematic measurements. The small failure-case corpus (8 cases) in Chapter 7 is explicitly labeled as illustrative.

### 11.5.3 Cost data assumes list prices

All cost figures in Chapter 8 use vendor list prices. Enterprise agreements, volume discounts, and committed-use pricing can materially change the cost picture. No source in the set publishes enterprise-tier pricing. Practitioners should expect their actual costs to differ from list-price calculations.

## 11.6 What This Report Does Not Claim

- This report does **not** claim GPT-5.5 is "the best model" — only that it scored highest on a specific independent index (AA Intelligence Index) at the time of writing
- This report does **not** claim GPT-5.5 is "safe" or "unsafe" — only that specific safety metrics have specific values from specific sources
- This report does **not** claim its recommendations in Chapter 2 are universal — they are conditional on use case, deployment context, and user tolerance for hallucination
- This report does **not** claim that vendor-reported benchmarks are false — only that they are not independently reproduced at the same magnitudes in this report's source set

## 11.7 Update Policy

This report is a **snapshot** as of 2026-07-12. If significant new evidence becomes available (e.g., a second independent measurement institution cross-validates Artificial Analysis's findings; OpenAI publishes updated benchmarks), this report should be updated with a new version. The current version remains citable as a point-in-time assessment of evidence available up to 2026-07-12.

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/
2. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04.
4. EveryTo (Laura Entis). "Who Isn't Using GPT 5.5." 2026-04-30. URL: https://every.to/context-window/who-isnt-using-gpt-55
