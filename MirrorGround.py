# com.workingnaresh.adventofcode

import io 
from dataclasses import dataclass
from functools import lru_cache


def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.split("\n")

	patterns = []

	x = []
	for i in input_lines:
		if i.strip() == "":
			patterns.append(x)
			x = []
		else:
			x.append(list(i.strip()))
	return patterns
			

def part_one(input_data):
	patterns = input_data
	total = 0

	for x in patterns:
		m,n = len(x), len(x[0])

		max_row = 0
		for i in range(1, m):
			j = 1
			while i-j >= 0 and i+j-1 < m :
				if x[i-j] != x[i+j-1]:
					break
				j+=1
			else:
				max_row = i


		t = []

		for i in zip(*x):
			t.append(list(i))

		x = t


		max_col = 0
		for j in range(1, n):
			i = 1
			while j-i >= 0 and i+j-1 < n :
				if x[j-i] != x[i+j-1]:
					break
				i+=1
			else:
				max_col = j

		total += max_row*100 + max_col


	return total

def part_two(input_data):
	patterns = input_data
	total = 0

	for x in patterns:

		m,n = len(x), len(x[0])

		max_row = 0
		for i in range(1, m):
			j = 1
			cost = 0
			while i-j >= 0 and i+j-1 < m :
				cost +=	sum([int(x[i-j][k] != x[i+j-1][k]) for k in range(n)])
				if cost > 1:
					break
				j+=1
			else:
				if cost == 1:
					max_row = i


		t = []

		for i in zip(*x):
			t.append(list(i))

		x = t

		max_col = 0
		for j in range(1, n):
			i = 1
			cost = 0
			while j-i >= 0 and i+j-1 < n :
				cost +=	sum([int(x[j-i][k] != x[i+j-1][k])for k in range(m)])
				if cost > 1:
					break
				i+=1
			else:
				if cost == 1:
					max_col = j

		total += max_row*100 + max_col


	return total


input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)









