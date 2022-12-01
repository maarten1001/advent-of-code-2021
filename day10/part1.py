# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

match = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

total = 0
for i, m in enumerate(entries):
    stack = []
    for j, n in enumerate(m):
        if n in match:
            stack.append(match[n])
        elif len(stack) == 0:
            print(f"{m} invalid: closing character {n} on empty stack")
            break
        else:
            closing = stack.pop()
            if n != closing:
                print(f"{m} corrupted: expected {closing}, but found {n} instead")
                total += points[n]
                break
    if len(stack) != 0:
        print(f"{m} incomplete: remaining stack ", end="")
        while len(stack) != 0:
            print(stack.pop(), end="")
        print()

print(total)
