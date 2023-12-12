# com.workingnaresh.adventofcode

import io 

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.split("\n")

	x = []
	for i in input_lines:
		x.append(list(i.strip()))
	return x




def expanded_dist_calc(input_data, size):
	x = input_data
	m,n = len(x), len(x[0])

	empty_columns = set()
	empty_rows = set()

	for i in range(m):
		if all(x[i][j] == "." for j in range(n)):
			empty_rows.add(i)
	for j in range(n):
		if all(x[i][j] == "." for i in range(m)):
			empty_columns.add(j)


	points = []
	extra_rows = 0
	for i in range(m):
		if i in empty_rows:
			extra_rows += 1
			continue
		extra_columns = 0
		for j in range(n):
			if j in empty_columns:
				extra_columns += 1

			if x[i][j] == "#":
				points.append((i + extra_rows*(size-1), j + extra_columns*(size-1)))

	dist = 0

	for i in range(len(points)-1):
		for j in range(i+1, len(points)):
			dist += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

	return dist



def part_one(input_data):
	return expanded_dist_calc(input_data, 2)



# Doesn't work - tried
def part_two(input_data):
	return expanded_dist_calc(input_data, 1000000)





input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)









