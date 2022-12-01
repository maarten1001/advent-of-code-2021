# get the input numbers
with open("test.txt") as f:
    entries = f.read().splitlines()

die_size = 3
position = []
for i, e in enumerate(entries):
    e = e.split()
    position.append(int(e[-1]))


class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.rolls = 0
        self.value = 0

    def roll(self):
        self.rolls += 1
        self.value = (self.value % self.sides) + 1
        return self.value

    def total_rolls(self):
        return self.rolls


def next_roll(score, pos, next_player, roll):
    pos[next_player] = (pos[next_player] + roll) % 10
    if pos[next_player] == 0:
        pos[next_player] = 10
    score[next_player] += pos[next_player]
    print(f"Player {next_player + 1} rolls ", end="")
    print(roll, sep="+", end="")
    print(f" and moves to space {pos[next_player]} for a total score of {score[next_player]}.")

    if score[next_player] >= 6:
        print(f"Player {next_player + 1} wins the game with a score of {score[next_player]}")
        if next_player == 0:
            return 1, 0
        else:
            return 0, 1
    else:
        next_player = (next_player + 1) % 2
        first = next_roll(score.copy(), pos.copy(), next_player, 1)
        second = next_roll(score.copy(), pos.copy(), next_player, 2)
        third = next_roll(score.copy(), pos.copy(), next_player, 3)
        print([sum(x) for x in zip(first, second, third)])
        return [sum(x) for x in zip(first, second, third)]


total = []
for i in range(1, die_size + 1):
    total.append(next_roll([0, 0], position, 0, i))
print()
print([sum(x) for x in zip(*total)])
