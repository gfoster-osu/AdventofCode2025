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
        for prod_id in range(int(first_id), int(last_id) + 1):
            test_id = str(prod_id)
            if len(test_id) % 2 == 0:
                slicer = int(len(test_id)/2)
                if test_id[:(slicer)] == test_id[slicer:]:
                    invalid_sum += prod_id

print(invalid_sum)

file.close()