# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

algorithm = [1 if i == '#' else 0 for i in entries[0]]
image = [[1 if i == '#' else 0 for i in j] for j in entries[2:]]


def print_image():
    for i, m in enumerate(image):
        for j, n in enumerate(m):
            if n == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def expand_image():
    # Expand the image size by 3 pixels on each side
    pixel = image[0][0]
    for i in image:
        i.insert(0, pixel)
        i.insert(0, pixel)
        i.insert(0, pixel)
        i.extend((pixel, pixel, pixel))
    line = [pixel for x in range(len(image[0]))]
    for i in range(3):
        image.insert(0, line.copy())
        image.append(line.copy())


def enhance_image():
    enhanced = [[i for i in j] for j in image]
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            if i == 0 or i == len(image) - 1 or j == 0 or j == len(image) - 1:
                # due to the infinite image size, "edge" pixels can be determined by a square of their own value
                # this leads to an index of either 0 or 511
                index = (512 - 1) * image[i][j]
            else:
                square = ""
                for y in range(i - 1, i + 2):
                    for x in range(j - 1, j + 2):
                        square += str(image[y][x])
                index = int(square, 2)
            enhanced[i][j] = algorithm[index]
    return enhanced


for i in range(50):
    expand_image()
    image = enhance_image()
    print_image()

print(sum([sum(x) for x in image]))
