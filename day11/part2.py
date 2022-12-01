# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

grid = [[int(i) for i in j] for j in entries]
flash = [[False for i in range(10)] for j in range(10)]


def print_grid():
    for i, m in enumerate(grid):
        for j, n in enumerate(m):
            if flash[i][j]:
                print("\033[95m", end="")
                print(0, end="")
                print("\033[0m", end="")
            else:
                if n > 9:
                    print(0, end="")
                else:
                    print(n, end="")
        print()
    print()


print("Before any steps:")
print_grid()

count = 0
for step in range(1, 20001):
    flash = [[False for i in range(10)] for j in range(10)]
    # increase the energy level of each octopus by 1
    for i, m in enumerate(grid):
        for j, n in enumerate(m):
            grid[i][j] += 1

    modified = True
    while modified:
        modified = False
        for i, m in enumerate(grid):
            for j, n in enumerate(m):
                if n > 9 and not flash[i][j]:
                    # flash
                    flash[i][j] = True
                    modified = True
                    count += 1
                    # increase the energy level of all adjacent octopuses
                    for k in range(max(0, i - 1), min(len(grid), i + 2)):
                        for l in range(max(0, j - 1), min(len(m), j + 2)):
                            grid[k][l] += 1

    # set the energy level of octopuses that flashed to 0
    for i, m in enumerate(grid):
        for j, n in enumerate(m):
            if flash[i][j]:
                grid[i][j] = 0

    print(f"After step {step}:")
    print_grid()
    if sum([sum(x) for x in flash]) == 100:
        break
