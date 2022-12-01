# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

cave = [[int(i) for i in j] for j in entries]


def print_cave():
    for i, m in enumerate(cave):
        for j, n in enumerate(m):
            print(n, end="")
        print()
    print()


x = x_start = len(cave[0]) - 1
y = y_start = len(cave) - 1

for i in range(110000):
    # check if we have reached the edge
    if y == len(cave) and y_start > 0:
        y_start -= 1
        y = y_start
        x = x_start
    if x < 0:
        x_start -= 1
        y = y_start
        x = x_start
    # starting from the bottom right, add the lowest risk path to the end
    if y == len(cave) - 1:
        if x != len(cave[0]) - 1:
            cave[y][x] += cave[y][x + 1]
    elif x == len(cave[0]) - 1:
        cave[y][x] += cave[y + 1][x]
    # we are at the start, print the result
    elif x == 0 and y == 0:
        print(min(cave[y][x + 1], cave[y + 1][x]))
        break
    else:
        cave[y][x] += min(cave[y][x + 1], cave[y + 1][x])
    y += 1
    x -= 1
