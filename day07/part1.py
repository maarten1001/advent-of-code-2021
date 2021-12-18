# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

crabs = [int(x) for x in entries[0].split(",")]

minimum_pos = 0
minimum_fuel = sum(crabs)
for i in range(max(crabs) + 1):
    total = 0
    for c in crabs:
        total += abs(c - i)
    if total < minimum_fuel:
        minimum_fuel = total
        minimum_pos = i

print(f"Move to position {minimum_pos}: {minimum_fuel} fuel")
