# direction = code[0]
# distance = code[1:]
# location = 50
# if direction == L, location - distance, else plus
# if location  < 0: location = 100 + location
# if location > 99: location = location - 100
# if location == 0, counter += 1

instructions = open('day1_data.txt')

#instructions = open('day1_example1.txt')

counter = 0
location = 50
for line in instructions:
    code = line.strip()
    direction = code[0]
    distance = int(code[1:])

    if direction == 'L':
        location = location - distance
    elif direction == 'R':
        location = location + distance
    else:
        print("Direction is fucked up")
        raise ValueError

    if location < 0:
        location = 100 + location
    elif location > 99:
        location = location - 100

    if location == 0:
        counter += 1

print(f'Counter: {counter}\nFinal Location: {location}')
