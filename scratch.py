


instructions = open('day1_data.txt')

counter = 0
location = 50

for line in instructions:
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