with open("input.txt", "r") as f:
    crabs = [int(x) for x in f.readline().split(",")]

max_position = max(crabs)

best_position = -1
min_cost = pow(max_position, 2)

for position in range(max_position + 1):
    cost = sum(map(lambda crab: abs(crab - position), crabs))
    if cost < min_cost:
        min_cost = cost
        best_position = position

print("Position", best_position, "Cost", min_cost)