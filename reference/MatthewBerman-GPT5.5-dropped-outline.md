# OpenAI just dropped GPT-5.5.. (WOAH) — Matthew Berman 视频大纲

> 来源: YouTube (Matthew Berman频道), 发布时间约 2026-04-23
> 原始字幕文件: `reference/[English (auto-generated)] OpenAI just dropped GPT-5.5.. (WOAH) [DownSub.com].txt`

---

## 一、发布概述

### 1.1 发布信息
- OpenAI 官方发布 GPT-5.5
- 定位: "A new class of intelligence for real work"
- 在 Codex 和 ChatGPT 中提供

### 1.2 定价
- $5/M 输入 token, $30/M 输出 token
- Pro 版: $30/$180
- 价格是 GPT-5.4 的 2 倍

---

## 二、核心基准测试成绩

### 2.1 编码相关
- **Terminal-Bench 2.0**: 82.7% (在终端命令执行和调试上的统治级表现)
- **SWE-Bench Pro**: 58.6% (真实软件工程任务)
- **Expert-SWE**: 73.1% (专业级 SWE)
- Matthew Berman 推测 Codex + GPT-5.5 在这个基准上会达到 90%+

### 2.2 知识工作
- **GDPval**: 84.9% (真实职业任务评估,包括分析数据、写报告、做判断)
- **OSWorld**: 78.7% (真实 OS 环境中的操作能力)
- 从"给答案"到"动手做"的转变

### 2.3 搜索/推理
- **BrowseComp**: 84.4% (网页浏览和信息检索)
- **FrontierMath Tier 1–3**: 51.7%

### 2.4 安全相关
- **CyberGym**: 81.8% (网络安全)
- 生物/化学安全评估: GPT-5.5 被评为 **High** 风险(首次)

---

## 三、与 Claude Opus 4.7 的对比

### 3.1 基准对比
- Terminal-Bench 2.0: GPT-5.5 82.7% vs Opus 4.7 显著较低
- SWE-Bench Pro: GPT-5.5 58.6% vs Opus 4.7 仍领先
- OSWorld: GPT-5.5 78.7% vs Opus 4.7 较低

### 3.2 总体评价
- GPT-5.5 在多数基准上领先但优势并非碾压级
- Codex 集成让 GPT-5.5 的实际使用体验远好于纯 API 调用

---

## 四、Token 效率

### 4.1 关键创新
- 与之前的模型相比,相同任务的 token 使用量减少 20-40%
- 效率源于模型更好地理解用户意图 → 更精准的输出
- 速度与 GPT-5.4 基本持平

### 4.2 成本分析
- 每个 token 价格翻倍,但总 token 消耗降低
- 实际净成本增加约 20%
- 但任务完成质量同时提升

---

## 五、视觉检测(Vision)改进

### 5.1 Visual Inspection 增强
- 展示 cluttered desk 照片 → 指出"第二本书下面压着钥匙"
- 比 GPT-5.4 的视觉理解能力有"step-function" 提升
- 可用于 UI 审查和图像分析等场景

### 5.2 实际应用
- UI 视觉检查(布局是否合理、是否有 UI bug)
- 医学图像分析(已集成到 Box AI 中)

---

## 六、与硬件协同

### 6.1 英伟达 GB200/GB300 合作
- GPT-5.5 在英伟达最新硬件上共同设计/优化
- 推理性能提升显著
- GB200 NVL72 机架: 72 GPU 通过高速连接

### 6.2 "模型帮助改进推理栈"
- GPT-5.5 自身参与了自己的推理系统优化
- 这标志着一个新的发展模式: 模型自我改进

---

## 七、Box AI 集成演示

### 7.1 企业集成
- Box 立即演示了 GPT-5.5 在文件管理中的使用
- 自动扫描、分类、提取信息、生成摘要
- 企业级别的内容智能

---

## 八、安全与防护

### 8.1 防护框架升级
- 最严格的一代 AI 模型
- 多项安全评估: 生物、网络、说服力
- 近 200 个真实场景安全测试

### 8.2 API 延迟
- API 延迟上线,等待更多安全防护到位
- ChatGPT/Codex 首周可用

---

## 九、关键结论

1. GPT-5.5 在多个基准上超越了所有其他模型
2. Token 效率是最大亮点: 更少 token 完成更好工作
3. 价格翻倍但效率同步提升,实际成本增加不大
4. Codex 捆绑是 OpenAI 的战略重心
5. 这是"AI 推理公司"转型的重要一步

---

## 白皮书章节映射

> 对照目标: [GPT5.5outline.md](../reports-md/GPT5.5outline.md)

| 白皮书章节 | 可支撑内容 | 证据类型 |
|-----------|----------|---------|
| **Ch0 执行摘要** | 核心基准数字（Terminal-Bench 82.7%、SWE-Bench Pro 58.6%、GDPval 84.9%、OSWorld 78.7%、CyberGym 81.8%） | T6 厂商发布数据 |
| **Ch1 研究背景与问题** | GPT-5.5官方定位声明（"A new class of intelligence for real work"）；发布渠道（ChatGPT + Codex, API延迟）；OpenAI向"AI推理公司"转型 | T6 厂商声明 |
| **Ch5.1 事实性推理** | BrowseComp 84.4%（网页浏览/信息检索）；FrontierMath Tier 1-3 51.7% | T6 厂商基准数据 |
| **Ch5.2 代码生成能力** | Terminal-Bench 82.7%；SWE-Bench Pro 58.6%；Expert-SWE 73.1%；Matthew Berman推测Codex+GTP-5.5可达90%+ | T6厂商数据+T5专家推测 |
| **Ch5 知识工作** | GDPval 84.9%（44种真实职业任务）；OSWorld 78.7%（真实OS环境操作）；从"给答案"到"动手做"的范式转变 | T6 厂商基准数据 |
| **Ch5 多模态/视觉** | Visual Inspection step-function提升（cluttered desk图像→定位钥匙）；UI审查应用；Box AI医疗图像分析集成 | T5 用户演示体验 |
| **Ch6.1 总体对比矩阵** | GPT-5.5 vs Claude Opus 4.7: Terminal-Bench显著领先，SWE-Bench Pro领先，OSWorld领先；总体评价：多数基准领先但非碾压 | T5 用户对比分析 |
| **Ch8.1 API定价** | GPT-5.5 $5/$30, Pro $30/$180（GPT-5.4的2倍） | T6 厂商官方价格 |
| **Ch8.2 实际任务成本** | Token效率：完成相同任务使用减少20-40% token；实际净成本仅增约20%；速度与GPT-5.4持平 | T5 用户效率分析 |
| **Ch8.4 成本效率比** | 每token价格翻倍但总token消耗降低 → 净成本增约20%（效率基本吸收涨价） | T5 用户成本分析 |
| **Ch9.1 安全评估** | 生物/化学安全首次被评"High"风险；CyberGym 81.8%；近200个真实场景安全测试 | T6 厂商安全声明 |
| **Ch9.2 有害内容/防护** | 当前防护最严格的一代模型；API延迟等待额外安全防护到位 | T6 厂商声明 |

> **总体评价**: 本文是 GPT-5.5 官方发布后最全面的解读之一，为白皮书 Ch0（执行摘要）、Ch5（核心评测-多维度基准数据）、Ch8（成本）和 Ch9（安全）提供大量可引用的基准数据和官方声明。但所有数据来自厂商发布（T6级别），白皮书需通过独立测试验证后方可引用。