# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-02

# Part 1:
# import csv
#
# file = open('day2_data.csv')
# puzzle_input = csv.reader(file)
# invalid_sum = 0
#
# for line in puzzle_input:
#     for i in range(len(line)):
#         id_range = line[i]
#         first_id, last_id = str(id_range).split("-")
#         for prod_id in range(int(first_id), int(last_id) + 1):
#             test_id = str(prod_id)
#             if len(test_id) % 2 == 0:
#                 slicer = int(len(test_id)/2)
#                 if test_id[:(slicer)] == test_id[slicer:]:
#                     invalid_sum += prod_id
#
# print(invalid_sum)
#
# file.close()

# Part 2:
import csv

file = open('day2_example.txt')
puzzle_input = csv.reader(file)
invalid_sum = 0

for line in puzzle_input:
    for i in range(len(line)):
        id_range = line[i]
        first_id, last_id = str(id_range).split("-")
        for prod_id in range(int(first_id), int(last_id) + 1):
            test_id = str(prod_id)
            window_range = len(test_id)//2
            test_list = list()
            for i in range(1,window_range+1):
                if len(test_id) % i == 0:
                    test_list.append(i)
            for test_range in test_list:
                start_index = 0
                while (test_id[start_index:(start_index + test_range)] ==
                       test_id[(start_index + test_range):(start_index + test_range*2)]):
                    start_index += test_range
                    if start_index == len(test_id) - test_range:
                        invalid_sum += prod_id

print(invalid_sum)
file.close()