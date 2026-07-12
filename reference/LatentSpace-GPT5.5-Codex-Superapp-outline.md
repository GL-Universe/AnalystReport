# [AINews] GPT 5.5 and OpenAI Codex Superapp — Latent Space 文章大纲

> 来源: Latent Space (Substack), 发布时间约 2026-04-22/23
> 原文链接: https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp
> 作者注: 这是 AINews 每日 AI 新闻摘要,涵盖 GPT-5.5 发布及当天的所有重要行业动态

---

## 一、GPT-5.5 发布：核心分析

### 1.1 与 Claude Opus 4.7 的对比框架
- Opus 4.7 发布一周后,OpenAI 回击
- 类似"Pareto 前沿改善"图表(Noam Brown 推崇的 2D 智力/美元图)
- 在 4.7 vs 5.5 对比中,**编码基准被刻意未提及**(暗示这一块差距不大)

### 1.2 Artificial Analysis 独立验证
- GPT-5.5 被 AA 认证为世界顶级独立验证模型
- **"智力/美元"关键数据**:
  - GPT-5.5 (Medium): 与 Opus 4.7 (Max) 同等智力,成本仅 1/4 (~$1,200 vs $4,800)
  - Gemini 3.1 Pro Preview: 同等智力,成本仅 ~$900
- 训练硬件: 与英伟达 GB200/300 协同设计

### 1.3 不是单纯的模型升级
- "有人更想叫它 GPT-5.9"
- **这是更大的 Codex 发布日**(捆绑发布):
  - 浏览器控制 (browser control)
  - Sheets/Slides 集成
  - Docs/PDFs 支持
  - OS 级语音输入
  - Auto-review 模式
- Prism(前身产品)被淘汰,Codex 成为超级应用战略基础

---

## 二、GPT-5.5 详细参数

### 2.1 基准测试得分
| 基准 | 分数 |
|------|------|
| Terminal-Bench 2.0 | 82.7% |
| SWE-Bench Pro | 58.6% |
| GDPval | 84.9% |
| OSWorld-Verified | 78.7% |
| CyberGym | 81.8% |
| BrowseComp | 84.4% |
| FrontierMath Tier 1-3 | 51.7% |

### 2.2 定价与上下文
- GPT-5.5: $5/$30 (输入/输出)
- GPT-5.5 Pro: $30/$180
- API 上下文窗口: **1M token**(Sam Altman 确认)
- 每任务 token 使用量比 5.4 更少

### 2.3 实际行为
- 用户报告: 更"人性化"、更不拘形式
- 更适合持久化代理工作流(尤其在 Codex 中)
- 自主性的阶跃提升,但也需要更严格的指令来保持方向

### 2.4 Sam Altman 定位
- OpenAI 正成为 **AI 推理公司**
- 推理栈由模型自身协助优化

### 2.5 Codex 升级为完整代理工作空间
- 浏览器控制: 可以操作 Web 应用、点击流程、截图、迭代直到完成
- Auto-review: 辅助"守护者"代理减少长时间运行的审批需求
- 从编码工具扩展为**通用电脑工作代理**: QA、电子表格、演示文稿、应用构建、研究循环、通宵实验运行

---

## 三、DeepSeek-V4 Preview(同日发布)

### 3.1 关键规格
- **GPT-5.5 发布数小时内** DeepSeek 即回应
- **MIT 许可证**开源! (V4-Pro 和 V4-Flash)
- V4-Pro: **1.6T 总参数 / 49B 激活参数**
- V4-Flash: 284B / 13B 激活
- 两者均支持 **1M token 上下文**
- 支持思考/非思考模式

### 3.2 技术亮点
- 两个新压缩/混合注意力机制
- mHC 架构
- Muon 训练
- FP4 量化感知训练
- 预训练约 32T token
- **1M 上下文实用化**: ~4x 计算效率提升,数量级 KV-cache 缩减
- vLLM 和 SGLang 均宣布 Day-0 支持

### 3.3 激进定价
- **V4-Flash: $0.14/$0.28** (输入/输出)
- **V4-Pro: $1.74/$3.48**
- Flash 如果服务稳定可能是更颠覆性的 SKU
- V4-Pro 吞吐量目前受限于高端计算资源(指向未来的 Ascend 950 芯片)

---

## 四、代理基础设施与工具

### 4.1 代理的系统化问题
- 生产代理越来越是 **harnesses、评估、记忆和编排**的问题,不只是模型问题
- **无状态决策记忆**: 不可变决策日志/事件溯源替代可变状态(提升水平扩展、可审计性、容错)
- 代理改进飞轮: 跟踪数据 → 评估/环境 → Harness 工程/SFT-RL
- Claude Code 质量回归案例(因3个问题 v2.1.116+ 修复),说明开放 harness 和开放评估的重要性

### 4.2 新工具
- **Cua Driver** 开源: macOS 驱动,让代理后台控制任意应用(多用户/多光标)
- **Cognition** 云代理基础设施栈: VM 隔离、会话持久化、环境配置、编排、集成
- **LangSmith Fleet**: 文件编辑、网页/演示文稿生成、斜杠命令技能

### 4.3 多代理编排产品化
- **Sakana AI Fugu**: 多代理编排 API,动态选择和协调前沿模型,声称 SWE-Pro/GPQA-D/ALE-Bench SOTA,支持递归测试时扩展
- **Hermes Agent v0.11.0**: 扩展供应商、图像生成、GPT-5.5 立即支持
- 趋势: 代理正在成为异构工具和模型的**编排层**

---

## 五、视觉、视频与多模态系统

### 5.1 Vision Banana(Google DeepMind)
- 统一视觉模型,将 2D/3D 视觉任务作为图像生成处理
- 在分割、深度、法线等任务上超越专业 SOTA
- 信号: 计算机视觉正转向统一生成式范式

### 5.2 Sapiens2(Meta)
- 高分辨率视觉 Transformer,在 10 亿人像上训练

### 5.3 LTX HDR Beta
- AI 视频的真正瓶颈是**动态范围**而非分辨率
- 超越 8-bit SDR,可经受调色和合成

### 5.4 Omni Models
- 统一的文本+图像+视频+3D几何+隐藏表征模型
- 推理过程在多模态间展开

---

## 六、训练、扩展与研究方法

### 6.1 Decoupled DiLoCo(Google)
- 解耦分布式低通信训练
- 实现全球数据中心训练、异构硬件、故障容忍
- 解决真正的顶级训练瓶颈

### 6.2 算法扩展
- Self-play 研究: 7B 模型解决与 **100 倍更大模型 pass@4** 相同数量的问题
- Token/计算效率被视为真正的顶级指标

### 6.3 基础设施信号
- Together AI: 从每月 300 亿 → 300 万亿 token (年同比增长)
- Stargate Abilene: ~0.3 GW 当前,1.2 GW 里程碑推迟至 Q4 2026

---

## 七、当日最热门推文

1. OpenAI GPT-5.5 发布(最高互动)
2. Claude Code 质量回归事后分析(Anthropic 承认三个问题并修复)
3. DeepSeek-V4 Preview 发布(MIT 许可证 + 1M 上下文 + 激进定价)
4. Vision Banana(纯研究视觉岗位)
5. ML-Intern 15 分钟通过实习风格测试(高 token 消费引发关注)

---

## 八、关键结论

1. GPT-5.5 不只是模型升级,Codex 超级应用是更大的叙事
2. DeepSeek-V4 同日以 MIT 许可证回应,开放模型与封闭模型的竞争加剧
3. 代理从模型问题演变为系统工程问题(编排/评估/记忆)
4. 1M 上下文正从"噱头"变为实用功能
5. AI 行业从单模型比较转向"智力/美元"的二维竞争

---

## 白皮书章节映射

> 对照目标: [GPT5.5outline.md](../reports-md/GPT5.5outline.md)

| 白皮书章节 | 可支撑内容 | 证据类型 |
|-----------|----------|---------|
| **Ch1 研究背景与问题** | GPT-5.5 发布背景（Opus 4.7发布一周后OpenAI回击）；Codex超级应用战略（捆绑发布浏览器控制/Sheets/Slides/Docs/OS语音/auto-review）；DeepSeek-V4同日发布的竞争加剧；AI行业从单模型比较→"智力/美元"二维竞争的范式转变 | T5行业深度分析 |
| **Ch2 方法论** | Artificial Analysis独立评测方法论作为方法论设计参照（Intelligence Index + 多推理级别测试） | T3独立评测 |
| **Ch5.2 代码生成能力** | Terminal-Bench 82.7%、SWE-Bench Pro 58.6%、Expert-SWE 73.1%；Codex升级为完整代理工作空间（浏览器控制/auto-review/QA/电子表格/演示文稿/通宵实验） | T6厂商基准+T5分析 |
| **Ch6.1 总体对比矩阵** | GPT-5.5 (Medium) vs Opus 4.7 (Max): 同等智力,成本仅1/4(~$1,200 vs $4,800)；Gemini 3.1 Pro Preview同等智力成本~$900；编码基准被刻意未提及暗示差距不大 | T3独立评测+T5分析 |
| **Ch6.4 成本-效果权衡** | "智力/美元"二维Pareto前沿图表概念（Noam Brown推崇）；AA认证GPT-5.5为世界顶级独立验证模型 | T3独立评测 |
| **Ch8.1 API定价** | $5/$30（GPT-5.5）、$30/$180（Pro）；API上下文窗口1M token（Sam Altman确认） | T6厂商价格+T6厂商声明 |
| **Ch8.4 成本效率比** | Medium推理级别成本仅为Opus 4.7 Max的1/4达成同等智力 | T3独立评测 |
| **Ch10.1 使用场景推荐** | Codex从编码工具→通用电脑工作代理（浏览器控制/auto-review/QA/Slides/研究循环等场景） | T5场景分析 |

> **总体评价**: 本文的核心价值在于提供 **AA独立验证（T3级别）的"智力/美元"成本对比数据**，这对白皮书 Ch6.4（成本效果权衡）和 Ch8（成本效益分析）至关重要。同时，将GPT-5.5置于Codex超级应用叙事中，为 Ch1（行业背景——从模型到平台的转型）提供战略层面解读。DeepSeek-V4并行发布为竞品对比提供额外参照。