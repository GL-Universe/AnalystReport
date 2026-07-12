# OpenAI's GPT-5.5 is the new leading AI model — Artificial Analysis 文章大纲

> 来源: Artificial Analysis (独立 AI 评测机构), 发布时间约 2026-04-23
> 原文链接: https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model/
> 特别说明: OpenAI 给予 AA 预发布权限测试了全部 5 个推理强度级别(xhigh/high/medium/low/non-reasoning)

---

## 一、总体排名

### 1.1 Intelligence Index
- GPT-5.5 在 Artificial Analysis 智力指数上**领先 3 分**
- 打破了之前 Anthropic、Google、OpenAI 的三方持平局面
- 确认 GPT-5.5 是世界顶级独立验证模型

### 1.2 五项评测领先
- Terminal-Bench Hard (终端指令排错)
- GDPval-AA (真实职业任务)
- APEX-Agents-AA (代理能力,AA 新托管的基准)
- CritPt 仅落后其他 OpenAI 模型
- AA-LCR 仅落后其他 OpenAI 模型

### 1.3 与 Gemini 3.1 Pro Preview 对比
- Gemini 3.1 Pro Preview 在三项额外评测中领先 GPT-5.5

---

## 二、关键增益

### 2.1 AA-Omniscience (+14 分)
- 知识和幻觉基准
- 最大增益项

### 2.2 τ²-Bench Telecom (+7 分)
- 客服代理基准
- 显著提升

---

## 三、推理努力度阶梯(Effort Ladder)

### 3.1 五级推理努力
- GPT-5.5 提供 xhigh / high / medium / low / non-reasoning 五种推理强度
- 每个级别在智力和成本之间形成清晰阶梯

### 3.2 关键对比数据
| 对比 | 智力匹配 | 成本对比 |
|------|---------|---------|
| GPT-5.5 (Medium) vs Opus 4.7 (Max) | 相同 | 1/4 成本 (~$1,200 vs $4,800) |
| GPT-5.5 (Low) vs Opus 4.7 (Non-reasoning, High) | 相近 | 1/2 成本 (~$500 vs ~$1,000) |
| Gemini 3.1 Pro Preview | 相同智力 | 更便宜 (~$900) |

---

## 四、成本分析

### 4.1 Token 定价
- GPT-5.5: $5/$30 每百万 token (比 GPT-5.4 翻倍)

### 4.2 Token 使用效率
- **~40% 更少输出 token** 完成相同 Index(相比 GPT-5.4)
- 这几乎完全吸收了涨价

### 4.3 净成本影响
- 运行 AA Intelligence Index 的成本仅增加 **~+20%**
- 比 Claude Opus 4.7 (Max) 便宜 **30%**

---

## 五、GDPval-AA 排行

### 5.1 Elo 分数
- GPT-5.5 (xhigh): **1785 Elo**
- 领先 Claude Opus 4.7 (Max): **约 30 分**
- 领先 Gemini 3.1 Pro Preview: **约 470 分**

### 5.2 基准说明
- 基于 OpenAI 的 GDPval 数据集
- 评估模型在真实世界有经济价值的任务上的表现

---

## 六、AA-Omniscience: 知识 vs 幻觉

### 6.1 GPT-5.5 的最高知识准确率
- **57% 准确率**(所有模型中最高的知识召回能力)
- 能最有效地回忆 Omniscience 语料库中的事实

### 6.2 幻觉问题
- GPT-5.5 (xhigh) 幻觉率: **86%**
- Claude Opus 4.7 (Max): **36%**
- Gemini 3.1 Pro Preview: **50%**
- **含义**: GPT-5.5 更倾向于在不确定时仍回答问题(而不是说"我不知道")
- 这是 AA 独立测试中暴露的最大弱点

### 6.3 与前代对比
- 相比 GPT-5.4 (xhigh), 14 分 GAIN 主要来自知识提升
- 幻觉改善微弱

---

## 七、关键结论

1. GPT-5.5 在 AI 智力指数上确认为世界第一,打破三方持平
2. 推理努力度阶梯让用户可按需平衡智力与成本
3. Medium 推理即可与 Opus 4.7 Max 匹敌,成本仅 1/4
4. Token 效率提升 ~40% 基本吸收涨价,实际成本仅增 20%
5. **幻觉率高达 86% 是最大短板**,远超 Claude 和 Gemini
6. AA-Omniscience 的知识准确率最高但可靠性仍需改善

---

## 白皮书章节映射

> 对照目标: [GPT5.5outline.md](../reports-md/GPT5.5outline.md)

| 白皮书章节 | 可支撑内容 | 证据类型 |
|-----------|----------|---------|
| **Ch0 执行摘要** | Intelligence Index领先3分（打破三方持平）；核心矛盾数字：最高知识准确率57% vs 幻觉率86%；Token效率~40%更少；成本仅增~20% | **T3独立评测** |
| **Ch1 研究背景与问题** | 独立验证打破Anthropic/Google/OpenAI三方持平局面；GPT-5.5被认证为世界顶级独立验证模型；现有benchmark的局限（厂商声称 vs 独立实测） | **T3独立评测** |
| **Ch4 评估指标体系** | 推理努力度阶梯（xhigh/high/medium/low/non-reasoning五级）作为评测变量设计的参考；Intelligence Index评分方法论；AA-Omniscience知识vs幻觉的双维度测量方法 | **T3评测方法论** |
| **Ch5.1 事实性推理与知识** | GDPval-AA Elo 1785（领先Opus 4.7 Max约30分、Gemini 3.1 Pro Preview约470分）；AA-Omniscience最高知识准确率57%（所有模型最高）；五项评测领先（Terminal-Bench Hard、GDPval-AA、APEX-Agents-AA等） | **T3独立评测** |
| **Ch6.1 总体对比矩阵** | Intelligence Index排名（GPT-5.5第一、领先3分）；五级推理强度 vs 竞品的完整智力/成本对比数据 | **T3独立评测** |
| **Ch6.2 实质优势场景** | AA-Omniscience +14分（知识准确率最大增益）；τ²-Bench Telecom +7分（客服代理显著提升）；GDPval-AA 1785 Elo显著领先 | **T3独立评测** |
| **Ch6.3 劣势场景** | Gemini 3.1 Pro Preview 在三项额外评测中领先 GPT-5.5 | **T3独立评测** |
| **Ch6.4 成本-效果权衡** | 推理努力度阶梯的智力/成本对比表；GPT-5.5 (Medium) = Opus 4.7 (Max)智力但1/4成本；GPT-5.5 (Low) ≈ Opus 4.7 (Non-reasoning High) 但1/2成本 | **T3独立评测** |
| **Ch7 失败案例** | **核心发现：GPT-5.5幻觉率86%** (vs Claude Opus 4.7 36%、Gemini 3.1 Pro 50%)——AA独立测试中暴露的最大弱点；评分标准：知识提升+14分但幻觉改善微弱（前代对比） | **T3独立评测** |
| **Ch8.2 实际任务成本** | Token效率~40%更少输出token（相比GPT-5.4）；净成本仅增~20%；比Claude Opus 4.7 (Max)便宜30% | **T3独立评测** |
| **Ch8.4 成本效率比** | 运行AA Intelligence Index的完整成本对比数据；推理努力度阶梯允许用户按需平衡智力与成本 | **T3独立评测** |
| **Ch10.1 使用场景推荐** | 推理模式配置建议（Medium推理即可匹敌Opus 4.7 Max，可节省75%成本） | **T3独立评测** |

> **总体评价**: 本文是 **所有来源中权威性最高的独立评测数据（T3级别）**。为白皮书 Ch0（执行摘要核心数字）、Ch4（评估指标——推理努力度阶梯）、Ch6（竞品对比矩阵+成本权衡）、Ch7（失败案例——86%幻觉率的核心发现）和 Ch8（成本分析）提供最关键的量化证据。**幻觉率86% vs Opus 36%的对比数据是白皮书 Ch7 的核心引用**，必须在报告中被重点突出。AA方法论（多推理级别测试+Intelligence Index）可直接作为白皮书 Ch2 方法论设计的参照。