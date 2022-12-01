# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

target = entries[0].split(",")
for i, t in enumerate(target):
    target[i] = t[t.find("=") + 1:].split("..")
    for j, s in enumerate(target[i]):
        target[i][j] = int(s)

style_height = 0
style_velocity = [0, 0]
for x in range(max(target[0])):
    for y in range(abs(min(target[1]))):
        position = [0, 0]
        velocity = [x, y]
        max_height = 0
        # while we haven't passed the target area
        while position[0] <= max(target[0]) and position[1] >= max(target[1]):
            position[0] += velocity[0]
            position[1] += velocity[1]
            if velocity[0] > 0:
                velocity[0] -= 1
            velocity[1] -= 1
            max_height = max(max_height, position[1])
            # we have reached the target area
            if (min(target[0]) <= position[0] <= max(target[0])
                    and (min(target[1]) <= position[1] <= max(target[1]))):
                if max_height > style_height:
                    style_height = max_height
                    style_velocity = [x, y]
                break

print(style_velocity)
print(style_height)
