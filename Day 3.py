# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-03

# Part 1:
# puzzle_input = open('day3_data.txt')
#
# total_joltage = 0
#
# for line in puzzle_input:
#     ones_max = -1
#     tens_max = 1
#     tens_index = -1
#     for i in range(len(line.strip())-1):
#         digit = int(line[i])
#         if digit > tens_max:
#             tens_max = digit
#             tens_index = i
#     for i in range(tens_index+1,len(line.strip())):
#         digit = int(line[i])
#         if digit > ones_max:
#             ones_max = digit
#     bank_joltage = int(str(tens_max)+str(ones_max))
#     total_joltage += bank_joltage
#     print(tens_max, ones_max, bank_joltage)
#
# print(total_joltage)
# puzzle_input.close()

# Part 2:
puzzle_input = open('day3_example.txt')

total_joltage = 0

for line in puzzle_input:
    ones_max = -1
    start_max = -1
    start_index = -1
    for i in range(len(line.strip())-11):
        digit = int(line[i])
        if digit > start_max:
            start_max = digit
            start_index = i
    for i in range(start_index+1,len(line.strip())):
        digit = int(line[i])
        if digit > ones_max:
            ones_max = digit
    bank_joltage = int(str(tens_max)+str(ones_max))
    total_joltage += bank_joltage
    print(tens_max, ones_max, bank_joltage)

print(total_joltage)
puzzle_input.close()