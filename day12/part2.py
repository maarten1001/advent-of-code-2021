# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

entries = [e.split("-") for e in entries]

caves = {}
for i, j in entries:
    # add the connections in both directions
    if i in caves:
        caves[i].add(j)
    else:
        caves[i] = {j}
    if j in caves:
        caves[j].add(i)
    else:
        caves[j] = {i}


def find_paths(cave, path, twice):
    total = 0
    path.append(cave)
    if cave == 'end':
        print(path)
        return 1
    for x in caves[cave]:
        if x != 'start':
            if x.isupper() or x not in path:
                total += find_paths(x, path.copy(), twice)
            # visit a single small cave twice
            elif x.islower() and twice is False and path.count(x) == 1:
                total += find_paths(x, path.copy(), True)
    return total


print(find_paths("start", [], False))
