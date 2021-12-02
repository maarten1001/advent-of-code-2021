# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

hor = 0
depth = 0
aim = 0

for x in entries:
    y = x.split()
    if y[0] == 'forward':
        hor = hor + int(y[1])
        depth = depth + (aim * int(y[1]))
    if y[0] == 'down':
        aim = aim + int(y[1])
    if y[0] == 'up':
        aim = aim - int(y[1])

print(hor)
print(depth)
print(hor * depth)
