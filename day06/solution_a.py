with open("input.txt", "r") as f:
    fish = [int(x) for x in f.readline().split(",")]

for _ in range(80):
    newfish = []
    for f in fish:
        if f == 0:
            newfish.append(8)
            newfish.append(6)
        else:
            newfish.append(f-1)
    fish = newfish

print(len(newfish))
