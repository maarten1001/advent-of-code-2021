# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

dots = []
folds = []
for i, line in enumerate(entries):
    if line[:4] == "fold":
        fold = line[11:].split("=")
        fold[1] = int(fold[1])
        folds.append(fold)
    elif line != '':
        dots.append([int(x) for x in line.split(",")])

# find the maximum values to determine paper size
maximum = max([max(x) for x in dots])
paper = [[False for i in range(maximum + 1)] for j in range(maximum + 1)]


def print_paper():
    for p in paper:
        for pp in p:
            if pp:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


for x, y in dots:
    paper[y][x] = True

for axis, line in folds:
    if axis == 'x':
        for y in range(len(paper)):
            for x in range(1, len(paper[y]) - line):
                paper[y][line - x] = paper[y][line - x] or paper[y][line + x]
            paper[y] = paper[y][:line]
    if axis == 'y':
        for i in range(1, len(paper) - line):
            paper[line - i] = [x or y for x, y in zip(paper[line - i], paper[line + i])]
        paper = paper[:line]
    break

print(sum([sum(x) for x in paper]))
