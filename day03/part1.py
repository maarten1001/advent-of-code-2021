# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

length = len(entries)
total = [0 for e in entries[0]]
gamma = ""
epsilon = ""

for i in range(length):
    entry = [int(z) for z in entries[i]]
    total = [x + y for x, y in zip(total, entry)]

for t in total:
    if t > length / 2:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
print("gamma   = " + gamma)
print("epsilon = " + epsilon)
print(int(gamma, 2) * int(epsilon, 2))
