#!/usr/bin/env python3
"""QQ 聊天记录解析器（CyberHR 版）"""

import argparse, os, re, sys
from pathlib import Path


def parse_qq_txt(file_path, target_name):
    messages, current = [], None
    pattern = re.compile(r'^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(.+?)(?:\((\d+)\))?\s*$')
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.rstrip('\n')
            m = pattern.match(line)
            if m:
                if current:
                    messages.append(current)
                ts, sender, _ = m.groups()
                current = {'timestamp': ts, 'sender': sender.strip(), 'content': ''}
            elif current and line.strip() and not line.startswith('==='):
                current['content'] += ('\n' if current['content'] else '') + line
    if current:
        messages.append(current)
    target_msgs = [m for m in messages if target_name in m.get('sender', '')]
    text = ' '.join([m.get('content', '') for m in target_msgs])
    return {'total_messages': len(messages), 'target_messages': len(target_msgs), 'question_count': text.count('?') + text.count('？'), 'sample_messages': [m.get('content', '') for m in target_msgs[:50] if m.get('content')]}


def parse_qq_mht(file_path, target_name):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    clean = re.sub(r'<[^>]+>', '\n', content)
    clean = re.sub(r'\n{3,}', '\n\n', clean)
    return {'total_messages': 0, 'target_messages': 0, 'question_count': clean.count('?') + clean.count('？'), 'sample_messages': clean.splitlines()[:80]}


def main():
    parser = argparse.ArgumentParser(description='QQ 聊天记录解析器（CyberHR 版）')
    parser.add_argument('--file', required=True)
    parser.add_argument('--target', required=True, help='目标HR的名字/昵称')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if not os.path.exists(args.file):
        print(f'错误：文件不存在 {args.file}', file=sys.stderr)
        sys.exit(1)
    result = parse_qq_mht(args.file, args.target) if Path(args.file).suffix.lower() in {'.mht', '.mhtml'} else parse_qq_txt(args.file, args.target)
    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(f'# QQ沟通分析（CyberHR）— {args.target}\n\n')
        f.write(f'总消息数：{result.get("total_messages", 0)}\n目标消息数：{result.get("target_messages", 0)}\n问题句数量：{result.get("question_count", 0)}\n\n')
        f.write('## 样本\n')
        for i, msg in enumerate(result.get('sample_messages', []), 1):
            f.write(f'{i}. {msg}\n')
    print(f'分析完成，结果已写入 {args.output}')


if __name__ == '__main__':
    main()
