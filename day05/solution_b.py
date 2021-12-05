from collections import namedtuple

Coordinates = namedtuple("Coordinates", ["x", "y"])
Line = namedtuple("Line", ["start", "end"])

lines = []

highest_x = 0
highest_y = 0

with open("day05/input.txt", "r+") as f:
    for l in f.readlines():
        c = l.split(" -> ")
        start = c[0].split(",")
        end = c[1].split(",")
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
    x = line.start.x
    y = line.start.y
    inc_x = 1 if line.start.x < line.end.x else -1 if line.start.x > line.end.x else 0
    inc_y = 1 if line.start.y < line.end.y else -1 if line.start.y > line.end.y else 0
    while x != line.end.x or y != line.end.y:
        count[y][x] += 1
        x += inc_x
        y += inc_y
    count[line.end.y][line.end.x] += 1

dangerous = 0

for y in range(highest_y + 1):
    for x in range(highest_x + 1):
        if count[y][x] > 1:
            dangerous += 1

print(dangerous)
