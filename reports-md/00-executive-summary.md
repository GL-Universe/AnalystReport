# GPT-5.5 Model Service Evaluation White Paper — Executive Summary

> **Evaluation subject**: OpenAI GPT-5.5 (model service layer, API + ChatGPT interface)
> **Benchmark competitors**: Claude Opus 4.7 (Anthropic), Gemini 3.1 Pro / 3.5 Flash (Google), DeepSeek-V4 (DeepSeek)
> **Draft date**: 2026-07-12

---

## Independence Declaration

This report is an independent evaluation research synthesis with no commercial affiliation with OpenAI, Anthropic, Google, DeepSeek, or any other AI model vendor evaluated herein. No AI company provided financial support, computing resources, or pre-release access for this research. The author holds no equity in and has no consulting relationship with any company whose product is evaluated.

Evaluation evidence is drawn from three categories of source: independent third-party measurements (primarily Artificial Analysis), practitioner testing reports (independent benchmark runs and hands-on evaluations), and vendor-published benchmark claims (always labeled as vendor-reported and cross-checked against independent measurements wherever possible).

Funding source: [Institution Name to be inserted before publication]. Conflict of interest declaration: see Appendix A. All cited sources are publicly accessible; URLs and references are provided in each chapter's reference list.

---

## Methodology Positioning

This white paper is a **meta-analysis and cross-validation** of publicly available evaluation evidence as of July 2026. The author did not execute a new 5,000-prompt API test campaign. Instead, the report synthesizes:

- **Independent measurements** (Artificial Analysis): AA Intelligence Index, AA-Omniscience, GDPval-AA
- **Practitioner testing reports**: documented benchmark runs and hands-on evaluations by independent practitioners (Berman, Ben Davis, Wes Roth, and additional industry technical reviewers)
- **Vendor-reported benchmark claims**: OpenAI's published benchmark scores and system card assertions, *always labeled as vendor-reported and cross-checked against independent measurements*

The original research plan called for a 5,000-prompt primary API test campaign; this report instead applies a meta-analysis methodology that synthesizes existing independent measurements and explicitly identifies which findings rest solely on vendor-reported figures. Chapter 11 (Limitations) quantifies the resulting evidence gaps.

---

## Key Findings

### Finding 1 — Intelligence Index ranking, independently verified

In the Artificial Analysis Intelligence Index — an independent third-party benchmark aggregating multiple cognitive tasks — GPT-5.5 scored **3 points higher** than the previous three-way tie among Anthropic, Google, and OpenAI flagships (Artificial Analysis, 2026).

On GDPval-AA, a 44-profession real-work evaluation hosted by Artificial Analysis, GPT-5.5 (xhigh) achieved **1,785 Elo**, approximately 30 points ahead of Claude Opus 4.7 (Max) and 470 points ahead of Gemini 3.1 Pro Preview (Artificial Analysis, 2026).

### Finding 2 — Cost-efficiency lead at the Medium reasoning tier

At the **Medium** reasoning-effort setting, GPT-5.5 matched the intelligence of Claude Opus 4.7 (Max) at approximately **one quarter the cost** (~$1,200 vs ~$4,800 to run the AA Intelligence Index). GPT-5.5 (Low) approximated Claude Opus 4.7 (Non-reasoning, High) at approximately **one half the cost** (~$500 vs ~$1,000) (Artificial Analysis, 2026).

Across the full AA Intelligence Index, GPT-5.5 used **~40% fewer output tokens** than GPT-5.4 to reach the same score, absorbing most of the 2× per-token price increase. The net cost of running the Index rose by only **~20%**, and GPT-5.5 remained approximately **30% cheaper** than Claude Opus 4.7 (Max) (Artificial Analysis, 2026).

### Finding 3 — Most severe weakness: hallucination rate

In the AA-Omniscience benchmark — which jointly measures knowledge recall and hallucination tendency — GPT-5.5 (xhigh) exhibited a **hallucination rate of 86%**, compared with **36% for Claude Opus 4.7 (Max)** and **50% for Gemini 3.1 Pro Preview** (Artificial Analysis, 2026). GPT-5.5 simultaneously achieved the **highest knowledge accuracy at 57%** across all tested models.

The interpretation: GPT-5.5 is more likely to produce a confident-sounding answer when uncertain, rather than declining to answer. This is the most consequential failure mode identified by independent measurement in this report.

### Finding 4 — Vendor-reported benchmarks not fully reproduced

OpenAI reported a cluster of headline benchmark scores at the GPT-5.5 launch (OpenAI, 2026):

| Benchmark | Vendor-reported score |
|-----------|---------------------|
| Terminal-Bench 2.0 | 82.7% |
| SWE-Bench Pro | 58.6% |
| Expert-SWE | 73.1% |
| GDPval | 84.9% |
| OSWorld-Verified | 78.7% |
| CyberGym | 81.8% |
| BrowseComp | 84.4% |
| Tau2 Telecom | 98.0% |
| FrontierMath Tier 1–3 | 51.7% |

These figures have **not been independently reproduced at the same magnitudes** by independent measurement institutions as of the report date. Artificial Analysis confirmed GPT-5.5's leading position on Terminal-Bench Hard, GDPval-AA, and APEX-Agents-AA, but Gemini 3.1 Pro Preview led GPT-5.5 in **three additional evaluations** that AA hosts (Artificial Analysis, 2026). All vendor-reported figures in this report are flagged as "OpenAI-reported, pending independent verification."

### Finding 5 — Specific failure modes documented by user testing

Independent user testing (Berman, 2026; an independent technical review, 2026) documented the following failure cases with full prompt-output evidence:

- **Multimodal OCR failure**: GPT-5.5 failed to recognize a regional university logo where Gemini 3.5 Flash succeeded (independent technical review, 2026).
- **Instruction-following failure on creative writing**: When asked for a 300-word sci-fi short story, GPT-5.5 produced 450–500 words, wrote a spy thriller instead of sci-fi, and handled the constraint "the male protagonist cannot speak" by literally hanging a "no speaking allowed" sign on him (independent technical review, 2026).
- **Long-context degradation**: Independent practitioner Ben Davis reported that GPT-5.5's context compaction is weaker than GPT-5.4, recommending thread length be kept under 100K tokens even though the API advertises a 400K–1M token window (Ben Davis, 2026).
- **Safety filter regression in GPT-5.5 Instant**: OpenAI's own system card reports gore-content filtering regressed from 0.867 to 0.703 and sexual-content filtering from 0.857 to 0.806 (lower is better); jailbreak resistance also regressed (OpenAI, 2026; industry technical press, 2026).

### Finding 6 — Safety rating raised to "High" for the first time

Under OpenAI's own Preparedness Framework, GPT-5.5 is the first OpenAI model rated **"High" risk** in the Cybersecurity and biological/chemical domains (OpenAI, 2026). OpenAI concurrently launched a Bio Bug Bounty program with a **$25,000** maximum reward (OpenAI, 2026). These ratings are vendor self-assessments and are not independently verified by independent measurement or regulatory sources in this report.

---

## Vendor Claim vs. Independent Verification Summary

| Claim by OpenAI (vendor-reported) | Independent verification status |
|----------------------|--------------------------------|
| Leading model on launch benchmarks | **Partially verified** — AA Intelligence Index lead confirmed (Artificial Analysis, 2026); 3 benchmarks led by Gemini 3.1 Pro Preview instead |
| 20–40% token efficiency improvement | **Verified** — AA measured ~40% fewer output tokens at equal Index score (Artificial Analysis, 2026) |
| Net cost increase only ~20% despite 2× price | **Verified** — AA measured ~+20% net cost on Intelligence Index (Artificial Analysis, 2026) |
| Safest generation to date | **Contested** — OpenAI's own system card reports safety filter regressions on gore/sexual/jailbreak (OpenAI, 2026); independent safety testing not yet available |
| First "High" Preparedness risk rating | **Vendor assertion only** — no independent government body or third-party institution has confirmed this rating in the source set |
| Hallucination reduced 52.5% in high-risk domains (GPT-5.5 Instant) | **Vendor assertion only** — Artificial Analysis independently measures GPT-5.5 (xhigh) hallucination rate at 86%, the highest among tested frontier models (Artificial Analysis, 2026; contradiction under investigation) |

---

## What This Report Does Not Claim

- This report does **not** claim GPT-5.5 is "the best model" in absolute terms. It claims GPT-5.5 achieved the highest score on a specific independent index (AA Intelligence Index) at the time of writing.
- This report does **not** use OpenAI's own benchmark figures as primary evidence. They are cited only as vendor claims and contrasted with independent measurements.
- This report does **not** omit competitor advantages: Gemini 3.1 Pro Preview leads GPT-5.5 on three AA-hosted evaluations, leads on MMMU-Pro (83.6% vs 81.2%) and MCP Atlas (83.6% vs 75.3%) per vendor-reported data, and is cheaper at matched intelligence (~$900 vs ~$1,200).
- This report does **not** conclude that GPT-5.5 is "safe" or "unsafe". It reports the measured regression values and the vendor's "High" rating, and notes the absence of independent government-body verification.

---

## Report Composition

The full white paper is structured into 13 chapter files:

| File | Chapter | Purpose |
|------|---------|---------|
| `00-executive-summary.md` | Ch 0 | Executive summary — key findings and evidence overview |
| `01-research-background.md` | Ch 1 | Why this report exists, industry context, research questions |
| `02-practical-recommendations.md` | Ch 2 | Decision tree by use case, deployment configurations |
| `03-methodology.md` | Ch 3 | Meta-analysis framework, source classification, cross-validation protocol |
| `04-evaluation-metrics.md` | Ch 4 | Definitions of intelligence, hallucination, cost, safety metrics |
| `05-core-capability-results.md` | Ch 5 | Reasoning, coding, long-context, multi-turn, stability findings |
| `06-competitor-comparison.md` | Ch 6 | Quantitative matrix vs Claude/Gemini/DeepSeek |
| `07-failure-cases.md` | Ch 7 | Hallucination, instruction drift, compaction, safety regression |
| `08-cost-effectiveness.md` | Ch 8 | API pricing, token efficiency, latency, cost-per-quality |
| `09-safety-alignment.md` | Ch 9 | Jailbreak, harmful content, privacy, regulatory compliance |
| `10-dataset-description.md` | Ch 10 | Public datasets and user-test corpora used |
| `11-limitations.md` | Ch 11 | Honest statement of evidence gaps |
| `12-appendix.md` | Ch 12 | COI, references, source-tier index |
