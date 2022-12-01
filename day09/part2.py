# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

count = [[0 if int(i) == 9 else 1 for i in j] for j in entries]
entries = [[int(i) for i in j] for j in entries]

modified = True
while modified:
    modified = False
    # model the flow of smoke
    for i, m in enumerate(entries):
        for j, n in enumerate(m):
            if count[i][j] > 0:
                if i > 0 and entries[i - 1][j] <= n:
                    count[i - 1][j] += count[i][j]
                    count[i][j] = 0
                    modified = True
                # < instead of <= to prevent flipping between equal heights
                elif i < len(entries) - 1 and entries[i + 1][j] < n:
                    count[i + 1][j] += count[i][j]
                    count[i][j] = 0
                    modified = True
                elif j > 0 and entries[i][j - 1] <= n:
                    count[i][j - 1] += count[i][j]
                    count[i][j] = 0
                    modified = True
                elif j < len(m) - 1 and entries[i][j + 1] < n:
                    count[i][j + 1] += count[i][j]
                    count[i][j] = 0
                    modified = True

largest = []
for i, m in enumerate(count):
    for j, n in enumerate(m):
        if n > 0:
            largest.append(n)
largest.sort(reverse=True)
print(largest[0] * largest[1] * largest[2])
