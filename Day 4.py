# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-04

# Part 1:
puzzle_input = open('day4_data.txt')

matrix = list()

for line in puzzle_input:
    matrix.append(list(line.strip()))

open_counter = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '@':
            adjacent_counter = 0
            for k in range(i - 1, i + 2):
                if k >= 0 and k < len(matrix):
                    for l in range(j - 1, j + 2):
                        if l >= 0 and l < len(matrix[i]):
                            if matrix[k][l] == '@':
                                adjacent_counter += 1
            if adjacent_counter < 5:
                open_counter += 1

print(open_counter)
puzzle_input.close()