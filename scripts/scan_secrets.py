"""Git hygiene and secret scanning script."""

import os
import re

patterns = [
    re.compile(r'(?i)api[_-]?key\s*[:=]\s*["\'][A-Za-z0-9_\-]{16,}["\']'),
    re.compile(r'(?i)secret[_-]?key\s*[:=]\s*["\'][A-Za-z0-9_\-]{16,}["\']'),
    re.compile(r'(?i)password\s*[:=]\s*["\'][^\s"\']{8,}["\']'),
    re.compile(r'(?i)bearer\s+[A-Za-z0-9_\-\.]{20,}'),
]

found = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'node_modules']
    for f in files:
        if f.endswith(('.py', '.R', '.yaml', '.yml', '.csv', '.json', '.md', '.qmd', '.toml', '.txt')):
            p = os.path.join(root, f)
            try:
                content = open(p, 'r', encoding='utf-8', errors='ignore').read()
                for pat in patterns:
                    matches = pat.findall(content)
                    if matches:
                        found.append((p, matches))
            except Exception:
                pass

print(f"Secret Scanner Completed. Total Potential Secrets Found: {len(found)}")
for path, match_list in found:
    print(f"  [ALERT] {path}: {match_list}")
