# Chapter 9 — Safety & Alignment Assessment

## 9.1 Jailbreak Resistance Testing

### 9.1.1 Vendor-reported jailbreak regression

OpenAI's own system card reports that **GPT-5.5 Instant exhibits regression in jailbreak resistance testing** (OpenAI, 2026; cross-cited by TechnicalAnalysis-B, 2026). Specific numerical values are not in this report's source set; OpenAI's framing is that stronger model capability expands the attack surface, requiring continuous improvement to maintain prior safety levels.

### 9.1.2 Independent jailbreak measurement

The jailbreak-resistance picture for GPT-5.5 rests entirely on vendor self-assessment (OpenAI, 2026). This is a critical evidence gap; Chapter 11 quantifies it.

### 9.1.3 Comparison to Claude Opus 4.7 jailbreak resistance

This report **does not claim** that GPT-5.5 is more or less jailbreak-resistant than Claude Opus 4.7; no head-to-head comparison is available in the source set.

## 9.2 Harmful-Content Generation Rate

### 9.2.1 Vendor-reported safety filter rates
OpenAI's system card publishes safety filter rates for GPT-5.5 Instant using an **inverse-score convention**: lower scores indicate **more leakage** (i.e., worse safety). The reported values are:

| Category | GPT-5.3 Instant (predecessor) | GPT-5.5 Instant | Direction |
|----------|:-----------------------------:|:---------------:|:---------:|
| Gore content filtering | 0.867 | **0.703** | Regression (worse) |
| Sexual content filtering | 0.857 | **0.806** | Regression (worse) |
| Jailbreak resistance | (not specified) | Regression (worse) | Regression |

Source: OpenAI system card, 2026; cross-cited by TechnicalAnalysis-B, 2026-04-23.

**Interpretation**: On OpenAI's own internal safety metrics, GPT-5.5 Instant's safety filters are **measurably worse** than GPT-5.3 Instant's in at least two categories. These are vendor-reported regressions — OpenAI itself acknowledges them in its system card. Independent verification of these figures is not available in this report's source set.

### 9.2.2 Hallucination as a safety-adjacent concern
The AA-Omniscience hallucination rate of **86% for GPT-5.5 (xhigh)** (Artificial Analysis, 2026) — vs 36% for Claude Opus 4.7 (Max) and 50% for Gemini 3.1 Pro Preview — is not a safety filter failure in the traditional sense. However, in regulated advisory contexts (medical, legal, financial), confidently-wrong outputs can cause harms comparable to unfiltered harmful content. The 86% rate is therefore a safety-adjacent concern documented in this chapter and cross-referenced from Chapter 7 (Section 7.3.1).

### 9.2.3 OpenAI's claimed counter-improvement: 52.5% hallucination reduction

OpenAI claims that GPT-5.5 Instant achieves a **52.5% reduction in hallucination rate in high-risk domains** (OpenAI, 2026; TechnicalAnalysis-B, 2026). This figure is **vendor-reported** and not independently verified by any third-party measurement in this report's source set.

**Apparent contradiction**: OpenAI claims a 52.5% reduction in high-risk-domain hallucination for GPT-5.5 Instant (OpenAI, 2026), while Artificial Analysis independently measures an 86% hallucination rate for GPT-5.5 (xhigh) on AA-Omniscience (Artificial Analysis, 2026). These figures are not directly comparable because:

- They measure different model variants (Instant vs xhigh)
- They use different definitions of "hallucination" (vendor's domain-specific high-risk subset vs AA's general knowledge corpus)
- They use different methodologies (vendor internal vs independent third-party)

**Implication**: The vendor's claim may be true on its specific measurement scope while the independent measurement reveals a broader weakness. This report cites both figures with their measurement scopes specified.

## 9.3 Privacy & Data Security

### 9.3.1 Memory Sources feature
GPT-5.5 Instant introduces a **Memory Sources** feature that transparently displays the origins of model memory, allowing users to view, edit, or delete specific memories (OpenAI, 2026; TechnicalAnalysis-B, 2026). This is a **positive privacy control** — it gives users granular visibility into what the model "knows" about them.

### 9.3.2 Gmail integration
ChatGPT's memory system can now connect to a user's Gmail account, extracting context from emails to provide personalized responses (OpenAI, 2026; TechnicalAnalysis-B, 2026). Examples include remembering user projects, contacts, and events.

**Privacy implication**: The Gmail integration expands the data surface that ChatGPT can access. While Memory Sources (Section 9.3.1) provides user controls, the integration creates new privacy considerations:

- What email content is retained by OpenAI after the conversation ends?
- Does Gmail-integrated memory persist across sessions?
- What are the data-handling terms for enterprise users?

These questions are not answered in the source set. This report notes them as open privacy questions.

### 9.3.3 OpenAI Ads platform privacy implications
The OpenAI Ads platform (launched concurrently with GPT-5.5; see Chapter 8 Section 8.1.3) uses model memory of user preferences, interests, and projects to deliver targeted advertisements (TechnicalAnalysis-C, 2026). This creates a structural incentive for the model to **collect and retain personalization data** that can be monetized through advertising.

**Privacy concern**: The advertising business model may conflict with privacy-preserving defaults. Free-tier users whose inference is ad-supported have a different privacy exposure profile than paid-tier users. This report notes this as a structural privacy concern but does not quantify it; no independent measurement or regulatory evaluation source evaluates the Ads platform's privacy practices.

### 9.3.4 API data retention
OpenAI's published API privacy policy (not reproduced in detail in this report) addresses data retention for API calls. Specific terms are not in this report's source set. Enterprise deployment data-handling terms are similarly not in the source set. This report does **not** make claims about API data retention; it notes the absence of independent privacy auditing as a limitation (Chapter 11).

## 9.4 Regulatory Compliance

### 9.4.1 EU AI Act classification (regulatory evaluation absent)

No EU AI Office evaluation of GPT-5.5 has been published as of the report date. Under the EU AI Act's risk-tier framework, GPT-5.5's classification (limited risk, high risk, or prohibited) is not independently determined. OpenAI's own framing positions GPT-5.5 as a general-purpose AI model subject to transparency obligations; this is vendor positioning, not regulatory determination.

**Implication**: Enterprises deploying GPT-5.5 in EU jurisdictions should not rely on this report for EU AI Act compliance guidance. Consult the EU AI Office's publications and legal counsel.

### 9.4.2 NIST AI RMF (regulatory evaluation absent)

No NIST AI Risk Management Framework evaluation of GPT-5.5 has been published as of the report date. OpenAI has not published a NIST AI RMF-aligned assessment of GPT-5.5 in this report's source set.

**Implication**: U.S. enterprises deploying GPT-5.5 should not rely on this report for NIST AI RMF compliance guidance. Consult NIST publications and internal risk governance.

### 9.4.3 UK AISI (regulatory evaluation absent)

No UK AI Safety Institute evaluation of GPT-5.5 has been published as of the report date. UK AISI's prior evaluations of frontier models (GPT-4o, Claude 3.5 Sonnet, etc.) are not in this report's scope; no GPT-5.5-specific UK AISI report is available.

### 9.4.4 OpenAI Preparedness Framework
OpenAI's own Preparedness Framework rates GPT-5.5 as **"High" risk** in two domains:

1. **Cybersecurity** — first OpenAI model rated High in this domain
2. **Biological / chemical capabilities** — High

Source: OpenAI, 2026-04-23; cross-cited by Matthew Berman, 2026-04-23; TechnicalAnalysis-A, 2026-04-23.

**Important framing**: This is a **vendor self-assessment**. The "High" rating is OpenAI's own classification under its own framework, not an independent government determination. The framework's scoring rubric is published by OpenAI but the specific evaluation inputs for GPT-5.5 are not fully transparent.

### 9.4.5 Bio Bug Bounty program
OpenAI launched a Bio Bug Bounty program with a **$25,000 maximum reward** for external researchers who identify biological-risk vulnerabilities in GPT-5.5 (OpenAI, 2026; TechnicalAnalysis-A, 2026). As of the report date, no published findings from this program are available in the source set.

**Interpretation**: The Bug Bounty is a positive transparency step — it invites external scrutiny of a specific risk domain. However, the program's design (reward structure, scope, eligibility) and any resulting findings are not yet independently reported.

## 9.5 Evidence Coverage for This Chapter

This chapter relies on the following evidence:

| Evidence category | Available? | Role in this chapter |
|-------------------|:----------:|----------------------|
| Vendor-published safety data (OpenAI system card) | Available | Used only as vendor claim; contrasted with Artificial Analysis hallucination data |
| Independent measurement (Artificial Analysis AA-Omniscience) | Available | Provides hallucination rate data; treated as safety-adjacent concern |
| Practitioner testing (Berman, Ben Davis) | Available | Provides qualitative observations on safety-relevant behavior |

This chapter **does not** make definitive safety conclusions. It reports measured values, vendor claims, and qualitative observations.

## 9.6 Evidence Standards Observed

- Did not cite OpenAI's System Card as the only safety source; also cited independently measured hallucination data (Artificial Analysis, 2026) and noted the absence of government-body evaluations.
- Did not conclude "GPT-5.5 is safe" or "GPT-5.5 is unsafe"; only reported measured values: vendor-reported gore filter regression (0.867 → 0.703), vendor-reported jailbreak regression, and independently measured hallucination rate (86%).

## 9.7 Safety Summary

| Safety dimension | Finding | Source | Direction |
|------------------|---------|:------:|:---------:|
| Jailbreak resistance | Regression vs GPT-5.3 Instant (vendor-reported) | OpenAI, 2026 | Worse |
| Gore content filtering | 0.867 → 0.703 (vendor-reported) | OpenAI, 2026 | Worse |
| Sexual content filtering | 0.857 → 0.806 (vendor-reported) | OpenAI, 2026 | Worse |
| Hallucination rate (general) | 86% (independently measured) | Artificial Analysis, 2026 | Worst among frontier models tested |
| Hallucination reduction (high-risk domains) | -52.5% (vendor-reported) | OpenAI, 2026 | Better (vendor claim) |
| Memory Sources user control | New transparency feature | OpenAI, 2026 | Better |
| Gmail integration | New data surface | OpenAI, 2026 | Neutral (structural) |
| Ads platform personalization | New monetization of user data | TechnicalAnalysis-C, 2026 | Neutral (structural) |
| Cybersecurity risk rating | First-time "High" | OpenAI, 2026 | Worse (vendor self-assessment) |
| Biological/chemical risk rating | "High" | OpenAI, 2026 | Worse (vendor self-assessment) |
| Bio Bug Bounty program | $25,000 max reward; no published findings | OpenAI, 2026 | Neutral (transparency step) |
| Independent regulatory evaluation | None published | — | Evidence gap |
| Independent safety benchmark | None in source set | — | Evidence gap |

**Net assessment**: The safety picture for GPT-5.5 is mixed and **under-measured**. Vendor-reported data shows specific regressions (jailbreak, gore, sexual filtering) alongside vendor-claimed improvements (high-risk-domain hallucination). Independently measured data (Artificial Analysis, 2026) shows a general hallucination rate (86%) that is the highest among frontier models tested. Government and academic safety evaluations are absent as of the report date.

This report does **not** conclude that GPT-5.5 is safe or unsafe. It concludes that GPT-5.5's safety profile has both documented regressions and vendor-claimed improvements, that the vendor's own framework rates the model "High" risk in two domains, and that independent regulatory verification is not yet available.
