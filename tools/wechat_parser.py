#!/usr/bin/env python3
"""微信聊天记录解析器（CyberHR 版）"""

import argparse, json, os, re, sys
from pathlib import Path


def detect_format(file_path: str) -> str:
    ext = Path(file_path).suffix.lower()
    if ext == '.json':
        return 'liuhen'
    if ext in {'.txt', '.csv', '.html', '.htm'}:
        return 'wechatmsg_txt'
    return 'plaintext'


def analyze_messages(messages, target_name):
    target_msgs = [m for m in messages if target_name in m.get('sender', '')]
    text = ' '.join([m.get('content', '') for m in target_msgs])
    return {
        'target_name': target_name,
        'total_messages': len(messages),
        'target_messages': len(target_msgs),
        'analysis': {
            'avg_message_length': round(sum(len(m.get('content', '')) for m in target_msgs) / len(target_msgs), 1) if target_msgs else 0,
            'question_density': text.count('?') + text.count('？'),
            'keyword_hits': {
                '为什么': text.count('为什么'),
                '具体': text.count('具体'),
                '举例': text.count('举例'),
                '风险': text.count('风险'),
                '匹配': text.count('匹配')
            }
        },
        'sample_messages': [m.get('content', '') for m in target_msgs[:50] if m.get('content')]
    }


def parse_wechatmsg_txt(file_path, target_name):
    messages, current = [], None
    pattern = re.compile(r'^(\d{4}[-/]\d{2}[-/]\d{2}.*?)([^:：]+)$')
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.rstrip('\n')
            m = pattern.match(line)
            if m:
                if current:
                    messages.append(current)
                ts, sender = m.groups()
                current = {'timestamp': ts, 'sender': sender.strip(), 'content': ''}
            elif current and line.strip():
                current['content'] += ('\n' if current['content'] else '') + line
    if current:
        messages.append(current)
    return analyze_messages(messages, target_name)


def parse_liuhen_json(file_path, target_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    msg_list = data if isinstance(data, list) else data.get('messages', data.get('data', []))
    messages = [{'timestamp': m.get('time', m.get('timestamp', '')), 'sender': m.get('sender', m.get('nickname', m.get('from', ''))), 'content': m.get('content', m.get('message', m.get('text', '')))} for m in msg_list]
    return analyze_messages(messages, target_name)


def parse_plaintext(file_path, target_name):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return {'target_name': target_name, 'total_messages': 0, 'target_messages': 0, 'analysis': {'note': '纯文本模式'}, 'sample_messages': content.splitlines()[:50]}


def main():
    parser = argparse.ArgumentParser(description='微信聊天记录解析器（CyberHR 版）')
    parser.add_argument('--file', required=True)
    parser.add_argument('--target', required=True, help='目标HR的名字/昵称')
    parser.add_argument('--output', required=True)
    parser.add_argument('--format', default='auto')
    args = parser.parse_args()
    if not os.path.exists(args.file):
        print(f'错误：文件不存在 {args.file}', file=sys.stderr)
        sys.exit(1)
    fmt = detect_format(args.file) if args.format == 'auto' else args.format
    func = {'wechatmsg_txt': parse_wechatmsg_txt, 'liuhen': parse_liuhen_json, 'plaintext': parse_plaintext}.get(fmt, parse_plaintext)
    result = func(args.file, args.target)
    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(f'# 微信沟通分析（CyberHR）— {args.target}\n\n')
        f.write(f'来源文件：{args.file}\n检测格式：{fmt}\n总消息数：{result.get("total_messages", 0)}\n目标消息数：{result.get("target_messages", 0)}\n\n')
        f.write('## 风格线索\n')
        for k, v in result.get('analysis', {}).items():
            f.write(f'- {k}: {v}\n')
        f.write('\n## 样本\n')
        for i, msg in enumerate(result.get('sample_messages', []), 1):
            f.write(f'{i}. {msg}\n')
    print(f'分析完成，结果已写入 {args.output}')


if __name__ == '__main__':
    main()
