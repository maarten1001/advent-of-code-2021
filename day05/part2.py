import re

# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

# process the list into a list of numbers per vent: x1, y1, x2, y2
vents = [re.split(',| -> ', e) for e in entries]
for i in range(len(vents)):
    vents[i] = [int(x) for x in vents[i]]

# find the maximum values to determine floor size
maximum = 0
for i in vents:
    for j in i:
        if j > maximum:
            maximum = j
maximum += 1

floor = [[0 for i in range(maximum)] for j in range(maximum)]


def print_floor():
    for i in floor:
        for j in i:
            if j == 0:
                print(".", end=" ")
            else:
                print(j, end=" ")
        print()


# vent format: x1, y1, x2, y2
for v in vents:
    x1, y1, x2, y2 = v
    if x1 == x2:
        dy = int((y2 - y1) / abs(y2 - y1))
        floor[y1][x1] += 1
        while y1 != y2:
            y1 += dy
            floor[y1][x1] += 1
    elif y1 == y2:
        dx = int((x2 - x1) / abs(x2 - x1))
        floor[y1][x1] += 1
        while x1 != x2:
            x1 += dx
            floor[y1][x1] += 1
    else:
        dx = int((x2 - x1) / abs(x2 - x1))
        dy = int((y2 - y1) / abs(y2 - y1))
        floor[y1][x1] += 1
        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            floor[y1][x1] += 1

total = 0
for i in floor:
    for j in i:
        if j >= 2:
            total += 1
print()
print(total)
