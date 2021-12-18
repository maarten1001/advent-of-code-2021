# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

today = [int(x) for x in entries[0].split(",")]

print(f"Initial state: {today}")
for day in range(80):
    tomorrow = today.copy()
    for i, fish in enumerate(today):
        if today[i] == 0:
            tomorrow[i] = 6
            tomorrow.append(8)
        else:
            tomorrow[i] = today[i] - 1
    today = tomorrow
    print("After", end=" ")
    print('{:>2}'.format(day + 1), end=" ")
    # print(f"days: {today}", end=" ")
    print(f"days: {len(today)} fish")
