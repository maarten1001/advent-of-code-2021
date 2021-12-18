# get the input numbers
import sys

with open("input.txt") as f:
    entries = f.read().splitlines()

crabs = [int(x) for x in entries[0].split(",")]

minimum_pos = 0
minimum_fuel = sys.maxsize
for i in range(max(crabs) + 1):
    total = 0
    for c in crabs:
        # each step becomes more expensive
        n = abs(c - i)
        total += int(0.5 * n * (n + 1))
    if total < minimum_fuel:
        minimum_fuel = total
        minimum_pos = i

print(f"Move to position {minimum_pos}: {minimum_fuel} fuel")
