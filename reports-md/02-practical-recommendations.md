# Chapter 2 — Practical Recommendations

> This chapter translates the findings from Chapters 5–9 into actionable guidance for enterprise decision-makers, developers, and integrators. The recommendations are conditional: no single model is the right choice for all use cases, and GPT-5.5's reasoning-effort ladder makes "use GPT-5.5" an incomplete recommendation without specifying the effort level.

## 2.1 Decision Tree by Use Case

### 2.1.1 Code generation / development assistance

**Recommendation**: **GPT-5.5 (Medium or X-High)** for most development tasks, with **Pi** as the preferred harness for long-running workflows.

**Rationale**:
- Terminal-Bench Hard lead confirmed by independent measurement (Artificial Analysis, 2026)
- Engineering-grade security awareness (UUID renaming, whitelist validation, MIME verification) observed in practitioner testing test (TechnicalAnalysis-C, 2026)
- Codex platform integration (browser control, auto-review) provides agentic-workflow capability not yet matched by competitors (Latent Space, 2026; Ben Davis, 2026-05-28)
- X-High recommended for autonomous workflows requiring first-try success; Medium for interactive use (Ben Davis, 2026-05-28)

**Caveats**:
- SWE-Bench Pro lead over Claude Opus 4.7 may be narrower than headline (TechnicalAnalysis-A, 2026)
- Long-context coding should plan thread length under 100K tokens despite 400K advertised window (Ben Davis, 2026-05-04)
- Practitioners with deeply-integrated Claude Code workflows should evaluate switching cost before migrating to Codex (EveryTo, 2026)

### 2.1.2 Long-text processing / document analysis

**Recommendation**: **GPT-5.5 (Medium or X-High) only for threads <100K tokens**. For longer contexts, evaluate Gemini 3.1 Pro Preview or Claude Opus 4.7.

**Rationale**:
- GPT-5.5's compaction regression (vs GPT-5.4) reduces practical usable context to ~100K tokens despite the 400K–1M advertised window (Ben Davis, 2026-05-04)
- Vendor-reported long-context positioning benchmark (94.8% vs Gemini 77.3%) is vendor-reported and not independently verified
- Needle-in-haystack test failure documented in practitioner testing source (an independent technical review, 2026)

**Caveat**: No independent benchmark in the source set independently measures long-context quality across context lengths. This recommendation rests on practitioner findings only.

### 2.1.3 Conversation / customer service / intelligent assistants

**Recommendation**: **GPT-5.5 (Medium)** for high-stakes customer-service workflows where task-completion is more valuable than cost minimization. **Gemini 3.1 Pro Preview** for cost-optimized high-volume customer service at matched intelligence.

**Rationale**:
- τ²-Bench Telecom: +7 point improvement over GPT-5.4 (independently verified) (Artificial Analysis, 2026)
- GDPval-AA: GPT-5.5 leads 1,785 Elo vs Claude ~1,755 and Gemini ~1,315 (independently verified)
- Gemini 3.1 Pro Preview is cheaper at matched intelligence ($900 vs $1,200 per Index run) (Artificial Analysis, 2026)

**Critical caveat — hallucination**: GPT-5.5 (xhigh) hallucination rate is 86%. For customer-service use cases where confidently-wrong answers carry business risk (regulated industries, financial services, healthcare), prefer **Claude Opus 4.7 (Max)** with 36% hallucination rate despite the 4× cost premium. For cost-optimized low-risk workflows, prefer Gemini 3.1 Pro Preview.

### 2.1.4 Research tasks requiring high factual accuracy

**Recommendation**: **Claude Opus 4.7 (Max)** preferred over GPT-5.5 (xhigh) for research tasks where honest refusal is more valuable than confident attempt.

**Rationale**:
- GPT-5.5 (xhigh) hallucination rate: 86% vs Claude Opus 4.7 (Max): 36% (Artificial Analysis, 2026)
- For fact-checking, academic research, regulated advisory, the 50-percentage-point hallucination-rate differential is a substantive risk factor
- GPT-5.5 has the **highest knowledge accuracy** (57%) in the same benchmark — it recalls more facts in absolute terms, but produces more incorrect confident assertions when uncertain

**Use case refinement**:
- **Use GPT-5.5** for research tasks where breadth of attempted answers matters and where outputs will be independently verified
- **Use Claude Opus 4.7** for research tasks where confidently-wrong answers carry high cost and verification is expensive
- **Use both** with cross-verification for highest-stakes research (one model produces candidate answers, the other validates refusals)

### 2.1.5 Multimodal / vision tasks

**Recommendation**: **Evaluate Gemini 3.5 Flash** for non-English multimodal OCR or institution-logo recognition tasks. **Use GPT-5.5** for general multimodal tasks where the Visual Inspection step-function improvement matters (per practitioner testing;; Matthew Berman, 2026).

**Rationale**:
- GPT-5.5 failed to recognize the a regional university logo where Gemini 3.5 Flash succeeded (an independent technical review, 2026)
- Gemini 3.5 Flash has higher vendor-reported MMMU-Pro (83.6% vs 81.2%) (Google, 2026; OpenAI, 2026)
- GPT-5.5's Visual Inspection improvement over GPT-5.4 is described as "step-function" by one practitioner testing source (Matthew Berman, 2026) — useful for UI inspection tasks

**Caveat**: Multimodal capability is one of the **least independently verified** dimensions in this report. Recommendations here are based on single practitioner cases and vendor-reported figures.

### 2.1.6 Constrained creative writing

**Recommendation**: **Gemini 3.5 Flash** preferred over GPT-5.5 for tasks with tight word-count or genre constraints.

**Rationale**:
- GPT-5.5 produced 450–500 words for a 300-word sci-fi prompt and wrote a spy thriller instead of sci-fi (an independent technical review, 2026)
- GPT-5.5 handled the "protagonist cannot speak" constraint by hanging a literal "no speaking allowed" sign on the character (Type B instruction drift, see Chapter 7)
- Gemini 3.5 Flash produced ~320 words of on-topic sci-fi for the same prompt

**Caveat**: Single prompt, single author. Not a systematic measurement. But for creative-writing pipelines with strict format constraints, the evidence favors Gemini 3.5 Flash in this tested case.

### 2.1.7 High-volume / cost-optimized / low-complexity tasks

**Recommendation**: **DeepSeek-V4 Flash** for tasks where open-weight deployment is acceptable and per-token cost is the primary driver.

**Rationale**:
- DeepSeek-V4 Flash: $0.14 / $0.28 per million tokens (input/output) (DeepSeek, 2026)
- Open-weight MIT license enables on-premise deployment
- 1M-token context window per vendor specification

**Caveats**:
- No independent Intelligence Index measurement of DeepSeek-V4 in this report's source set
- V4-Pro throughput is reportedly constrained by high-end compute availability (Latent Space, 2026)
- For regulated industries requiring U.S. or EU data residency, evaluate deployment jurisdiction carefully

### 2.1.8 Free-tier / consumer use

**Recommendation**: **GPT-5.5 Instant** is the default ChatGPT model and is free for all users, including free-tier users. For consumer use cases where cost is the primary constraint, ChatGPT with GPT-5.5 Instant is a reasonable default.

**Rationale**:
- Free in ChatGPT for all users (OpenAI, 2026; TechnicalAnalysis-C, 2026)
- AIME 2025: 81.2 (vs GPT-5.3 Instant 65.4) — significant improvement
- Memory Sources feature provides transparency over model memory
**Caveats**:
- Ads platform monetizes free-tier data: CPC $3–5, CPM $60
- Safety filter regressions documented in OpenAI's own system card (gore 0.867→0.703, sexual 0.857→0.806)
- Jailbreak resistance regression vs GPT-5.3 Instant
## 2.2 Not-Recommended Use Cases

This section lists use cases that are **not recommended** with GPT-5.5 based on the findings in Chapters 5–9:

### 2.2.1 Clinical medical decision support

**Not recommended**: GPT-5.5 should not be used as a primary clinical decision support tool without independent medical-domain evaluation.

**Rationale**:
- 86% hallucination rate on AA-Omniscience — highest among frontier models tested
- For clinical-decision-support use cases, the cost of confidently-wrong assertions is materially higher than the cost of honest refusals

### 2.2.2 Legal compliance research

**Not recommended**: GPT-5.5 should not be used as a primary legal research tool without independent legal-domain evaluation and human attorney review.

**Rationale**:
- 86% hallucination rate — in legal research, confidently-wrong case citations are a known professional hazard
- Claude Opus 4.7 (Max) with 36% hallucination rate is the safer choice for legal-research pipelines that require factual reliability

### 2.2.3 Long-running autonomous workflows with blanket "sudo" permissions

**Not recommended without modification**: Ben Davis's documented use case of granting GPT-5.5 (xhigh) full filesystem and sudo access for overnight autonomous workflows is a viable pattern **only for practitioners with experience managing AI agent permissions**.

**Rationale**:
- GPT-5.5 accepted blanket "dangerous" permissions without pushback (Ben Davis, 2026-05-28)
- For enterprise deployment, require granular permission scoping (filesystem allow-lists, network egress controls, audit logging)

### 2.2.4 Tasks with strict format / constraint adherence (creative writing)

**Not recommended**: GPT-5.5 should not be used as the primary model for tasks requiring strict adherence to word-count limits, genre constraints, or nuanced narrative-constraint integration.

**Rationale**:
- Documented Type B instruction-understanding drift on a 300-word sci-fi prompt (Chapter 7, Section 7.4.1)
- GPT-5.5 produced 50%+ over the word limit, wrong genre, literal-sign constraint handling
- Gemini 3.5 Flash performed better on this tested case
### 2.2.5 non-English multimodal OCR (case-specific)

**Not recommended as the only model**: For non-English institution logo recognition or specialized non-English OCR tasks, evaluate Gemini 3.5 Flash alongside GPT-5.5 based on the tested case.

**Rationale**:
- GPT-5.5 failed to recognize a regional university logo; Gemini 3.5 Flash succeeded (an independent technical review, 2026)
- This is a single test case; for production non-English multimodal OCR, conduct domain-specific evaluation

### 2.2.6 Regulated advisory with high cost-of-error

**Not recommended**: For regulated advisory (financial, legal, medical) where confidently-wrong answers carry high cost, prefer Claude Opus 4.7 (Max) over GPT-5.5 (xhigh).

**Rationale**:
- 86% vs 36% hallucination rate differential
- 4× cost premium for Claude Opus 4.7 (Max) is justified when cost-of-error exceeds cost-of-inference

## 2.3 Deployment Configuration Recommendations

### 2.3.1 Reasoning-effort level selection

| Task type | Recommended effort level | Rationale |
|-----------|--------------------------|-----------|
| UI / front-end / design (interactive) | Low / No-reasoning | Ben Davis (2026-05-04) recommends Low for UI; faster, sufficient quality for interactive design iteration |
| Math / complex logic (interactive) | X-High | Reasoning depth required; output quality justifies token cost (Ben Davis, 2026-05-04) |
| Long-running autonomous workflows | X-High | First-try success rate justifies token cost; Low reasoning requires multiple iterations (Ben Davis, 2026-05-28) |
| General knowledge queries | Medium | Matched intelligence to Opus 4.7 (Max) at 1/4 cost (Artificial Analysis, 2026) |
| Customer service | Medium | τ²-Bench Telecom improvement justifies Medium over Low for quality |
| High-stakes factual advisory | X-High + independent verification | Effort level does not solve hallucination; verification is required regardless |

### 2.3.2 Context length management

- **Plan thread length budgets assuming a ~100K token practical limit** (practitioner testing finding, compaction regression)
- **Open new threads between unrelated tasks** rather than maintaining a single long thread (Ben Davis, 2026-05-04)
- **Use Pi harness** rather than Codex CLI for long-running workflows — Pi handles context summarization and thread management more stably per practitioner report (Ben Davis, 2026-05-04)

### 2.3.3 System-prompt design

Practitioners should test their own system prompts against representative task sets before production deployment, as system-prompt design materially affects GPT-5.5's performance on task-completion benchmarks.

### 2.3.4 Temperature setting

Artificial Analysis uses a documented fixed configuration; practitioner testing sources vary in their temperature settings. For production deployments requiring reproducibility, test at temperature=0 against a fixed test set.

## 2.4 Migration Considerations

### 2.4.1 Migrating from GPT-5.4 to GPT-5.5

- **Cost**: Expect ~20% net cost increase per AA Intelligence Index run despite 2× per-token price increase
- **Quality**: Higher Intelligence Index score; broader knowledge accuracy (57% on AA-Omniscience)
- **Risk**: Higher hallucination rate (86% on AA-Omniscience) requires additional verification
- **Compaction**: Plan for shorter thread budgets; the regression vs GPT-5.4 is a documented behavioral change

### 2.4.2 Migrating from Claude Opus 4.7 to GPT-5.5

- **Cost**: 4× cost reduction at Medium reasoning
- **Quality**: Intelligence Index lead; GDPval-AA lead; knowledge accuracy lead
- **Risk**: 86% vs 36% hallucination rate — material increase in confidently-wrong outputs
- **Switching cost**: For teams with deep Claude Code workflow integration, the switching cost may offset the model advantage (EveryTo, 2026)

### 2.4.3 Migrating from Gemini 3.1 Pro to GPT-5.5

- **Cost**: 33% cost increase per Index run — Gemini 3.1 Pro Preview is cheaper at matched intelligence
- **Quality**: GPT-5.5 leads on Intelligence Index overall; Gemini leads on 3 additional AA evaluations (Artificial Analysis, 2026)
- **Risk**: Both models have different hallucination profiles (86% vs 50%); task-specific evaluation recommended
