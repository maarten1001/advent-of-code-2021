# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

score = [0, 0]
position = []
next_player = 0
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


die = Dice(100)
while True:
    turn = []
    for i in range(3):
        turn.append(die.roll())
    position[next_player] = (position[next_player] + sum(turn)) % 10
    if position[next_player] == 0:
        position[next_player] = 10
    score[next_player] += position[next_player]
    print(f"Player {next_player + 1} rolls ", end="")
    print(*turn, sep="+", end="")
    print(f" and moves to space {position[next_player]} for a total score of {score[next_player]}.")
    if score[next_player] >= 1000:
        print()
        print(f"Player {next_player + 1} wins the game with a score of {score[next_player]}")
        next_player = (next_player + 1) % 2
        print(f"{score[next_player]} * {die.total_rolls()} = {score[next_player] * die.total_rolls()}")
        break
    next_player = (next_player + 1) % 2
