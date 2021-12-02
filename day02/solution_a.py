def parse_command(command):
    parts = command.split(" ")
    return (parts[0], int(parts[1]))

file = open('input.txt', 'r+')
commands = [parse_command(command) for command in file.readlines()]
file.close()

depth = 0
position = 0

for command in commands:
    if command[0] == "forward":
        position += command[1]
    elif command[0] == "down":
        depth += command[1]
    else:
        depth -= command[1]

print("Depth: " + str(depth))
print("Position: " + str(position))

print("Solution: " + str(depth * position))