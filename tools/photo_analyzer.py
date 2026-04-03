#!/usr/bin/env python3
"""照片/截图时间线分析器（CyberHR 版）"""

import argparse, os, sys
from pathlib import Path
try:
    from PIL import Image
    from PIL.ExifTags import TAGS
    HAS_PIL = True
except Exception:
    HAS_PIL = False


def get_exif_data(path):
    if not HAS_PIL:
        return {'file': os.path.basename(path), 'note': 'Pillow 未安装'}
    try:
        img = Image.open(path)
        exif_raw = img.getexif()
        data = {'file': os.path.basename(path), 'path': path}
        for tag_id, value in exif_raw.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag in {'DateTimeOriginal', 'DateTime'}:
                data['date_taken'] = str(value)
        return data
    except Exception as e:
        return {'file': os.path.basename(path), 'error': str(e)}


def main():
    parser = argparse.ArgumentParser(description='照片/截图时间线分析器（CyberHR 版）')
    parser.add_argument('--dir', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if not os.path.isdir(args.dir):
        print(f'错误：目录不存在 {args.dir}', file=sys.stderr)
        sys.exit(1)
    image_exts = {'.jpg', '.jpeg', '.png', '.heic', '.heif', '.webp'}
    rows = []
    for root, _, files in os.walk(args.dir):
        for fname in sorted(files):
            if Path(fname).suffix.lower() in image_exts:
                rows.append(get_exif_data(os.path.join(root, fname)))
    rows.sort(key=lambda x: x.get('date_taken', '9999'))
    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('# CyberHR 图片/截图时间线\n\n')
        f.write(f'扫描目录：{args.dir}\n总文件数：{len(rows)}\n\n')
        for row in rows:
            f.write(f"- {row.get('date_taken', '[无时间]')} — {row.get('file')}\n")
    print(f'分析完成，结果已写入 {args.output}')


if __name__ == '__main__':
    main()
