# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

entries = [int(x) for x in entries[0].split(",")]

# we don't need to track each individual fish
# instead we keep a list of the total number of fish in each timer value
today = [0 for x in range(9)]
for e in entries:
    today[e] += 1

print(f"Initial state:  {today}")
for day in range(256):
    tomorrow = today.copy()
    for counter, fish in enumerate(today):
        if counter == 0:
            # reset the counter
            tomorrow[8] = fish
        elif counter == 7:
            # add the new fish
            tomorrow[6] = fish + today[0]
        else:
            tomorrow[counter - 1] = fish
    today = tomorrow
    print("After", end=" ")
    print('{:>3}'.format(day + 1), end=" ")
    print(f"days: {sum(today)} fish")
