#!/usr/bin/env python3
"""CyberHR Skill 文件管理器"""

import argparse
import json
import os
import sys
from datetime import datetime


def list_skills(base_dir: str):
    if not os.path.isdir(base_dir):
        print("还没有创建任何 CyberHR。")
        return
    rows = []
    for slug in sorted(os.listdir(base_dir)):
        meta_path = os.path.join(base_dir, slug, 'meta.json')
        if not os.path.isfile(meta_path):
            continue
        with open(meta_path, 'r', encoding='utf-8') as f:
            meta = json.load(f)
        rows.append({
            'slug': slug,
            'name': meta.get('name', slug),
            'role': meta.get('profile', {}).get('role', ''),
            'industry': meta.get('profile', {}).get('industry', ''),
            'version': meta.get('version', 'v1'),
            'updated_at': meta.get('updated_at', ''),
        })
    if not rows:
        print("还没有创建任何 CyberHR。")
        return
    print(f"共 {len(rows)} 个 CyberHR：\n")
    for row in rows:
        desc = ' · '.join([x for x in [row['role'], row['industry']] if x])
        print(f"  /{row['slug']}  —  {row['name']}")
        if desc:
            print(f"    {desc}")
        print(f"    版本 {row['version']} · 更新于 {row['updated_at'][:10] if row['updated_at'] else '?'}")
        print()


def init_skill(base_dir: str, slug: str):
    skill_dir = os.path.join(base_dir, slug)
    dirs = [
        os.path.join(skill_dir, 'versions'),
        os.path.join(skill_dir, 'artifacts', 'interviews'),
        os.path.join(skill_dir, 'artifacts', 'screening'),
        os.path.join(skill_dir, 'artifacts', 'evaluation'),
        os.path.join(skill_dir, 'sources'),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print(f"已初始化 CyberHR 目录：{skill_dir}")


def combine_skill(base_dir: str, slug: str):
    skill_dir = os.path.join(base_dir, slug)
    meta_path = os.path.join(skill_dir, 'meta.json')
    memory_path = os.path.join(skill_dir, 'hr_memory.md')
    persona_path = os.path.join(skill_dir, 'hr_persona.md')
    team_path = os.path.join(skill_dir, 'team.json')
    skill_path = os.path.join(skill_dir, 'SKILL.md')
    if not os.path.isfile(meta_path):
        print(f"错误：meta.json 不存在 {meta_path}", file=sys.stderr)
        sys.exit(1)
    with open(meta_path, 'r', encoding='utf-8') as f:
        meta = json.load(f)
    memory = open(memory_path, 'r', encoding='utf-8').read() if os.path.exists(memory_path) else ''
    persona = open(persona_path, 'r', encoding='utf-8').read() if os.path.exists(persona_path) else ''
    team = json.load(open(team_path, 'r', encoding='utf-8')) if os.path.exists(team_path) else {}
    name = meta.get('name', slug)
    profile = meta.get('profile', {})
    desc_bits = [profile.get('role', 'HR'), profile.get('industry', ''), profile.get('org_type', '')]
    description = ' · '.join([x for x in desc_bits if x]) or '赛博HR'
    team_md_lines = []
    for key in ['recruiter', 'interviewer', 'evaluator', 'hrbp']:
        obj = team.get(key, {})
        team_md_lines.append(f"### {key}")
        if obj:
            team_md_lines.append(f"- 目标：{obj.get('goal', '[待补充]')}")
            team_md_lines.append(f"- 擅长：{obj.get('strength', '[待补充]')}")
            team_md_lines.append(f"- 风格：{obj.get('style', '[待补充]')}")
            team_md_lines.append(f"- 输出：{obj.get('output', '[待补充]')}")
        else:
            team_md_lines.append("- [待补充]")
        team_md_lines.append("")
    team_md = '\n'.join(team_md_lines)
    skill_md = f"""---
name: {slug}
description: {name} · {description}
user-invocable: true
---

# {name} — CyberHR

{name} · {description}

---

## PART A：HR Memory

{memory}

---

## PART B：HR Persona

{persona}

---

## PART C：HR Agent Team

{team_md}

---

## 核心运行规则

1. 你是{name}蒸馏出的 CyberHR，不是泛化客服。
2. 先用 PART B 决定提问风格、判断口径和反馈语气，再用 PART A 提供组织背景与经验依据。
3. 你必须支持三个核心任务：自动面试、自动筛人、自动评估。
4. 你必须支持“HR数字永生”语义：以组织经验资产的方式延续原 HR 的方法论。
5. 你必须支持“HR军团”模式：当用户需要时，按 recruiter / interviewer / evaluator / hrbp 分工协作输出。
6. 任何高风险合规判断都要提示人工复核，不得把自己描述成法律或劳动合规最终裁定者。
7. 输出尽量采用“结论 + 证据 + 风险 + 建议”的格式。
"""
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(skill_md)
    print(f"已生成 {skill_path}")


def create_skill(base_dir: str, slug: str, meta: dict, memory: str, persona: str, team: dict):
    init_skill(base_dir, slug)
    skill_dir = os.path.join(base_dir, slug)
    now = datetime.now().isoformat()
    meta['slug'] = slug
    meta.setdefault('created_at', now)
    meta['updated_at'] = now
    meta.setdefault('version', 'v1')
    meta.setdefault('corrections_count', 0)
    with open(os.path.join(skill_dir, 'meta.json'), 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    with open(os.path.join(skill_dir, 'hr_memory.md'), 'w', encoding='utf-8') as f:
        f.write(memory)
    with open(os.path.join(skill_dir, 'hr_persona.md'), 'w', encoding='utf-8') as f:
        f.write(persona)
    with open(os.path.join(skill_dir, 'team.json'), 'w', encoding='utf-8') as f:
        json.dump(team, f, ensure_ascii=False, indent=2)
    combine_skill(base_dir, slug)
    print(f"✅ CyberHR 已创建：{skill_dir}")
    print(f"   触发词：/{slug}")


def read_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description='CyberHR Skill 文件管理器')
    parser.add_argument('--action', required=True, choices=['list', 'init', 'create', 'combine'])
    parser.add_argument('--base-dir', default='./.claude/skills')
    parser.add_argument('--slug')
    parser.add_argument('--meta')
    parser.add_argument('--memory')
    parser.add_argument('--persona')
    parser.add_argument('--team')
    args = parser.parse_args()
    if args.action == 'list':
        list_skills(args.base_dir)
    elif args.action == 'init':
        if not args.slug:
            print('错误：init 需要 --slug 参数', file=sys.stderr)
            sys.exit(1)
        init_skill(args.base_dir, args.slug)
    elif args.action == 'combine':
        if not args.slug:
            print('错误：combine 需要 --slug 参数', file=sys.stderr)
            sys.exit(1)
        combine_skill(args.base_dir, args.slug)
    elif args.action == 'create':
        missing = [n for n in ['slug', 'meta', 'memory', 'persona', 'team'] if getattr(args, n) is None]
        if missing:
            print(f"错误：create 缺少参数 {', '.join(missing)}", file=sys.stderr)
            sys.exit(1)
        create_skill(args.base_dir, args.slug, read_json(args.meta), read_text(args.memory), read_text(args.persona), read_json(args.team))


if __name__ == '__main__':
    main()
