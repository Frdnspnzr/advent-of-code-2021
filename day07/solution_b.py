
with open("input.txt", "r") as f:
    crabs = [int(x) for x in f.readline().split(",")]

max_position = max(crabs)

lookup = [sum(range(steps + 1)) for steps in range(max_position + 1)]
print(lookup)

best_position = -1
min_cost = 9999999999999

for position in range(max_position + 1):
    cost = sum(map(lambda crab: lookup[abs(crab - position)], crabs))
    if cost < min_cost:
        min_cost = cost
        best_position = position

print("Position", best_position, "Cost", min_cost)