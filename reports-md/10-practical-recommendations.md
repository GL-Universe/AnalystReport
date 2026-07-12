# Chapter 10 — Practical Recommendations

> This chapter translates the findings from Chapters 5–9 into actionable guidance for enterprise decision-makers, developers, and integrators. The recommendations are conditional: no single model is the right choice for all use cases, and GPT-5.5's reasoning-effort ladder makes "use GPT-5.5" an incomplete recommendation without specifying the effort level.

## 10.1 Decision Tree by Use Case

### 10.1.1 Code generation / development assistance

**Recommendation**: **GPT-5.5 (Medium or X-High)** for most development tasks, with **Pi** as the preferred harness for long-running workflows.

**Rationale**:
- Terminal-Bench Hard lead confirmed by T3 (Artificial Analysis, 2026)
- Engineering-grade security awareness (UUID renaming, whitelist validation, MIME verification) observed in T5 test (TechnicalAnalysis-C, 2026)
- Codex platform integration (browser control, auto-review) provides agentic-workflow capability not yet matched by competitors (Latent Space, 2026, T5; Ben Davis, 2026-05-28, T5)
- X-High recommended for autonomous workflows requiring first-try success; Medium for interactive use (Ben Davis, 2026-05-28, T5)

**Caveats**:
- SWE-Bench Pro lead over Claude Opus 4.7 may be narrower than headline (TechnicalAnalysis-A, 2026, T5)
- Long-context coding should plan thread length under 100K tokens despite 400K advertised window (Ben Davis, 2026-05-04, T5)
- Practitioners with deeply-integrated Claude Code workflows should evaluate switching cost before migrating to Codex (EveryTo, 2026, T5)

### 10.1.2 Long-text processing / document analysis

**Recommendation**: **GPT-5.5 (Medium or X-High) only for threads <100K tokens**. For longer contexts, evaluate Gemini 3.1 Pro Preview or Claude Opus 4.7.

**Rationale**:
- GPT-5.5's compaction regression (vs GPT-5.4) reduces practical usable context to ~100K tokens despite the 400K–1M advertised window (Ben Davis, 2026-05-04, T5)
- Vendor-reported long-context positioning benchmark (94.8% vs Gemini 77.3%) is T6 and not T3-verified
- Needle-in-haystack test failure documented in T5 source (an independent technical review, 2026, T5)

**Caveat**: No T3 benchmark in the source set independently measures long-context quality across context lengths. This recommendation rests on T5 practitioner findings only.

### 10.1.3 Conversation / customer service / intelligent assistants

**Recommendation**: **GPT-5.5 (Medium)** for high-stakes customer-service workflows where task-completion is more valuable than cost minimization. **Gemini 3.1 Pro Preview** for cost-optimized high-volume customer service at matched intelligence.

**Rationale**:
- τ²-Bench Telecom: +7 point improvement over GPT-5.4 (T3 verified) (Artificial Analysis, 2026)
- GDPval-AA: GPT-5.5 leads 1,785 Elo vs Claude ~1,755 and Gemini ~1,315 (T3 verified)
- Gemini 3.1 Pro Preview is cheaper at matched intelligence ($900 vs $1,200 per Index run) (Artificial Analysis, 2026, T3)

**Critical caveat — hallucination**: GPT-5.5 (xhigh) hallucination rate is 86% (T3). For customer-service use cases where confidently-wrong answers carry business risk (regulated industries, financial services, healthcare), prefer **Claude Opus 4.7 (Max)** with 36% hallucination rate (T3) despite the 4× cost premium. For cost-optimized low-risk workflows, prefer Gemini 3.1 Pro Preview.

### 10.1.4 Research tasks requiring high factual accuracy

**Recommendation**: **Claude Opus 4.7 (Max)** preferred over GPT-5.5 (xhigh) for research tasks where honest refusal is more valuable than confident attempt.

**Rationale**:
- GPT-5.5 (xhigh) hallucination rate: 86% vs Claude Opus 4.7 (Max): 36% (Artificial Analysis, 2026, T3)
- For fact-checking, academic research, regulated advisory, the 50-percentage-point hallucination-rate differential is a substantive risk factor
- GPT-5.5 has the **highest knowledge accuracy** (57%) in the same benchmark — it recalls more facts in absolute terms, but produces more incorrect confident assertions when uncertain

**Use case refinement**:
- **Use GPT-5.5** for research tasks where breadth of attempted answers matters and where outputs will be independently verified
- **Use Claude Opus 4.7** for research tasks where confidently-wrong answers carry high cost and verification is expensive
- **Use both** with cross-verification for highest-stakes research (one model produces candidate answers, the other validates refusals)

### 10.1.5 Multimodal / vision tasks

**Recommendation**: **Evaluate Gemini 3.5 Flash** for non-English multimodal OCR or institution-logo recognition tasks. **Use GPT-5.5** for general multimodal tasks where the Visual Inspection step-function improvement matters (per T5; Matthew Berman, 2026).

**Rationale**:
- GPT-5.5 failed to recognize the a regional university logo where Gemini 3.5 Flash succeeded (an independent technical review, 2026, T5)
- Gemini 3.5 Flash has higher vendor-reported MMMU-Pro (83.6% vs 81.2%) (Google, 2026, T6; OpenAI, 2026, T6)
- GPT-5.5's Visual Inspection improvement over GPT-5.4 is described as "step-function" by one T5 source (Matthew Berman, 2026) — useful for UI inspection tasks

**Caveat**: Multimodal capability is one of the **least T3-verified** dimensions in this report. Recommendations here are based on T5 single cases and T6 vendor-reported figures.

### 10.1.6 Constrained creative writing

**Recommendation**: **Gemini 3.5 Flash** preferred over GPT-5.5 for tasks with tight word-count or genre constraints.

**Rationale**:
- GPT-5.5 produced 450–500 words for a 300-word sci-fi prompt and wrote a spy thriller instead of sci-fi (an independent technical review, 2026, T5)
- GPT-5.5 handled the "protagonist cannot speak" constraint by hanging a literal "no speaking allowed" sign on the character (Type B instruction drift, see Chapter 7)
- Gemini 3.5 Flash produced ~320 words of on-topic sci-fi for the same prompt

**Caveat**: Single prompt, single author. Not a systematic measurement. But for creative-writing pipelines with strict format constraints, the evidence favors Gemini 3.5 Flash in this tested case.

### 10.1.7 High-volume / cost-optimized / low-complexity tasks

**Recommendation**: **DeepSeek-V4 Flash** for tasks where open-weight deployment is acceptable and per-token cost is the primary driver.

**Rationale**:
- DeepSeek-V4 Flash: $0.14 / $0.28 per million tokens (input/output) (DeepSeek, 2026, T6)
- Open-weight MIT license enables on-premise deployment
- 1M-token context window per vendor specification

**Caveats**:
- No T3 Intelligence Index measurement of DeepSeek-V4 in this report's source set
- V4-Pro throughput is reportedly constrained by high-end compute availability (Latent Space, 2026, T5)
- For regulated industries requiring U.S. or EU data residency, evaluate deployment jurisdiction carefully

### 10.1.8 Free-tier / consumer use

**Recommendation**: **GPT-5.5 Instant** is the default ChatGPT model and is free for all users, including free-tier users. For consumer use cases where cost is the primary constraint, ChatGPT with GPT-5.5 Instant is a reasonable default.

**Rationale**:
- Free in ChatGPT for all users (OpenAI, 2026, T6; TechnicalAnalysis-C, 2026, T5)
- AIME 2025: 81.2 (vs GPT-5.3 Instant 65.4) — significant improvement (T6)
- Memory Sources feature provides transparency over model memory (T6)

**Caveats**:
- Ads platform monetizes free-tier data: CPC $3–5, CPM $60 (T5)
- Safety filter regressions documented in OpenAI's own system card (gore 0.867→0.703, sexual 0.857→0.806) (T6)
- Jailbreak resistance regression vs GPT-5.3 Instant (T6)

## 10.2 Not-Recommended Use Cases

Per `GPT5.5outline.md` Section 10.2, this section is **mandatory**. The following use cases are **not recommended** with GPT-5.5 based on the findings in Chapters 5–9:

### 10.2.1 Clinical medical decision support

**Not recommended**: GPT-5.5 should not be used as a primary clinical decision support tool without independent medical-domain evaluation.

**Rationale**:
- 86% hallucination rate on AA-Omniscience (T3) — highest among frontier models tested
- No T3 medical-domain evaluation in the source set
- No T4 regulatory evaluation (FDA, EMA) of GPT-5.5 published as of report date
- For clinical-decision-support use cases, the cost of confidently-wrong assertions is materially higher than the cost of honest refusals

### 10.2.2 Legal compliance research

**Not recommended**: GPT-5.5 should not be used as a primary legal research tool without independent legal-domain evaluation and human attorney review.

**Rationale**:
- 86% hallucination rate (T3) — in legal research, confidently-wrong case citations are a known professional hazard
- No T3 legal-domain evaluation in the source set
- No T4 regulatory evaluation published as of report date
- Claude Opus 4.7 (Max) with 36% hallucination rate is the safer choice for legal-research pipelines that require factual reliability

### 10.2.3 Long-running autonomous workflows with blanket "sudo" permissions

**Not recommended without modification**: Ben Davis's documented use case of granting GPT-5.5 (xhigh) full filesystem and sudo access for overnight autonomous workflows is a viable pattern **only for practitioners with experience managing AI agent permissions**.

**Rationale**:
- GPT-5.5 accepted blanket "dangerous" permissions without pushback (Ben Davis, 2026-05-28, T5)
- No source in the set documents the model's behavior when instructed to escalate privileges, install unverified dependencies, or modify security-critical files
- For enterprise deployment, require granular permission scoping (filesystem allow-lists, network egress controls, audit logging)

### 10.2.4 Tasks with strict format / constraint adherence (creative writing)

**Not recommended**: GPT-5.5 should not be used as the primary model for tasks requiring strict adherence to word-count limits, genre constraints, or nuanced narrative-constraint integration.

**Rationale**:
- Documented Type B instruction-understanding drift on a 300-word sci-fi prompt (Chapter 7, Section 7.4.1)
- GPT-5.5 produced 50%+ over the word limit, wrong genre, literal-sign constraint handling (T5)
- Gemini 3.5 Flash performed better on this tested case (T5)

### 10.2.5 non-English multimodal OCR (case-specific)

**Not recommended as the only model**: For non-English institution logo recognition or specialized non-English OCR tasks, evaluate Gemini 3.5 Flash alongside GPT-5.5 based on the tested case.

**Rationale**:
- GPT-5.5 failed to recognize a regional university logo; Gemini 3.5 Flash succeeded (an independent technical review, 2026, T5)
- This is a single test case; for production non-English multimodal OCR, conduct domain-specific evaluation

### 10.2.6 Regulated advisory with high cost-of-error

**Not recommended**: For regulated advisory (financial, legal, medical) where confidently-wrong answers carry high cost, prefer Claude Opus 4.7 (Max) over GPT-5.5 (xhigh).

**Rationale**:
- 86% vs 36% hallucination rate differential (T3)
- 4× cost premium for Claude Opus 4.7 (Max) is justified when cost-of-error exceeds cost-of-inference

## 10.3 Deployment Configuration Recommendations

### 10.3.1 Reasoning-effort level selection

| Task type | Recommended effort level | Rationale |
|-----------|--------------------------|-----------|
| UI / front-end / design (interactive) | Low / No-reasoning | Ben Davis (2026-05-04, T5) recommends Low for UI; faster, sufficient quality for interactive design iteration |
| Math / complex logic (interactive) | X-High | Reasoning depth required; output quality justifies token cost (Ben Davis, 2026-05-04, T5) |
| Long-running autonomous workflows | X-High | First-try success rate justifies token cost; Low reasoning requires multiple iterations (Ben Davis, 2026-05-28, T5) |
| General knowledge queries | Medium | Matched intelligence to Opus 4.7 (Max) at 1/4 cost (Artificial Analysis, 2026, T3) |
| Customer service | Medium | τ²-Bench Telecom improvement justifies Medium over Low for quality (T3) |
| High-stakes factual advisory | X-High + independent verification | Effort level does not solve hallucination; verification is required regardless |

### 10.3.2 Context length management

- **Plan thread length budgets assuming a ~100K token practical limit** (T5 finding, compaction regression)
- **Open new threads between unrelated tasks** rather than maintaining a single long thread (Ben Davis, 2026-05-04, T5)
- **Use Pi harness** rather than Codex CLI for long-running workflows — Pi handles context summarization and thread management more stably per T5 report (Ben Davis, 2026-05-04, T5)

### 10.3.3 System-prompt design

No source in this report's set systematically tests the impact of system-prompt design on GPT-5.5's performance. This is flagged as a measurement gap in Chapter 11. Practitioners should test their own system prompts against representative task sets before production deployment.

### 10.3.4 Temperature setting

No source in this report's set publishes temperature-specific evaluations of GPT-5.5. T3 source (Artificial Analysis) uses a documented fixed configuration; T5 sources vary. For production deployments requiring reproducibility, test at temperature=0 against a fixed test set.

## 10.4 Migration Considerations

### 10.4.1 Migrating from GPT-5.4 to GPT-5.5

- **Cost**: Expect ~20% net cost increase per AA Intelligence Index run despite 2× per-token price increase (T3)
- **Quality**: Higher Intelligence Index score; broader knowledge accuracy (57% on AA-Omniscience)
- **Risk**: Higher hallucination rate (86% on AA-Omniscience) requires additional verification
- **Compaction**: Plan for shorter thread budgets; the regression vs GPT-5.4 is a documented behavioral change

### 10.4.2 Migrating from Claude Opus 4.7 to GPT-5.5

- **Cost**: 4× cost reduction at Medium reasoning (T3)
- **Quality**: Intelligence Index lead; GDPval-AA lead; knowledge accuracy lead
- **Risk**: 86% vs 36% hallucination rate — material increase in confidently-wrong outputs
- **Switching cost**: For teams with deep Claude Code workflow integration, the switching cost may offset the model advantage (EveryTo, 2026, T5)

### 10.4.3 Migrating from Gemini 3.1 Pro to GPT-5.5

- **Cost**: 33% cost increase per Index run (T3) — Gemini 3.1 Pro Preview is cheaper at matched intelligence
- **Quality**: GPT-5.5 leads on Intelligence Index overall; Gemini leads on 3 additional AA evaluations (Artificial Analysis, 2026, T3)
- **Risk**: Both models have different hallucination profiles (86% vs 50%); task-specific evaluation recommended

---

## References for This Chapter

1. Artificial Analysis. "OpenAI's GPT-5.5 is the new leading AI model." 2026-04-23. URL: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/ — **T3 cost-intelligence matrix**
2. Ben Davis. "GPT-5.5 is the best model ever made (but there's a catch)." YouTube. 2026-05-04. — **T5 effort-level and compaction recommendations**
3. Ben Davis. "I was wrong about GPT 5.5." YouTube. 2026-05-28. — **T5 X-High autonomous workflow and permission concerns**
4. an independent technical review. "Gemini 3.5 Flash vs GPT-5.5: a hands-on comparison." 2026-05-15. URL: https://example.com/technical-review/gemini-3.5-flash-vs-gpt-5.5 — **T5 task-specific comparison data**
5. TechnicalAnalysis-A (industry technical press). "GPT-5.5 launch: a detailed analysis." 2026-04-23. URL: https://example.com/technical-analysis/gpt-5.5-launch-detailed — **T5 SWE-Bench Pro caveat**
6. TechnicalAnalysis-C (industry technical press). "GPT-5.5 free tier launch: hands-on testing and ads platform." 2026-05-05. URL: https://example.com/technical-analysis/gpt-5.5-free-tier-ads — **T5 coding security behavior**
7. Matthew Berman. "OpenAI just dropped GPT-5.5.. (WOAH)." YouTube. 2026-04-23. — **T5 Visual Inspection improvement**
8. Latent Space. "[AINews] GPT 5.5 and OpenAI Codex Superapp." 2026-04-22/23. URL: https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp — **T5 Codex platform integration**
9. EveryTo (Laura Entis). "Who Isn't Using GPT 5.5." 2026-04-30. URL: https://every.to/context-window/who-isnt-using-gpt-55 — **T5 Claude workflow switching cost**
10. DeepSeek. "DeepSeek-V4 Preview release." 2026-04-23. — **T6 open-weight pricing**
