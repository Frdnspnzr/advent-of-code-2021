file = open('input.txt', 'r+')
readings = [int(line) for line in file.readlines()]
file.close()

count = 0

windows = []

for i in range(len(readings) - 2):
    s = readings[i] + readings[i + 1] + readings[i + 2]
    windows.append(s)

prev_reading = windows[0]

for reading in windows:
    if reading > prev_reading:
        count += 1
    prev_reading = reading

print(count)