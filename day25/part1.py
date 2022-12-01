# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

floor = [[i for i in j] for j in entries]


def print_floor():
    for i, m in enumerate(floor):
        for j, n in enumerate(m):
            print(n, end="")
        print()
    print()


print("Initial state:")
print_floor()

step = 0
modified = True
while modified:
    step += 1
    modified = False
    move = [[i for i in j] for j in floor]
    # move east
    for y, line in enumerate(floor):
        for x, spot in enumerate(line):
            next_x = (x + 1) % len(line)
            if floor[y][x] == '>' and floor[y][next_x] == '.':
                move[y][next_x] = floor[y][x]
                move[y][x] = '.'
                modified = True
    floor = move
    move = [[i for i in j] for j in floor]
    # move south
    for y, line in enumerate(floor):
        for x, spot in enumerate(line):
            next_y = (y + 1) % len(floor)
            if floor[y][x] == 'v' and floor[next_y][x] == '.':
                move[next_y][x] = floor[y][x]
                move[y][x] = '.'
                modified = True
    floor = move

print(f"After {step} steps:")
print_floor()
