import re

# get the input numbers
with open("test.txt") as f:
    entries = f.read().splitlines()

# Like day 6: we don't need to track each individual letter, just the count!
# Create a dictionary of pairs to track and count:
# NNCB
# NN
#  NC
#   CB
template = entries[0]
current = {}
for i in range(0, len(template) - 1):
    pair = template[i:i + 2]
    if pair in current:
        current[pair] += 1
    else:
        current[pair] = 1

print(current)

rules = [re.split(' -> ', e) for e in entries[2:]]

for step in range(1, 3):
    new = current.copy()
    for find, element in rules:
        if find in current:
            # update the dictionary
            print(f"{find} -> ", end="")
            replace = find[0] + element
            print(replace, end=" + ")
            if replace in new:
                new[replace] += new[find]
            else:
                new[replace] = new[find]
            replace = element + find[1]
            print(replace)
            if replace in new:
                new[replace] += new[find]
            else:
                new[replace] = new[find]
            new[find] = 0
    current = new
    print(f"After step {step}: {current}")
