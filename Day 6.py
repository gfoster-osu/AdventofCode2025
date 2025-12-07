# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-06

# Part 1:
puzzle_input = open('day6_data.txt')

raw_matrix = list()

for line in puzzle_input:
    raw_row = line.strip().split(sep = " ")
    row = list()
    for i in range(len(raw_row)):
        if raw_row[i] == "+" or raw_row[i] == "*":
            row.append(raw_row[i])
        elif raw_row[i] != "":
            row.append(int(raw_row[i]))
    raw_matrix.append(row)

problems = list()
for i in range(len(raw_matrix[0])):
    problems.append(list())

for i in range(len(raw_matrix)):
    for j in range(len(raw_matrix[i])):
        problems[j].append(raw_matrix[i][j])

grand_total = 0
for row in problems:
    solution = None
    if row[-1] == "+":
        solution = 0
        for i in range(len(row) - 1):
            solution += row[i]
    else:
        solution = 1
        for i in range(len(row) - 1):
            solution *= row[i]

    grand_total += solution

print(grand_total)
puzzle_input.close()

# Part 2
puzzle_input = open('day6_data.txt')

raw_matrix = list()

for line in puzzle_input:
    cr = list()
    for i in line:
        cr.append(i)
    raw_matrix.append(cr)

transposed = reversed([list(row) for row in zip(*raw_matrix)])

grand_total = 0

operands = list()
operator = None
solution = 0

for line in transposed:
    digits = list()
    for i in range(len(line)):
        if line[i] == "+":
            number = int(''.join(map(str, digits)))
            operands.append(number)
            for x in operands:
                solution += x
            grand_total += solution
            solution = 0
            operands = list()
            digits = list()
        elif line[i] == "*":
            number = int(''.join(map(str, digits)))
            operands.append(number)
            solution = 1
            for x in operands:
                solution *= x
            grand_total += solution
            solution = 0
            operands = list()
            digits = list()
        elif i == len(line) - 1:
            if len(digits) > 0:
                number = int(''.join(map(str, digits)))
                operands.append(number)
        elif line[i].isdigit():
            digits.append(int(line[i]))

print(grand_total)

puzzle_input.close()