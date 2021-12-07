counters = [0, 0, 0, 0, 0, 0, 0, 0 ,0]
with open("input.txt", "r") as f:
    for x in f.readline().split(","):
        counters[int(x)] += 1

for _ in range(256):
    new_counters = [0, 0, 0, 0, 0, 0, 0, 0 ,0]
    for i in range(0, 8):
        new_counters[i] = counters[i+1]
    new_counters[8] = counters[0]
    new_counters[6] += counters[0]
    counters = new_counters

print(sum(counters))