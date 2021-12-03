# get the input numbers
f = open("test.txt")
entries = f.read().splitlines()
f.close()

length = len(entries)
print(length)
total = [0 for e in entries[0]]
gamma = ""
epsilon = list()

for i in range(length):
    total = [x + y for x, y in zip(total, list(map(int, entries[i])))]
print(total)

for t in total:
    if t > length / 2:
        gamma = gamma + "1"
    else:
        gamma = gamma + "0"
print(gamma)
print(int(gamma,2))
