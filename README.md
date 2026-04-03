<div align="center">

# 赛博HR.skill

> *"把 HR 蒸馏进系统，让招聘、评估与组织记忆继续在线。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

同事离职了，知识断档；招聘忙不过来，面试标准飘忽；
组织一换人，HR 话术、判断标准、候选人洞察就跟着散了。<br>
那不如把 **HR 蒸馏进系统**。<br>

**赛博HR.skill** 用聊天记录、面试纪要、招聘话术、制度文档、绩效评语等原材料，
构建一个可运行的 **CyberHR 数字分身**。它既能延续某位 HR 的判断风格，也能组建 **HR Agent Team**，承担自动面试、自动筛人、自动评估等任务。

[安装](#安装) · [使用](#使用) · [核心能力](#核心能力) · [English](README_EN.md)

</div>

---

## 这是什么

这是一个把 `yourself-skill` 改造成 **赛博HR / 数字HR / HR数字永生系统** 的版本。

输出结构不再是“自我镜像”，而是：

- **Part A — HR Memory**：招聘理念、用人标准、制度边界、组织经验、候选人判断框架
- **Part B — HR Persona**：沟通风格、追问方式、风险偏好、文化匹配口径、反馈语气
- **Part C — HR Agent Team**：把单个 CyberHR 扩展为招聘官、面试官、HRBP、评估官等分工协作的军团

这样做的目标不是“假装真人”，而是把组织里高价值的 HR 判断经验沉淀成可调用、可迭代、可回滚的 Skill。

---

## 核心能力

### 1. HR 数字永生

把某位 HR 的人格、方法论和判断口径蒸馏成 CyberHR：

```text
HR 人格 → CyberHR
```

当原 HR 转岗、离职、退休，组织仍可继续调用其经验资产。

### 2. HR 军团

一个人不够，就组队：

```text
HR Agent Team
├── recruiter      # 招聘官：负责吸引与初筛
├── interviewer    # 面试官：负责追问与结构化面试
├── evaluator      # 评估官：负责打分与风险分析
└── hrbp           # HRBP：负责组织匹配、用工边界、落地建议
```

### 3. 自动面试

根据岗位 JD、简历和候选人回答，自动生成：

- 结构化问题清单
- 深挖追问链路
- 面试纪要
- 多维打分与录用建议

### 4. 自动筛人

根据岗位要求、简历、项目经历与风险信号，输出：

- 匹配度摘要
- 强项 / 短板
- 必问问题
- 淘汰风险与保留建议

### 5. 自动评估

支持：

- 候选人综合评估
- 文化匹配评估
- 试用期表现评估
- 绩效反馈话术生成

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/YOUR_USERNAME/cyber-hr-skill .claude/skills/create-cyber-hr

# 或安装到全局
mkdir -p ~/.claude/skills
git clone https://github.com/YOUR_USERNAME/cyber-hr-skill ~/.claude/skills/create-cyber-hr
```

### 依赖（可选）

```bash
pip install -r requirements.txt
```

---

## 使用

在 Claude Code 中输入：

```text
/create-cyber-hr
```

然后按提示依次提供：

1. **HR 代号 / 名称**
2. **HR 基本信息**（岗位、行业、年限、组织类型）
3. **HR 风格画像**（强势/温和、数据驱动/直觉驱动、重文化匹配/重硬能力）

接着导入原材料：

- 面试记录 / 面试转录
- 招聘聊天记录（微信、QQ、邮件摘录等）
- Offer 沟通话术
- 绩效评语 / 评价模板
- 制度、手册、招聘 SOP
- 用户直接口述

生成完成后，可以用以下命令调用：

| 命令 | 说明 |
|------|------|
| `/list-hrs` | 列出所有 CyberHR |
| `/{slug}` | 完整 CyberHR（含记忆 + 人格 + 能力） |
| `/{slug}-memory` | 仅查看 HR Memory |
| `/{slug}-persona` | 仅查看 HR Persona |
| `/{slug}-team` | 以 HR Agent Team 方式工作 |
| `/cyber-hr-rollback {slug} {version}` | 回滚历史版本 |
| `/delete-cyber-hr {slug}` | 删除 |

---

## 原材料建议

优先级从高到低：

1. **真实面试记录**：最能暴露追问方式、风险判断和评价标准
2. **招聘沟通记录**：最能体现沟通风格、候选人运营和话术边界
3. **绩效评语 / 复盘纪要**：最能体现评估框架和组织价值观
4. **制度与流程文件**：最能校准合规边界与组织口径
5. **个人口述**：补足“为什么这么判断”

---

## 生成后的目录结构

```text
create-cyber-hr/
├── SKILL.md
├── prompts/
│   ├── intake.md
│   ├── hr_memory_analyzer.md
│   ├── hr_persona_analyzer.md
│   ├── hr_memory_builder.md
│   ├── hr_persona_builder.md
│   ├── merger.md
│   └── correction_handler.md
├── tools/
│   ├── wechat_parser.py
│   ├── qq_parser.py
│   ├── social_parser.py
│   ├── photo_analyzer.py
│   ├── skill_writer.py
│   └── version_manager.py
├── selves/
│   └── example_hr/
├── docs/PRD.md
├── requirements.txt
└── LICENSE
```

---

## 适合的场景

- 招聘团队经验沉淀
- 核心 HR 离职前的知识蒸馏
- 多岗位自动面试
- 校招 / 社招简历初筛
- 结构化评估报告生成
- HRBP 组织沟通口径沉淀
- “数字祠堂式”的 HR 档案馆 / 赛博纪念堂

---

## 注意事项

- 这不是法律意见系统，劳动合规、薪酬、隐私、反歧视等高风险问题仍需人工审查。
- 原材料质量决定还原度；没有真实面试和评估文本，生成结果会更像“概念 HR”，不像“能干活的 HR”。
- CyberHR 应被视为 **组织经验放大器**，而不是无责任替代者。
- 对外使用前，建议先做内部灰度验证，校验其提问风格、结论稳定性和偏差风险。

---

## 致谢

本项目沿用了这些 skill 的灵感与结构脉络：

- colleague skill
- ex-partner skill
- yourself skill

并感谢以下工具与模型在改造过程中的帮助：

- GPT-5.4
- Claude Code
- VSCode

同时也感谢 AgentSkills 开放标准提供的兼容生态。

---

## 一句话总结

**赛博HR.skill = 把 HR 的经验、口径与判断蒸馏成可运行的数字分身，并进一步扩展成可协作的 HR Agent Team。**
