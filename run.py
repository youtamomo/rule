import requests
import tempfile

urls = [
    "https://github.com/AdguardTeam/FiltersRegistry/raw/refs/heads/master/filters/filter_15_DnsFilter/filter.txt",
    "https://big.oisd.nl"
]

unique_lines = set()
for url in urls:
    try:
        response = requests.get(url, timeout=10)  # 设置请求超时
        response.raise_for_status()
        unique_lines.update(line.strip() for line in response.text.splitlines() if not line.startswith('!'))
    except requests.RequestException as e:
        print(f"下载失败 {url}: {e}")

# 使用 tempfile 创建临时文件
with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as f:
    for line in sorted(unique_lines):
        f.write(line + '\n')
    temp_filename = f.name

print(f"临时文件 {temp_filename} 已生成，包含 {len(unique_lines)} 行内容。")