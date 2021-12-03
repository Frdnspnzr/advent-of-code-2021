lines = 0
ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

file = open('input.txt', 'r+')
for line in file.readlines():
    lines += 1
    for i in range(12):
        if line[i] == '1':
            ones[i] += 1
file.close()

gamma = ""
epsilon = ""

for i in range(12):
    if ones[i] >= lines / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("")
print("Gamma: ", int(gamma, 2))
print("Epsilon: ", int(epsilon, 2))
print("")
print("Consumption: ", int(gamma, 2) * int(epsilon, 2))