# Reference → GPT-5.5 白皮书章节映射总表

> 生成日期: 2026-07-12
> 对照目标: `GPT5.5outline.md` (GPT-5.5 模型服务评测白皮书, 12 章 + 执行摘要)
> 数据来源: `reference/` 目录下的 12 篇 `-outline.md` 文件
> 
> **用途**: 撰写白皮书各章节时，快速定位哪篇文章包含该章节所需的数据、案例或分析。

---

## 一、白皮书章节结构速查

| # | 章节 | 需要的内容类型 |
|---|------|-------------|
| Ch0 | Executive Summary | 核心数字结论、与竞品差距、最重要失败场景 |
| Ch1 | 研究背景与问题 | 行业背景、GPT-5.5 发布背景、现有 benchmark 局限 |
| Ch2 | 方法论 | 评测框架设计、测试场景分类 |
| Ch3 | 测试数据集 | 数据集来源、构成、污染性控制 |
| Ch4 | 评估指标体系 | 事实准确率、幻觉率等指标定义与参照 |
| Ch5.1 | 事实性推理与知识 | 专业领域问答、跨语言知识迁移准确率 |
| Ch5.2 | 代码生成能力 | 真实工程任务修复通过率、代码安全性 |
| Ch5.3 | 长文本与文档理解 | 20K+ tokens 文档问答、摘要忠实度 |
| Ch5.4 | 多轮对话与指令跟随 | 复杂指令执行率、角色一致性、拒绝率 |
| Ch5.5 | 生成一致性与稳定性 | Temperature=0 下确定性、重复输出差异度 |
| Ch6 | 竞品对比分析 | 总体对比矩阵、优势/劣势场景、成本权衡 |
| Ch7 | 失败案例与边界 | 幻觉、指令偏差、一致性失败、长文本退化 |
| Ch8 | 成本效益分析 | API 定价、token 效率、延迟、成本效率比 |
| Ch9 | 安全与对齐评估 | 越狱抵抗、有害内容生成率、隐私、监管合规 |
| Ch10 | 实践建议 | 使用场景推荐/不推荐、部署配置 |
| Ch11 | 研究局限性 | 评测窗口、样本偏差、评分员偏差声明 |
| Ch12 | 附录 | 利益声明、原始数据、评估脚本、参考文献 |

---

## 二、来源概览

| 编号 | 文件名 | 来源类型 | 可信度 |
|:---:|--------|---------|:---:|
| S1 | `WesRoth-GPT5.5-is-wild-outline.md` | YouTube (Wes Roth) | T5 |
| S2 | `BenDavis-GPT5.5-best-model-outline.md` | YouTube (Ben Davis) | T5 |
| S3 | `BenDavis-I-was-wrong-about-GPT5.5-outline.md` | YouTube (Ben Davis 续篇) | T5 |
| S4 | `MatthewBerman-GPT5.5-dropped-outline.md` | YouTube (Matthew Berman) | T5 |
| S5 | `WXArticle1-GPT5.5-detailed-review-outline.md` | WeChat 公众号 | T5+T6 |
| S6 | `WXArticle2-GPT5.5-Instant-outline.md` | WeChat 公众号 | T5+T6 |
| S7 | `WXArticle3-GPT5.5-free-ads-outline.md` | WeChat 公众号 | T5 |
| S8 | `WXArticle4-Gemini3.5Flash-vs-GPT5.5-outline.md` | WeChat 公众号 (JackCui) | T5 |
| S9 | `WXArticle5-GPT5.5-real-work-outline.md` | WeChat 公众号 (字母AI) | T5+T6 |
| S10 | `LatentSpace-GPT5.5-Codex-Superapp-outline.md` | Latent Space (Substack) | T5+T3 |
| S11 | `ArtificialAnalysis-GPT5.5-leading-model-outline.md` | Artificial Analysis | **T3** |
| S12 | `EveryTo-Who-isnt-using-GPT5.5-outline.md` | Every.to (付费部分) | T5(有限) |

---

## 三、按白皮书章节的推荐来源

### Ch0 — Executive Summary

| 优先级 | 来源 | 可用的核心数据 |
|:---:|------|-------------|
| ★★★ | S11 ArtificialAnalysis | Intelligence Index 领先 3 分；幻觉率 86% vs Opus 36%；Token 效率 ~40% 更少；净成本 +20% |
| ★★★ | S5 WXArticle1 | 9 大核心基准数据一览表（Terminal-Bench/SWE-Bench/GDPval/OSWorld/CyberGym 等） |
| ★★ | S4 MatthewBerman | Terminal-Bench 82.7%、SWE-Bench Pro 58.6%、GDPval 84.9%、OSWorld 78.7% |

### Ch1 — 研究背景与问题

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S9 WXArticle5 | 范文转变论述（从"知不知道"到"能不能做完"）；GPT-4o→GPT-5.5 五阶段演进脉络 |
| ★★★ | S10 LatentSpace | GPT-5.5 发布背景（Opus 4.7 一周后回击）；Codex 超级应用战略；DeepSeek-V4 同日发布 |
| ★★ | S1 WesRoth | "Anthropic 效应"行业竞争格局（NSA/Google/Grok） |
| ★★ | S7 WXArticle3 | OpenAI 商业模式转折（免费 + Ads 转型） |
| ★ | S12 EveryTo | CTO→Anthropic IC 职业趋势；GPT-5.5 一周后脉搏检查 |

### Ch2 — 方法论

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S11 ArtificialAnalysis | T3 级独立评测方法论（Intelligence Index + 多推理级别测试框架） |
| ★★ | S9 WXArticle5 | 评测标准范式转变（任务级评估 vs 知识测试）的方法论启发 |

### Ch4 — 评估指标体系

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S11 ArtificialAnalysis | 推理努力度阶梯（xhigh/high/medium/low/non-reasoning 五级）作为指标设计参照 |
| ★★ | S6 WXArticle2 | 幻觉率降低 52.5%（高风险领域）——可作为指标参照/厂商声称值对比基准 |
| ★★ | S9 WXArticle5 | GDPval 定义（44 种真实职业任务、非选择题） |

### Ch5.1 — 事实性推理与知识能力

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S11 ArtificialAnalysis | AA-Omniscience 最高知识准确率 57%；GDPval-AA Elo 1785（>Opus 4.7 Max ~30 分）；五项评测领先 |
| ★★★ | S5 WXArticle1 | GDPval 84.9%（vs Opus 4.7 80.3%、Gemini 3.1 Pro 67.3%）；BrowseComp 84.4% |
| ★★ | S9 WXArticle5 | Tau2 Telecom 98.0%；FinanceAgent 60.0%；投资银行建模 88.5%；OfficeQA Pro 54.1% |
| ★★ | S6 WXArticle2 | AIME 2025: 81.2（GPT-5.3 Instant 65.4→GPT-5.5 Instant 81.2）；MMMU-Pro: 76.0 |
| ★ | S7 WXArticle3 | 数学收敛验证实测对比（GPT-5.3 跳过 vs GPT-5.5 完整收敛分析） |
| ★ | S8 WXArticle4 | 世界杯冠军预测分析；手写生物实验笔记解读 |

### Ch5.2 — 代码生成能力

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S5 WXArticle1 | Terminal-Bench 82.7%；SWE-Bench Pro 58.6%；Expert-SWE 73.1%；Codex 400K 上下文窗口 |
| ★★★ | S4 MatthewBerman | 完整编码基准套件 + Codex 90%+ 推测 |
| ★★ | S3 BenDavis-I-was-wrong | Computer Use 自动化测试闭环（写→看→发现bug→修复→验证）；工作树并行化 |
| ★★ | S2 BenDavis-best | 代码"克制"行为、全项目上下文保持、最小修改范围 |
| ★★ | S9 WXArticle5 | 官方 Codex Demo（天体图片→WebGL 3D + NASA 数据；3D 地牢竞技场 Three.js）；85%员工周使用 |
| ★★ | S7 WXArticle3 | 编码安全实测（文件上传：GPT-5.3 基础校验 vs GPT-5.5 工程级安全方案） |
| ★ | S8 WXArticle4 | 前端设计三场景实测（个人网站/3D 模型/赛马小游戏）；代码执行 78.2% vs Gemini 76.2% |
| ★ | S10 LatentSpace | Codex 升级为完整代理工作空间（浏览器控制/auto-review/QA/Slides） |
| ★ | S1 WesRoth | 代码质量描述（跨文件修复、上下文保持、非机械输出） |

### Ch5.3 — 长文本与文档理解

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S2 BenDavis-best | **独家发现**: compaction 比 GPT-5.4 更弱；400K 窗口但实际表现建议 <100K；接近窗口上限质量骤降 |
| ★★ | S8 WXArticle4 | 大海捞针测试（两个模型均未识别藏匿命令）；长上下文定位 GPT-5.5 94.8% vs Gemini 77.3% |
| ★ | S5 WXArticle1 | Codex 400K token 上下文窗口 |
| ★ | S10 LatentSpace | API 1M token 上下文（Altman 确认） |

### Ch5.4 — 多轮对话与指令跟随

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S8 WXArticle4 | 写作能力测试（300字要求→GPT-5.5 输出450-500字；"男主不能说话"→生硬处理）；抽象逻辑推理 84.6% vs Gemini 72.1% |
| ★★ | S3 BenDavis-I-was-wrong | Agent 自主运行（大型迁移/复杂重构/过夜无人监督） |
| ★ | S7 WXArticle3 | 人格风格改进（"去油"、回复简洁、活人感保留） |

### Ch6 — 竞品对比分析

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S8 WXArticle4 | **最全面的独立实测对比**: 前端/推理/上下文/写作四维测试 + 基准数据表 + 优势劣势场景完整分析 |
| ★★★ | S11 ArtificialAnalysis | Intelligence Index 总排名；五级推理 vs 竞品成本对比；Gemini 三项额外评测领先 |
| ★★ | S10 LatentSpace | GPT-5.5 (Medium) = Opus 4.7 (Max) 智力但 1/4 成本；编码基准被刻意未提及 |
| ★★ | S5 WXArticle1 | SWE-Bench Pro 不及 Claude；MCP Atlas 落后竞争对手；HLE 退步 |
| ★ | S1 WesRoth | 训练硬件对比（GB200/GB300 vs TPU）；基准领先但差距缩小 |
| ★ | S4 MatthewBerman | Terminal-Bench/SWE-Bench/OSWorld vs Opus 4.7 对比 |

### Ch7 — 失败案例与边界分析

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S11 ArtificialAnalysis | **核心发现**: 幻觉率 86% vs Claude Opus 4.7 36%、Gemini 3.1 Pro 50%——GPT-5.5 倾向于不确定时仍回答 |
| ★★★ | S8 WXArticle4 | **类型A**(OCR错误): 未识别郑州大学 logo；**类型B**(指令偏差): 写作超字数+跑题+生硬约束遵循；**类型D**(长文本): 大海捞针两模型均失败 |
| ★★★ | S6 WXArticle2 | 安全过滤退步: gore 0.867→0.703、sexual 0.857→0.806；jailbreak 测试退化 |
| ★★ | S2 BenDavis-best | **类型D**(长文本退化): compaction 弱、线程超 100K token 质量下降 |
| ★★ | S5 WXArticle1 | SWE-Bench Pro 在某些任务弱于 Anthropic；HLE 性能退步(回归) |
| ★ | S1 WesRoth | 推理模式不一致性（不同场景 Low vs X-High 矛盾） |
| ★ | S7 WXArticle3 | GPT-5.3 代码生成失败（基础校验 vs GPT-5.5 工程级方案）——前代对照 |
| ★ | S3 BenDavis-I-was-wrong | Low reasoning 模式下容易出错 |

### Ch8 — 成本效益分析

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S11 ArtificialAnalysis | **T3 核心数据**: ~40% 更少输出 token；净成本仅 +20%；比 Opus 4.7 (Max) 便宜 30%；AA Intelligence Index 完整成本测算 |
| ★★★ | S10 LatentSpace | AA 验证: GPT-5.5 (Medium) = Opus 4.7 (Max) 智力但成本 1/4 (~$1,200 vs $4,800) |
| ★★ | S8 WXArticle4 | AA 实测: GPT-5.5 Medium ~2200 万 token/$1,199/得分 57 vs Gemini 3.5 Flash ~7300 万 token/$1,522/得分 55 |
| ★★ | S2 BenDavis-best | 定价 $5/$30, Pro $30/$180；token 效率 20-40%；效率基本抵消涨价 |
| ★★ | S4 MatthewBerman | 相同任务 token 减少 20-40%；净成本增约 20%；速度持平 |
| ★★ | S5 WXArticle1 | 推理分区优化 20% 速度改进；2 倍定价效率提升后实际仅增 ~20% 成本 |
| ★ | S3 BenDavis-I-was-wrong | Peter's Experiment: $130 万/月 API 支出——极端商业成本案例 |

### Ch9 — 安全与对齐评估

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S6 WXArticle2 | **独家量化数据**: gore 0.867→0.703、sexual 0.857→0.806 安全过滤退步；jailbreak 退化；Memory Sources 隐私透明度 |
| ★★★ | S5 WXArticle1 | Cybersecurity 首次评 "High"；生物/化学 High；$25,000 Bio Bug Bounty；红队测试+200 场景 |
| ★★ | S4 MatthewBerman | CyberGym 81.8%；生物/化学 High 风险；近 200 场景安全测试；API 延等安全防护 |
| ★ | S3 BenDavis-I-was-wrong | 给模型 sudo 权限的安全风险；Computer Use "危险权限"讨论 |
| ★ | S1 WesRoth | Mythos 争议(AI 军事/情报应用)；NSA 使用 Claude 的安全边界 |
| ★ | S7 WXArticle3 | 个性化记忆用于广告投放的隐私担忧；Agentic Commerce 隐私边界 |

### Ch10 — 实践建议

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S2 BenDavis-best | 推理模式决策树（Low/No-Reasoning→UI/前端；X-High→复杂逻辑）；Pi vs Codex CLI 选择；线程管理最佳实践 |
| ★★★ | S11 ArtificialAnalysis | Medium 推理即可匹敌 Opus 4.7 Max — 成本优化建议 |
| ★★ | S8 WXArticle4 | 场景推荐/不推荐决策树：前端首屏→GPT-5.5(审美)；可运行项目→Gemini(细节)；多模态OCR→Gemini；严格约束写作→不宜GPT-5.5 |
| ★ | S3 BenDavis-I-was-wrong | Computer Use 场景推荐（大型迁移/复杂重构/通宵实验）；推理模式升级建议 |
| ★ | S12 EveryTo | Claude 工作流切换至 Codex 的采纳障碍 |
| ★ | S7 WXArticle3 | Conversational Commerce 场景推荐 |

### Ch11 — 研究局限性

| 优先级 | 来源 | 可用内容 |
|:---:|------|---------|
| ★★★ | S6 WXArticle2 | 安全过滤版本间 regression 警示（评测需标注模型版本和时间窗口） |
| ★★ | S3 BenDavis-I-was-wrong | 推理级别对评测结论的关键影响（Low vs X-High 结论完全相反） |
| ★ | S2 BenDavis-best | 上下文窗口敏感性（评测窗口内模型行为随 token 数变化） |
| ★ | S12 EveryTo | 采纳初期数据时效性（发布一周后评估的局限性） |

---

## 四、按来源总览

| 来源 | 覆盖的章节数 | 核心贡献章节 | 独特价值 |
|------|:---:|---------|---------|
| S11 ArtificialAnalysis | **10** | Ch0,Ch4,Ch5.1,Ch6,Ch7,Ch8 | **T3 级独立评测数据最全、可信度最高**，86%幻觉率是 Ch7 核心引用 |
| S8 WXArticle4 | **9** | Ch5.2,Ch5.3,Ch5.4,Ch6,Ch7,Ch8 | **实测案例最丰富**（含完整 prompt+错误输出），竞品对比最全面 |
| S5 WXArticle1 | **9** | Ch0,Ch5.1,Ch5.2,Ch6,Ch7,Ch8,Ch9 | 信息密度最高，**劣势场景和失败分析**覆盖完整 |
| S2 BenDavis-best | **7** | Ch5.3,Ch7,Ch8,Ch10 | 唯一发现 **compaction 退化和 100K 限制**的来源 |
| S3 BenDavis-I-was-wrong | **7** | Ch5.2,Ch8,Ch9,Ch10,Ch11 | **Computer Use** 和 **$130万/月**商业案例独家 |
| S9 WXArticle5 | **7** | Ch1,Ch5.1,Ch5.2 | **范式转变论述**最系统（Ch1 核心引用） |
| S10 LatentSpace | **7** | Ch1,Ch6,Ch8 | AA 成本对比 + **Codex 超级应用战略**，Ch1/Ch8 关键 |
| S4 MatthewBerman | **6** | Ch0,Ch5.2,Ch8,Ch9 | 官方发布后最全面的基准数据解读 |
| S6 WXArticle2 | **5** | Ch7,Ch9,Ch11 | **安全过滤量化退步独家数据**（Ch9 核心引用） |
| S7 WXArticle3 | **5** | Ch5.1,Ch5.2,Ch8,Ch9 | 编码安全实测 + 广告商业模式 |
| S1 WesRoth | **5** | Ch1,Ch6,Ch7,Ch9 | 行业竞争格局和 Anthropic 效应 |
| S12 EveryTo | **3** | Ch6,Ch10,Ch11 | **Claude 工作流切换障碍**的定性参考（付费内容不完整） |

---

## 五、按可信度分层的核心引用建议

### T3 级（独立评测机构，白皮书核心证据）
- **S11 ArtificialAnalysis** — 必须作为 Ch6/Ch7/Ch8 的主要量化数据来源
- **S10 LatentSpace** 引用的 AA 数据 — 可交叉验证 S11

### T5 级（用户实测 + 行业分析，支撑和案例）
- **S8 WXArticle4** — Ch6/Ch7 实测案例（含 prompt+输出）
- **S2/S3 BenDavis** — Ch5.3/Ch7 长文本退化、Ch5.2 Computer Use
- **S9 WXArticle5** — Ch1 范式转变论述

### T6 级（厂商声明，仅作参照/被验证对象）
- **S5/S4/S9** — 基准数据可作为独立测试的"待验证声明"
- **S6 WXArticle2** — 安全评估数据可作为 Ch9 的厂商声称对照

---

## 六、白皮书撰写顺序建议

基于各章节的数据可用性：

1. **先写 Ch2/Ch4**（方法论+指标）— 用 S11(AA 方法论) + S9(范式转变) 定调
2. **再写 Ch6/Ch8**（竞品对比+成本）— S11(AA)+S8(实测)+S10(AA成本) 数据最充分
3. **接着 Ch7**（失败案例）— S11(86%幻觉)+S8(实测案例)+S2(长文本退化)+S6(安全退步) 四重支撑
4. **然后 Ch5**（核心能力）— 按子章节从各来源交叉引用
5. **再写 Ch1/Ch9**（背景+安全）— S9(范式转变)+S5/S6(安全数据)
6. **最后 Ch0/Ch10/Ch11**（摘要+建议+局限）— 综合全报告后提炼