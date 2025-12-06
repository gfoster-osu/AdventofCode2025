# Author: Garett Foster
# GitHub username: gfoster-osu
# Date: 2025-12-05

# Part 1:
puzzle_input = open('day5_data.txt')

ranges = list()
items = list()
fresh_counter = 0

for line in puzzle_input:
    if "-" in line:
        low, high = line.strip().split(sep = "-")
        tup = (int(low),int(high))
        ranges.append(tup)
    elif len(line.strip()) > 0:
        items.append(int(line.strip()))

for id_range in ranges:
    for item in items:
        if item in range(id_range[0],id_range[1] + 1):
            fresh_counter += 1
            items.remove(item)

print(fresh_counter)

puzzle_input.close()

# Part 2:
puzzle_input = open('day5_data.txt')

ranges = list()
for line in puzzle_input:
    if "-" in line:
        low, high = line.strip().split(sep = "-")
        id_range = [int(low),int(high)]
        ranges.append(id_range)

sorted_ranges = sorted(ranges, key = lambda x: x[0])

merged = list()
for index in range(len(sorted_ranges)):
    if len(merged) == 0:
        merged.append(sorted_ranges[index])
    elif sorted_ranges[index][0] <= merged[-1][1] + 1:
        merged[-1][1] = max(merged[-1][1],sorted_ranges[index][1])
    else:
        merged.append(sorted_ranges[index])

fresh_sum = 0
for id_range in merged:
    fresh_sum += id_range[1] - id_range[0] + 1
print(fresh_sum)

puzzle_input.close()