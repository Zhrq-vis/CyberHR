#!/usr/bin/env python3
"""社交/文档目录扫描器（CyberHR 版）"""

import argparse, os, sys
from pathlib import Path


def scan_directory(dir_path):
    files = {'images': [], 'texts': [], 'other': []}
    image_exts = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}
    text_exts = {'.txt', '.md', '.json', '.csv', '.pdf'}
    for root, _, filenames in os.walk(dir_path):
        for fname in filenames:
            path = os.path.join(root, fname)
            ext = Path(fname).suffix.lower()
            if ext in image_exts:
                files['images'].append(path)
            elif ext in text_exts:
                files['texts'].append(path)
            else:
                files['other'].append(path)
    return files


def main():
    parser = argparse.ArgumentParser(description='社交/文档目录扫描器（CyberHR 版）')
    parser.add_argument('--dir', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if not os.path.isdir(args.dir):
        print(f'错误：目录不存在 {args.dir}', file=sys.stderr)
        sys.exit(1)
    files = scan_directory(args.dir)
    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('# CyberHR 材料扫描结果\n\n')
        f.write(f'扫描目录：{args.dir}\n\n')
        for kind in ['images', 'texts', 'other']:
            f.write(f'## {kind}\n')
            for item in sorted(files[kind]):
                f.write(f'- {item}\n')
            f.write('\n')
    print(f'扫描完成，结果已写入 {args.output}')


if __name__ == '__main__':
    main()
