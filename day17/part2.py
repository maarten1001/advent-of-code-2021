# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

target = entries[0].split(",")
for i, t in enumerate(target):
    target[i] = t[t.find("=") + 1:].split("..")
    for j, s in enumerate(target[i]):
        target[i][j] = int(s)

total = 0
for x in range(1, max(target[0]) + 1):
    for y in range(min(target[1]), abs(min(target[1])) + 1):
        position = [0, 0]
        velocity = [x, y]
        # while we haven't passed the target area
        while position[0] <= max(target[0]) and position[1] >= min(target[1]):
            position[0] += velocity[0]
            position[1] += velocity[1]
            if velocity[0] > 0:
                velocity[0] -= 1
            velocity[1] -= 1
            # we have reached the target area
            if (min(target[0]) <= position[0] <= max(target[0])
                    and (min(target[1]) <= position[1] <= max(target[1]))):
                total += 1
                break

print(total)
