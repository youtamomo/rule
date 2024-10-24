import requests

urls = [
    "https://github.com/AdguardTeam/FiltersRegistry/raw/refs/heads/master/filters/filter_15_DnsFilter/filter.txt",
    "https://big.oisd.nl"
]

unique_lines = set()

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        unique_lines.update(
            line.strip() for line in response.text.splitlines() if not line.startswith('!')
        )
    except requests.RequestException as e:
        print(f"Download failed for {url}: {e}")

temp_filename = "temp_filters.txt"
with open(temp_filename, 'w', encoding='utf-8') as f:
    for line in sorted(unique_lines):
        f.write(line + '\n')

print(f"Temporary file {temp_filename} created with {len(unique_lines)} lines.")