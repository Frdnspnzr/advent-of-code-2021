from collections import namedtuple

Coordinates = namedtuple("Coordinates", ["x", "y"])
Line = namedtuple("Line", ["start", "end"])

lines = []

highest_x = 0
highest_y = 0

with open("input.txt", "r+") as f:
    for l in f.readlines():
        c = l.split(" -> ")
        start = c[0].split(",")
        end = c[1].split(",")
        if int(start[0]) == int(end[0]) or int(start[1]) == int(end[1]):
            lines.append(Line(Coordinates(int(start[0]), int(
                start[1])), Coordinates(int(end[0]), int(end[1]))))
            highest_x = max(highest_x, int(start[0]), int(end[0]))
            highest_y = max(highest_y, int(start[1]), int(end[1]))

count = []
for x in range(highest_y+1):
    count.append([])
    for y in range(highest_x+1):
        count[x].append(0)


for line in lines:
    start_x = min(line.start.x, line.end.x)
    start_y = min(line.start.y, line.end.y)
    end_x = max(line.start.x, line.end.x)
    end_y = max(line.start.y, line.end.y)
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            count[y][x] += 1

dangerous = 0

for y in range(highest_y + 1):
    for x in range(highest_x + 1):
        if count[y][x] > 1:
            dangerous += 1

print(dangerous)
