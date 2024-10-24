import requests
import subprocess
import os

# 要下载的文件链接
urls = [
    "https://github.com/AdguardTeam/FiltersRegistry/raw/refs/heads/master/filters/filter_15_DnsFilter/filter.txt",
    "https://big.oisd.nl"
]

# 下载并去重处理
unique_lines = set()
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        # 直接处理文本
        unique_lines.update(line.strip() for line in response.text.splitlines() if not line.startswith('!'))
    except requests.RequestException as e:
        print(f"下载失败 {url}: {e}")

# 将去重后的内容写入临时文件
temp_filename = "temp_filters.txt"
with open(temp_filename, 'w', encoding='utf-8') as f:
    for line in sorted(unique_lines):
        f.write(line + '\n')

print(f"临时文件 {temp_filename} 已生成，包含 {len(unique_lines)} 行内容。")
