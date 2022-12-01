# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

entries = [[int(i) for i in j] for j in entries]
for e in entries:
    print(e)

total = 0
for i, m in enumerate(entries):
    for j, n in enumerate(m):
        if i > 0 and entries[i - 1][j] <= n:
            continue
        if i < len(entries) - 1 and entries[i + 1][j] <= n:
            continue
        if j > 0 and entries[i][j - 1] <= n:
            continue
        if j < len(m) - 1 and entries[i][j + 1] <= n:
            continue
        total += 1 + n

print(total)
