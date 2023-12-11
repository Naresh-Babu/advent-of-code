# com.workingnaresh.adventofcode

import io 

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.split("\n")

	patterns = []

	for line in input_lines:
		patterns.append(list(map(int, line.strip().split(" "))))

	return patterns


def part_one(input_data):
	patterns = input_data

	total = 0

	for pattern in patterns:
		form = [pattern]
		stack = []
		while any(value != 0 for value in form[-1]):
			cur = []
			for i in range(len(form[-1])-1):
				cur.append(form[-1][i+1] - form[-1][i])

			stack.append(form[-1][-1])
			form.append(cur)
		total += sum(stack)

	return total


def part_two(input_data):
	patterns = input_data

	total = 0

	for pattern in patterns:
		form = [pattern]
		stack = []
		while any(value != 0 for value in form[-1]):
			cur = []
			for i in range(len(form[-1])-1):
				cur.append(form[-1][i+1] - form[-1][i])

			stack.append(form[-1][0])
			form.append(cur)
		diff = 0

		for s in stack[::-1]:
			diff = s - diff

		total += diff

	return total


input_data = fetch_input()
value_one = part_one(input_data)
print(value_one)

value_two = part_two(input_data)
print(value_two)








