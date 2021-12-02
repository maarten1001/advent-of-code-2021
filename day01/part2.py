# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

entries = list(map(int, entries))

total = 0
for x in range(len(entries) - 3):
    # Due to the overlap in the sliding window we could have used entries[x] < entries[x + 3]
    if entries[x] + entries[x + 1] + entries[x + 2] < entries[x + 1] + entries[x + 2] + entries[x + 3]:
        total = total + 1

print(total)
