# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

number_of_players = 2
score_to_win = 21
die_size = 3

position = []
for i, e in enumerate(entries):
    e = e.split()
    position.append(int(e[-1]))


# create a dictionary with all possible values of the sum of three dice rolls
# this will allow us to run every sum only once instead of up to 7(!) times
die_list = []
die_sum = {}
for i in range(1, die_size + 1):
    for j in range(1, die_size + 1):
        for k in range(1, die_size + 1):
            die_list.append(i + j + k)
print(die_list)
for value in set(die_list):
    die_sum[value] = die_list.count(value)
print(die_sum)


def next_roll(score, pos, player, val):
    pos[player] = (pos[player] + val) % 10
    if pos[player] == 0:
        pos[player] = 10

    score[player] += pos[player]
    # print(f"Player {player + 1} rolls {val} and moves to space {pos[player]} for a score of {score[player]}.")
    if score[player] >= score_to_win:
        # print(f"Player {player + 1} wins")
        if player == 0:
            return 1, 0
        else:
            return 0, 1
    else:
        player = (player + 1) % number_of_players

    results = []
    for key, count in die_sum.items():
        result = next_roll(score.copy(), pos.copy(), player, key)
        results.append([count * x for x in result])
    return [sum(x) for x in zip(*results)]


total = []
for k, v in die_sum.items():
    res = next_roll([0, 0], position.copy(), 0, k)
    total.append([v * x for x in res])
print([sum(x) for x in zip(*total)])
