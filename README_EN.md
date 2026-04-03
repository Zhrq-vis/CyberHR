<div align="center">

# CyberHR.skill

> *"Distill HR into a living system so hiring judgment and organizational memory stay online."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

People leave. Hiring standards drift. Organizational memory disappears with each HR turnover.<br>
So instead of losing that experience, **distill HR into a system**.<br>

**CyberHR.skill** turns interview notes, recruiting chats, offer scripts, feedback documents, and policy files into a runnable **CyberHR digital replica**—and can scale that into an **HR Agent Team** for automated interviewing, candidate screening, and evaluation.

[Installation](#installation) · [Usage](#usage) · [Core Capabilities](#core-capabilities) · [中文](README.md)

</div>

---

## What it is

This is a CyberHR adaptation of the original `yourself-skill` architecture.

It produces:

- **Part A — HR Memory**
- **Part B — HR Persona**
- **Part C — HR Agent Team**

---

## Core Capabilities

### 1. HR Digital Immortality

```text
HR persona → CyberHR
```

### 2. HR Agent Team

```text
HR Agent Team
├── recruiter
├── interviewer
├── evaluator
└── hrbp
```

### 3. Automated Interviewing

CyberHR can generate structured questions, follow-up chains, interview notes, and scores.

### 4. Automated Screening

CyberHR can output fit summaries, strengths, weaknesses, risk flags, and keep/reject recommendations.

### 5. Automated Evaluation

CyberHR can support candidate evaluation, culture-fit evaluation, probation review, and performance feedback drafting.

---

## Installation

```bash
mkdir -p .claude/skills
git clone https://github.com/YOUR_USERNAME/cyber-hr-skill .claude/skills/create-cyber-hr
```

Optional dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run:

```text
/create-cyber-hr
```

Provide HR profile information and source materials such as:

- interview transcripts
- recruiter chats
- offer negotiation scripts
- evaluation comments
- SOP / policy docs
- direct narration

Commands:

| Command | Description |
|---------|-------------|
| `/list-hrs` | List all CyberHR skills |
| `/{slug}` | Full CyberHR |
| `/{slug}-memory` | HR memory only |
| `/{slug}-persona` | HR persona only |
| `/{slug}-team` | HR Agent Team mode |
| `/cyber-hr-rollback {slug} {version}` | Rollback |
| `/delete-cyber-hr {slug}` | Delete |

---

## Credits

This project builds on the lineage and inspiration of:

- colleague skill
- ex-partner skill
- yourself skill

Additional thanks to:

- GPT-5.4
- Claude Code
- VSCode
