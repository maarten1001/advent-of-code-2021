# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

entries = list(map(int, entries))

total = 0
for x in range(len(entries) - 1):
    if entries[x] < entries[x + 1]:
        total = total + 1

print(total)
