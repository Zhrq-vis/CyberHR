---
name: create-cyber-hr
description: "Distill an HR persona into a runnable CyberHR with digital immortality, HR Agent Team orchestration, automated interviewing, screening, and evaluation. | 把 HR 蒸馏成可运行的赛博HR，支持数字永生、HR军团、自动面试、自动筛人、自动评估。"
argument-hint: "[hr-name-or-slug]"
version: "2.0.0"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

> **Language / 语言**: Detect the user's first-message language and stay in that language throughout.
>
> 本 Skill 支持中英文。根据用户第一条消息的语言，全程保持同语言回复。

# 赛博HR.skill 创建器（Claude Code 版）

## 触发条件

当用户说以下内容时启动：
- `/create-cyber-hr`
- “帮我创建一个赛博HR skill”
- “我想把 HR 蒸馏成 skill”
- “做一个数字HR”
- “做一个 HR 数字分身”

当用户对已有 CyberHR 说以下内容时，进入进化模式：
- “我有新面试记录” / “追加文件” / “补充评语”
- “这不像 TA 的风格” / “这句 HR 不会这么说” / “标准不对”
- `/update-cyber-hr {slug}`

当用户说 `/list-hrs` 时列出所有已生成的 CyberHR。

## 工具使用规则

| 任务 | 使用工具 |
|------|----------|
| 读取 PDF / 图片 / 文档 | `Read` |
| 读取 MD / TXT | `Read` |
| 解析微信聊天记录 | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/wechat_parser.py` |
| 解析 QQ 聊天记录 | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/qq_parser.py` |
| 扫描社交媒体/截图目录 | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/social_parser.py` |
| 分析照片或截图时间线 | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/photo_analyzer.py` |
| 写入/更新 Skill 文件 | `Write` / `Edit` |
| 版本管理 | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/version_manager.py` |
| 列出 CyberHR | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/skill_writer.py --action list` |
| 合并生成 SKILL.md | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/skill_writer.py --action combine` |

**目标目录**：生成的 Skill 必须写入 `./.claude/skills/{slug}/`。

## 主流程：创建新 CyberHR

### Step 1：基础信息录入（3 个问题）

参考 `${CLAUDE_SKILL_DIR}/prompts/intake.md`，只问 3 个问题：
1. HR 代号 / 名称
2. HR 基本信息
3. HR 风格画像

### Step 2：原材料导入

可混用：
- 面试记录 / 面试转录
- 招聘沟通记录（微信 / QQ / 文本）
- Offer / 绩效 / 评价话术
- 制度 / 流程 / 手册 / SOP
- 照片 / 截图 / PDF / 文本文件
- 直接口述

### Step 3：分析原材料

**线路 A：HR Memory**  
参考 `${CLAUDE_SKILL_DIR}/prompts/hr_memory_analyzer.md`，提取招聘理念、能力模型、文化匹配标准、风险边界、组织经验、岗位画像。

**线路 B：HR Persona**  
参考 `${CLAUDE_SKILL_DIR}/prompts/hr_persona_analyzer.md`，提取提问风格、追问节奏、沟通语气、打分偏好、判断阈值、反馈方式。

同时拆出 **HR Agent Team**：`recruiter / interviewer / evaluator / hrbp`。

### Step 4：生成并预览

参考：
- `${CLAUDE_SKILL_DIR}/prompts/hr_memory_builder.md`
- `${CLAUDE_SKILL_DIR}/prompts/hr_persona_builder.md`

摘要至少包含：
- 招聘理念
- 风格画像
- 风险边界
- recruiter/interviewer/evaluator/hrbp 的角色定义

### Step 5：写入文件

生成文件：
- `.claude/skills/{slug}/hr_memory.md`
- `.claude/skills/{slug}/hr_persona.md`
- `.claude/skills/{slug}/team.json`
- `.claude/skills/{slug}/meta.json`
- `.claude/skills/{slug}/SKILL.md`

推荐命令：

```bash
python ${CLAUDE_SKILL_DIR}/tools/skill_writer.py \
  --action create \
  --slug {slug} \
  --base-dir ./.claude/skills \
  --meta /tmp/cyber_hr_{slug}/meta.json \
  --memory /tmp/cyber_hr_{slug}/hr_memory.md \
  --persona /tmp/cyber_hr_{slug}/hr_persona.md \
  --team /tmp/cyber_hr_{slug}/team.json
```

## 进化模式：追加文件

1. 读取新文件
2. 读取现有 `hr_memory.md`、`hr_persona.md`、`team.json`
3. 参考 `${CLAUDE_SKILL_DIR}/prompts/merger.md` 做增量 merge
4. 先备份：

```bash
python ${CLAUDE_SKILL_DIR}/tools/version_manager.py --action backup --slug {slug} --base-dir ./.claude/skills
```

5. 重新 combine：

```bash
python ${CLAUDE_SKILL_DIR}/tools/skill_writer.py --action combine --slug {slug} --base-dir ./.claude/skills
```

## 进化模式：对话纠正

当用户说“这不像 TA”“这个 HR 不会这么说”“标准不对”时：
- 参考 `${CLAUDE_SKILL_DIR}/prompts/correction_handler.md`
- 判断属于 HR Memory / HR Persona / Team 哪一层
- 写入 correction 记录
- 重新生成 `SKILL.md`

## 管理命令

`/list-hrs`
```bash
python ${CLAUDE_SKILL_DIR}/tools/skill_writer.py --action list --base-dir ./.claude/skills
```

`/cyber-hr-rollback {slug} {version}`
```bash
python ${CLAUDE_SKILL_DIR}/tools/version_manager.py --action rollback --slug {slug} --version {version} --base-dir ./.claude/skills
```

`/delete-cyber-hr {slug}`
```bash
rm -rf ./.claude/skills/{slug}
```

# English Version

The generated CyberHR must support:
1. **HR Digital Immortality** — HR persona → CyberHR
2. **HR Agent Team** — recruiter / interviewer / evaluator / hrbp collaboration
3. **Automated Interviewing**
4. **Automated Screening**
5. **Automated Evaluation**
