# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-01

# Part 1:
puzzle_input = open('day1_data.txt')

counter = 0
location = 50
for line in puzzle_input:
    code = line.strip()
    direction = code[0]
    distance = int(code[1:])

    if direction == 'L':
        location = location - distance
    else:
        location = location + distance

    while location < 0:
        location = 100 + location
    while location > 99:
        location = location - 100

    if location == 0:
        counter += 1

print(f'Part 1 Counter: {counter}')

# Part 2:
puzzle_input = open('day1_data.txt')

counter = 0
location = 50

for line in puzzle_input:
    code = line.strip()
    direction = code[0]
    distance = int(code[1:])

    if direction == "L":
        for i in range(distance):
            location -= 1
            if location == 0:
                counter += 1
            elif location == -1:
                location = 99
    else:
        for i in range(distance):
            location += 1
            if location == 100:
                location = 0
                counter += 1

print(f'Part 2 Counter: {counter}')