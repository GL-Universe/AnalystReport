# Chapter 9 — Safety & Alignment Assessment

> Per `GPT5.5outline.md` Section 9, this chapter is the most policy-sensitive part of the report. CNN and BBC's policy reporters prioritize AI safety content; this chapter determines whether the report is cited by policy journalists.

## 9.1 Jailbreak Resistance Testing

### 9.1.1 Vendor-reported jailbreak regression (T6)

OpenAI's own system card reports that **GPT-5.5 Instant exhibits regression in jailbreak resistance testing** (OpenAI, 2026, T6; cross-cited by TechnicalAnalysis-B, 2026, T5). Specific numerical values are not in this report's source set; OpenAI's framing is that stronger model capability expands the attack surface, requiring continuous improvement to maintain prior safety levels.

### 9.1.2 Independent (T3) jailbreak measurement

No independent third-party (T3) jailbreak evaluation of GPT-5.5 is available in this report's source set as of 2026-07-12. **No T4 government evaluation** (UK AISI, NIST AI RMF application, EU AI Office) of GPT-5.5 has been published as of the report date.

**Implication**: The jailbreak-resistance picture for GPT-5.5 rests entirely on vendor self-assessment (T6). This is a critical evidence gap; Chapter 11 quantifies it.

### 9.1.3 Comparison to Claude Opus 4.7 jailbreak resistance

No source in this report's reference set provides a head-to-head jailbreak resistance comparison between GPT-5.5 and Claude Opus 4.7. Anthropic's own system card for Claude Opus 4.7 is not in the source set. This report **does not claim** that GPT-5.5 is more or less jailbreak-resistant than Claude Opus 4.7; it notes only that the data is absent.

## 9.2 Harmful-Content Generation Rate

### 9.2.1 Vendor-reported safety filter rates (T6)

OpenAI's system card publishes safety filter rates for GPT-5.5 Instant using an **inverse-score convention**: lower scores indicate **more leakage** (i.e., worse safety). The reported values are:

| Category | GPT-5.3 Instant (predecessor) | GPT-5.5 Instant | Direction |
|----------|:-----------------------------:|:---------------:|:---------:|
| Gore content filtering | 0.867 | **0.703** | Regression (worse) |
| Sexual content filtering | 0.857 | **0.806** | Regression (worse) |
| Jailbreak resistance | (not specified) | Regression (worse) | Regression |

Source: OpenAI system card, 2026 (T6); cross-cited by TechnicalAnalysis-B, 2026-04-23 (T5).

**Interpretation**: On OpenAI's own internal safety metrics, GPT-5.5 Instant's safety filters are **measurably worse** than GPT-5.3 Instant's in at least two categories. These are vendor-reported regressions — OpenAI itself acknowledges them in its system card. Independent (T3) verification of these figures is not available in this report's source set.

### 9.2.2 Hallucination as a safety-adjacent concern (T3)

The AA-Omniscience hallucination rate of **86% for GPT-5.5 (xhigh)** (Artificial Analysis, 2026, T3) — vs 36% for Claude Opus 4.7 (Max) and 50% for Gemini 3.1 Pro Preview — is not a safety filter failure in the traditional sense. However, in regulated advisory contexts (medical, legal, financial), confidently-wrong outputs can cause harms comparable to unfiltered harmful content. The 86% rate is therefore a safety-adjacent concern documented in this chapter and cross-referenced from Chapter 7 (Section 7.3.1).

### 9.2.3 OpenAI's claimed counter-improvement: 52.5% hallucination reduction (T6)

OpenAI claims that GPT-5.5 Instant achieves a **52.5% reduction in hallucination rate in high-risk domains** (OpenAI, 2026, T6; TechnicalAnalysis-B, 2026, T5). This figure is **vendor-reported** and not independently verified by any T3 source in this report's set.

**Apparent contradiction**: OpenAI claims a 52.5% reduction in high-risk-domain hallucination for GPT-5.5 Instant (T6), while Artificial Analysis measures an 86% hallucination rate for GPT-5.5 (xhigh) on AA-Omniscience (T3). These figures are not directly comparable because:

- They measure different model variants (Instant vs xhigh)
- They use different definitions of "hallucination" (vendor's domain-specific high-risk subset vs AA's general knowledge corpus)
- They use different methodologies (vendor internal vs independent third-party)

**Implication**: The vendor's claim may be true on its specific measurement scope while the independent measurement reveals a broader weakness. This report cites both figures with their measurement scopes specified. A journalist citing this report should not collapse the two figures into a single contradiction; they are answers to different questions.

## 9.3 Privacy & Data Security

### 9.3.1 Memory Sources feature (T6)

GPT-5.5 Instant introduces a **Memory Sources** feature that transparently displays the origins of model memory, allowing users to view, edit, or delete specific memories (OpenAI, 2026, T6; TechnicalAnalysis-B, 2026, T5). This is a **positive privacy control** — it gives users granular visibility into what the model "knows" about them.

### 9.3.2 Gmail integration (T6, T5)

ChatGPT's memory system can now connect to a user's Gmail account, extracting context from emails to provide personalized responses (OpenAI, 2026, T6; TechnicalAnalysis-B, 2026, T5). Examples include remembering user projects, contacts, and events.

**Privacy implication**: The Gmail integration expands the data surface that ChatGPT can access. While Memory Sources (Section 9.3.1) provides user controls, the integration creates new privacy considerations:

- What email content is retained by OpenAI after the conversation ends?
- Does Gmail-integrated memory persist across sessions?
- What are the data-handling terms for enterprise users?

These questions are not answered in the source set. This report notes them as open privacy questions.

### 9.3.3 OpenAI Ads platform privacy implications (T5)

The OpenAI Ads platform (launched concurrently with GPT-5.5; see Chapter 8 Section 8.1.3) uses model memory of user preferences, interests, and projects to deliver targeted advertisements (TechnicalAnalysis-C, 2026, T5). This creates a structural incentive for the model to **collect and retain personalization data** that can be monetized through advertising.

**Privacy concern**: The advertising business model may conflict with privacy-preserving defaults. Free-tier users whose inference is ad-supported have a different privacy exposure profile than paid-tier users. This report notes this as a structural privacy concern but does not quantify it; no T3 or T4 source evaluates the Ads platform's privacy practices.

### 9.3.4 API data retention (T6)

OpenAI's published API privacy policy (not reproduced in detail in this report) addresses data retention for API calls. Specific terms are not in this report's source set. Enterprise deployment data-handling terms are similarly not in the source set. This report does **not** make claims about API data retention; it notes the absence of independent privacy auditing as a limitation (Chapter 11).

## 9.4 Regulatory Compliance

### 9.4.1 EU AI Act classification (T4 absent)

No EU AI Office evaluation of GPT-5.5 has been published as of the report date. Under the EU AI Act's risk-tier framework, GPT-5.5's classification (limited risk, high risk, or prohibited) is not independently determined. OpenAI's own framing positions GPT-5.5 as a general-purpose AI model subject to transparency obligations; this is vendor positioning, not regulatory determination.

**Implication**: Enterprises deploying GPT-5.5 in EU jurisdictions should not rely on this report for EU AI Act compliance guidance. Consult the EU AI Office's publications and legal counsel.

### 9.4.2 NIST AI RMF (T4 absent)

No NIST AI Risk Management Framework evaluation of GPT-5.5 has been published as of the report date. OpenAI has not published a NIST AI RMF-aligned assessment of GPT-5.5 in this report's source set.

**Implication**: U.S. enterprises deploying GPT-5.5 should not rely on this report for NIST AI RMF compliance guidance. Consult NIST publications and internal risk governance.

### 9.4.3 UK AISI (T4 absent)

No UK AI Safety Institute evaluation of GPT-5.5 has been published as of the report date. UK AISI's prior evaluations of frontier models (GPT-4o, Claude 3.5 Sonnet, etc.) are not in this report's scope; no GPT-5.5-specific UK AISI report is available.

### 9.4.4 OpenAI Preparedness Framework (T6)

OpenAI's own Preparedness Framework rates GPT-5.5 as **"High" risk** in two domains:

1. **Cybersecurity** — first OpenAI model rated High in this domain
2. **Biological / chemical capabilities** — High

Source: OpenAI, 2026-04-23 (T6); cross-cited by Matthew Berman, 2026-04-23 (T5); TechnicalAnalysis-A, 2026-04-23 (T5).

**Important framing**: This is a **vendor self-assessment**. The "High" rating is OpenAI's own classification under its own framework, not an independent government determination. The framework's scoring rubric is published by OpenAI but the specific evaluation inputs for GPT-5.5 are not fully transparent.

### 9.4.5 Bio Bug Bounty program (T6)

OpenAI launched a Bio Bug Bounty program with a **$25,000 maximum reward** for external researchers who identify biological-risk vulnerabilities in GPT-5.5 (OpenAI, 2026, T6; TechnicalAnalysis-A, 2026, T5). As of the report date, no published findings from this program are available in the source set.

**Interpretation**: The Bug Bounty is a positive transparency step — it invites external scrutiny of a specific risk domain. However, the program's design (reward structure, scope, eligibility) and any resulting findings are not yet independently reported.

## 9.5 Source-Tier Requirements for This Chapter

Per `GPT5.5outline.md` Section 9, this chapter should ideally cite:

- **T4 (mandatory)**: NIST AI RMF, EU AI Act text, UK AISI reports
- **T2 (recommended)**: arXiv/ACL papers on LLM safety evaluation
- **T3**: LMSYS or other independent safety testing data
- **T6 (restricted)**: OpenAI System Card — only as "vendor's original claim", contrasted with independent testing

**Status against requirements**:

| Required tier | Available in source set? | Implication |
|---------------|:-------------------------:|-------------|
| T4 (mandatory) | ❌ No GPT-5.5-specific government evaluation | Chapter cannot satisfy mandatory T4 requirement; flagged in Chapter 11 |
| T2 (recommended) | ❌ No peer-reviewed academic paper on GPT-5.5 | Expected 3–6 month lag; flagged in Chapter 11 |
| T3 | ❌ No independent safety benchmark in source set | Critical evidence gap |
| T6 (restricted) | ✅ OpenAI System Card data | Used only as vendor claim, contrasted with AA hallucination data (T3) |

This chapter **does not satisfy** the outline's mandatory T4 requirement. This is a substantive limitation, disclosed in Chapter 11 and reflected in the report's overall confidence statement.

## 9.6 Red Lines Observed in This Chapter

Per `GPT5.5outline.md` Section 9:

- ❌ Did not cite OpenAI's System Card as the only safety source — also cited AA (T3) hallucination data and noted T4 absence
- ❌ Did not conclude "GPT-5.5 is safe" or "GPT-5.5 is unsafe" — only reported measured values: "Under OpenAI's own system card, gore filter rate regressed from 0.867 to 0.703; under AA-Omniscience, hallucination rate is 86%"

## 9.7 Safety Summary

| Safety dimension | Finding | Source tier | Direction |
|------------------|---------|:-----------:|:---------:|
| Jailbreak resistance | Regression vs GPT-5.3 Instant (vendor-reported) | T6 | Worse |
| Gore content filtering | 0.867 → 0.703 (vendor-reported) | T6 | Worse |
| Sexual content filtering | 0.857 → 0.806 (vendor-reported) | T6 | Worse |
| Hallucination rate (general) | 86% (independently measured) | T3 | Worst among frontier models tested |
| Hallucination reduction (high-risk domains, vendor-claimed) | -52.5% (vendor-reported) | T6 | Better (vendor claim) |
| Memory Sources user control | New transparency feature | T6 | Better |
| Gmail integration | New data surface | T6 | Neutral (structural) |
| Ads platform personalization | New monetization of user data | T5 | Neutral (structural) |
| Cybersecurity risk rating | First-time "High" | T6 | Worse (vendor self-assessment) |
| Biological/chemical risk rating | "High" | T6 | Worse (vendor self-assessment) |
| Bio Bug Bounty program | $25,000 max reward; no published findings | T6 | Neutral (transparency step) |
| Independent T4 regulatory evaluation | None published | — | Evidence gap |
| Independent T3 safety benchmark | None in source set | — | Evidence gap |

**Net assessment**: The safety picture for GPT-5.5 is mixed and **under-measured**. Vendor-reported data shows specific regressions (jailbreak, gore, sexual filtering) alongside vendor-claimed improvements (high-risk-domain hallucination). Independent data shows a general hallucination rate (86%) that is the highest among frontier models tested. Independent government (T4) and academic (T2) safety evaluations are absent as of the report date.

This report does **not** conclude that GPT-5.5 is safe or unsafe. It concludes that GPT-5.5's safety profile has both documented regressions and vendor-claimed improvements, that the vendor's own framework rates the model "High" risk in two domains, and that independent regulatory verification is not yet available.

---

## References for This Chapter

1. OpenAI. "GPT-5.5 system card and Preparedness Framework assessment." 2026-04-23. — **T6 vendor safety data**
2. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/ — **T3 hallucination rate**
3. TechnicalAnalysis-B (industry technical press). "GPT-5.5 Instant: the first instant-tier model rated High." 2026-04-23. URL: https://example.com/technical-analysis/gpt-5.5-instant-high-rating — **T5 safety filter regression interpretation**
4. TechnicalAnalysis-A (industry technical press). "GPT-5.5 launch: a detailed analysis." 2026-04-23. URL: https://example.com/technical-analysis/gpt-5.5-launch-detailed — **T5 Bio Bug Bounty**
5. Matthew Berman. "OpenAI just dropped GPT-5.5.. (WOAH)." YouTube. 2026-04-23. — **T5 High risk rating interpretation**
6. TechnicalAnalysis-C (industry technical press). "GPT-5.5 free tier launch, hands-on testing, and ads platform." 2026-05-05. URL: https://example.com/technical-analysis/gpt-5.5-free-tier-ads — **T5 Ads platform privacy**
7. Ben Davis. "I was wrong about GPT 5.5." YouTube. 2026-05-28. — **T5 autonomous agent permission concerns**
8. `white-paper-research/summary-white-paper-focus.md` — citation standards (T4 mandatory for safety)
