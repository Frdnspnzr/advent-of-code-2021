file = open('input.txt', 'r+')
readings = [int(line) for line in file.readlines()]
file.close()

count = 0

prev_reading = readings[0]

for reading in readings:
    if reading > prev_reading:
        count += 1
    prev_reading = reading

print(count)