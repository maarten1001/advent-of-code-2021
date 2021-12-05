# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

entries2 = entries.copy()
oxygen = ''
co2 = ''

for bit in range(len(entries[0])):
    total = [0, 0]
    for e in entries:
        total[int(e[bit])] += 1
    for e in entries.copy():
        if (total[1] >= total[0] and e[bit] == '0') or (total[1] < total[0] and e[bit] == '1'):
            entries.remove(e)
    if len(entries) == 1:
        oxygen = entries[0]
        break

for bit in range(len(entries2[0])):
    total = [0, 0]
    for e in entries2:
        total[int(e[bit])] += 1
    for e in entries2.copy():
        if (total[1] < total[0] and e[bit] == '0') or (total[1] >= total[0] and e[bit] == '1'):
            entries2.remove(e)
    if len(entries2) == 1:
        co2 = entries2[0]
        break

print("oxygen = " + oxygen)
print("co2    = " + co2)
print(int(oxygen, 2) * int(co2, 2))