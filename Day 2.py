# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-02

# Part 1:
import csv

file = open('day2_data.csv')
puzzle_input = csv.reader(file)
invalid_sum = 0

for line in puzzle_input:
    for i in range(len(line)):
        id_range = line[i]
        first_id, last_id = str(id_range).split("-")


file.close()