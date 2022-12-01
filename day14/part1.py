import re

# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

current = list(entries[0])
rules = [re.split(' -> ', e) for e in entries[2:]]
print(f"Template: {''.join(current)}")

for step in range(1, 11):
    new = current.copy()
    for i in range(len(current) - 1, 0, -1):
        for find, element in rules:
            if current[i - 1:i + 1] == list(find):
                new.insert(i, element)
    current = new
    print(f"After step {step}: {''.join(current)}")
    print(len(current))

print()
count = [current.count(c) for c in set(current)]
print(max(count) - min(count))
