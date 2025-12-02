# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-02

# Part 1:
import csv

file = open('day2_data.csv')
puzzle_input = csv.reader(file)
invalid_counter = 0

for line in puzzle_input:
    print(len(line))
    for i in range(len(line)):
        current_id = line[i]
        first_id, second_id = str(current_id).split("-")
        print(f'ID: {current_id}\tFirst: {first_id}\tSecond: {second_id}')
        first_win_max = len(first_id)//2



file.close()