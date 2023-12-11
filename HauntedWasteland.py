# com.workingnaresh.adventofcode

import io 

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.split("\n")

	steps = input_lines[0].strip()

	map = {}

	for i in range(2, len(input_lines)):
		start, direction = input_lines[i].split(" = ")
		left, right = direction[1:-1].split(", ")

		map[start] = (left, right)

	return (steps, map)


def calculate_steps(input_data):
	(steps, map) = input_data

	cur = "AAA"

	iter = 0
	
	while cur != "ZZZ":
		is_right = int(steps[iter%len(steps)] == 'R')
		cur = map[cur][is_right]
		iter += 1

	return iter

def gcd(a,b):
	if a==0:
		return b
	return gcd(b%a, a)

def calculate_total_steps(input_data):
	(steps, map) = input_data

	starts = list(filter(lambda x: x[-1] == "A", map.keys()))
	n = len(starts)

	cur = starts[:]

	indices = [[] for _ in range(n)]

	iter = 0
	while any(x[-1] != "Z" for x in cur) and not all(len(x) > 1 for x in indices):
		is_right = int(steps[iter%len(steps)] == 'R')
		for i in range(n):
			cur[i] = map[cur[i]][is_right]
			if cur[i][-1] == "Z":
				indices[i].append(iter)
		iter += 1

	diffs = []
	for i in indices:
		diffs.append(i[1] - i[0])

	g = diffs[0]

	m = diffs[0]
	for i in diffs[1:]:
		g = gcd(g, i)
		m *= i
	return m//(g**(n-1))



input_data = fetch_input()
steps = calculate_steps(input_data)
print(steps)

total_steps = calculate_total_steps(input_data)
print(total_steps)








