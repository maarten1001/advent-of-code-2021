# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

total = 0
for i, k in enumerate(entries):
    entries[i] = entries[i].split(" | ")
    for j, v in enumerate(entries[i][1].split()):
        if len(v) in (2, 4, 3, 7):
            total += 1
print(total)
