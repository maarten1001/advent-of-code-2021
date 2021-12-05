# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

numbers = entries[0].split(",")
entries = entries[2:]

boards = []
new = []
for i in entries:
    if i == '':
        boards.append(new)
        new = []
    else:
        new.append([{'value': j, 'marked': False} for j in i.split()])
boards.append(new)


def print_board(n):
    for i in boards[n]:
        for j in i:
            if j["marked"]:
                print("\033[95m", end="")
                print('{:>2}'.format(j["value"]), end=" ")
                print("\033[0m", end="")
            else:
                print('{:>2}'.format(j["value"]), end=" ")
        print()


def is_bingo():
    for b in range(len(boards)):
        # check the rows
        for i in range(5):
            bingo = True
            for j in range(5):
                if not boards[b][i][j]["marked"]:
                    bingo = False
                    break
            if bingo:
                return b
        # check the columns
        for i in range(5):
            bingo = True
            for j in range(5):
                if not boards[b][j][i]["marked"]:
                    bingo = False
                    break
            if bingo:
                return b
    return -1


for n in numbers:
    for b in boards:
        for i in b:
            for j in i:
                if j["value"] == n:
                    j["marked"] = True
    result = is_bingo()
    if result > -1:
        print_board(result)
        total = 0
        for i in boards[result]:
            for j in i:
                if not j["marked"]:
                    total += int(j["value"])
        print()
        print(total)
        print(n)
        print(total * int(n))
        break
