#!/usr/bin/env python3
"""
Tải toàn bộ ảnh (https://images.pexels.com/...) của dự án về thư mục images/
và sửa lại đường dẫn trong các file .html / .css thành đường dẫn tương đối.

Cách dùng (cần Internet MỘT LẦN, sau đó web chạy offline):
    1. Đặt file này ở thư mục gốc dự án (cùng chỗ với index.html)
    2. Chạy:  python tai-anh-ve-may.py      (hoặc: python3 tai-anh-ve-may.py)
Chạy lại nhiều lần vẫn an toàn: ảnh đã tải sẽ được bỏ qua.
"""
import os, re, sys, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(ROOT, 'images')
URL_RE = re.compile(r'https://images\.pexels\.com/photos/(\d+)/pexels-photo-\d+\.(jpe?g|png|webp)\?[^\s"\'()<>]*')


def source_files():
    for base, _dirs, files in os.walk(ROOT):
        if os.path.abspath(base).startswith(IMG_DIR):
            continue
        for f in files:
            if f.lower().endswith(('.html', '.css')):
                yield os.path.join(base, f)


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def fetch(url):
    last = None
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except Exception as e:          # thử lại tối đa 3 lần
            last = e
            time.sleep(1.5)
    raise last


def main():
    os.makedirs(IMG_DIR, exist_ok=True)

    # 1) Gom các ảnh duy nhất (mỗi ảnh lấy khổ rộng nhất đang được dùng)
    photos = {}
    for path in source_files():
        for m in URL_RE.finditer(read(path)):
            w = re.search(r'w=(\d+)', m.group(0))
            w = int(w.group(1)) if w else 940
            pid, ext = m.group(1), m.group(2).lower()
            old = photos.get(pid)
            if not old or w > old[1]:
                photos[pid] = (ext, w)
    print(f'Tìm thấy {len(photos)} ảnh cần tải.')

    # 2) Tải về images/
    ok, fail = set(), []
    for pid, (ext, w) in sorted(photos.items()):
        dest = os.path.join(IMG_DIR, f'pexels-{pid}.{ext}')
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            ok.add(pid); continue
        url = f'https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.{ext}?auto=compress&cs=tinysrgb&w={w}'
        try:
            data = fetch(url)
            with open(dest, 'wb') as fh:
                fh.write(data)
            ok.add(pid); print('  đã tải', os.path.basename(dest))
        except Exception as e:
            fail.append(pid); print('  LỖI', pid, '-', e)

    # 3) Sửa đường dẫn trong html/css (chỉ với ảnh đã tải thành công)
    changed = 0
    for path in source_files():
        s = read(path)
        def rep(m):
            pid, ext = m.group(1), m.group(2).lower()
            if pid not in ok:
                return m.group(0)
            local = os.path.join(IMG_DIR, f'pexels-{pid}.{ext}')
            return os.path.relpath(local, os.path.dirname(path)).replace(os.sep, '/')
        s2 = URL_RE.sub(rep, s)
        if s2 != s:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(s2)
            changed += 1
    print(f'Xong: {len(ok)} ảnh trong images/, đã sửa đường dẫn ở {changed} file.')
    if fail:
        print('Chưa tải được (vẫn dùng link online):', ', '.join(fail), '- chạy lại script khi có mạng.')
        sys.exit(1)


if __name__ == '__main__':
    main()
