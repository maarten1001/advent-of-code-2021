# get the input numbers
with open("test.txt") as f:
    entries = f.read().splitlines()

cave1 = [[int(i) for i in j] for j in entries]
cave2 = [[0 for i in j] for j in entries]
# cave = []
# for m in range(5):
#     for j, n in enumerate(entries):
#         cave.append([])
#         for k in range(5):
#             for i in n:
#                 x = int(i) + k + m
#                 if x > 9:
#                     cave[-1].append((x % 10) + 1)
#                 else:
#                     cave[-1].append(x)


def print_cave(c, x=None, y=None):
    for i, m in enumerate(c):
        if i % 10 == 0:
            print()
        for j, n in enumerate(m):
            if j % 10 == 0:
                print(" ", end="")
            if i == y and j == x:
                print("\033[96m", end="")
                print('{:>3}'.format(n), end="")
                print("\033[0m", end="")
            elif i < len(c) - 1 and j < len(c[i]) - 1 and n > (c[i+1][j-1] + c[i+1][j] + c[i+1][j+1]):
                print("\033[95m", end="")
                print('{:>3}'.format(n), end="")
                print("\033[0m", end="")
            elif n == 0:
                print('{:>3}'.format('.'), end="")
            else:
                print('{:>3}'.format(n), end="")
        print()
    print()


x = x_start = len(cave1[0]) - 1
y = y_start = len(cave1) - 1

while True:
    # check if we have reached the edge
    if y == len(cave2) and y_start > 0:
        y_start -= 1
        y = y_start
        x = x_start
    if x < 0:
        x_start -= 1
        y = y_start
        x = x_start
    # starting from the bottom right, add the lowest risk path to the end
    if y == len(cave2) - 1:
        if x == len(cave2[0]) - 1:
            cave2[y][x] = cave1[y][x]
        else:
            cave2[y][x] = cave1[y][x] + cave2[y][x + 1]
    elif x == len(cave2[0]) - 1:
        cave2[y][x] = cave1[y][x] + cave2[y + 1][x]
    # we are at the start, print the result
    elif x == 0 and y == 0:
        print_cave(cave2)
        print(min(cave2[y][x + 1], cave2[y + 1][x]))
        break
    else:
        cave2[y][x] = cave1[y][x] + min(cave2[y][x + 1], cave2[y + 1][x])
    print_cave(cave2, x, y)
    y += 1
    x -= 1
    input("Press Enter to continue")
