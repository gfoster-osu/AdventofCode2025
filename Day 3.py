# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-03

# Part 1:
puzzle_input = open('day3_data.txt')

total_joltage = 0

for line in puzzle_input:
    ones_max = -1
    tens_max = 1
    tens_index = -1
    for i in range(len(line.strip())-1):
        digit = int(line[i])
        if digit > tens_max:
            tens_max = digit
            tens_index = i
    for i in range(tens_index+1,len(line.strip())):
        digit = int(line[i])
        if digit > ones_max:
            ones_max = digit
    bank_joltage = int(str(tens_max)+str(ones_max))
    total_joltage += bank_joltage

print(total_joltage)
puzzle_input.close()

# Part 2:
puzzle_input = open('day3_data.txt')

total_joltage = 0

for line in puzzle_input:
    digit_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    prev_index = -1
    for digit_to_find in range(0,12):
        digit_max = -1
        for i in range(prev_index + 1, len(line.strip()) - (11-digit_to_find)):
            digit = int(line[i])
            if digit > digit_max:
                digit_list[digit_to_find] = digit
                digit_max = digit
                prev_index = i
    bank_joltage = int(''.join(map(str,digit_list)))
    total_joltage += bank_joltage

print(total_joltage)
puzzle_input.close()