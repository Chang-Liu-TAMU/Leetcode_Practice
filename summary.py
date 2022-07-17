from pathlib import Path
from collections import defaultdict
p = Path()
prefixes = ["dp", "linked-list", "tree"]
s = defaultdict(int)
for i in p.iterdir():
    for j in prefixes:
        if i.name.startswith(j):
            s[j] += 1
            break
s["total"] = sum(s.values())
print(s)