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
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

totals = []
for i, m in enumerate(entries):
    stack = []
    for j, n in enumerate(m):
        if n in match:
            stack.append(match[n])
        elif len(stack) == 0:
            print(f"{m} invalid: found closing character {n} but the stack is empty")
            break
        elif n != stack.pop():
            # discard corrupted line
            stack = []
            break
    if len(stack) != 0:
        total = 0
        print(f"{m} incomplete: remaining stack ", end="")
        while len(stack) != 0:
            closing = stack.pop()
            total = total * 5 + points[closing]
            print(closing, end="")
        print()
        totals.append(total)

totals.sort()
middle = (len(totals)) / 2
print(totals[int(middle)])
