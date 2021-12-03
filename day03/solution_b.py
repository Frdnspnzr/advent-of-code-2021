def filter_readings(readings, position, expected):
    return [reading for reading in readings if reading[position] == expected]


def count_ones_in_position(readings, position):
    return len(filter_readings(readings, position, "1"))


readings = []

file = open('input.txt', 'r+')
for line in file.readlines():
    readings.append(line)
file.close()

o2_generator = list(readings)
co2_scrubber = list(readings)

pos = 0
while len(o2_generator) > 1:
    o2_generator = filter_readings(o2_generator, pos, "1" if count_ones_in_position(
        o2_generator, pos) >= len(o2_generator) / 2 else "0")
    pos += 1

pos = 0
while len(co2_scrubber) > 1:
    co2_scrubber = filter_readings(co2_scrubber, pos, "0" if count_ones_in_position(
        co2_scrubber, pos) >= len(co2_scrubber) / 2 else "1")
    pos += 1

print("O2 Generator: ", int(o2_generator[0], 2))
print("CO2 Scrubber: ", int(co2_scrubber[0], 2))
print("")
print("Life Support: ", int(o2_generator[0], 2) * int(co2_scrubber[0], 2))
