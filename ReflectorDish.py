# com.workingnaresh.adventofcode

import io 
from dataclasses import dataclass
from functools import lru_cache


def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.split("\n")


	x = []
	for i in input_lines:
		x.append(list(i.strip()))
	return x
			

def part_one(input_data):
	x = input_data
	total = 0

	m,n = len(x), len(x[0])

	load = 0
	for column in zip(*x):
		rocks = 0
		for j in range(1, n+1):
			if column[n-j] == "O":
				rocks += 1
			elif column[n-j] == "#" and rocks > 0:
				load += j*(j-1)//2 - (j-rocks-1)*(j-rocks)//2
				rocks = 0
		load += j*(j+1)//2 - (j-rocks)*(j-rocks+1)//2
	return load


def tilt_and_rotate(x):
	m,n = len(x), len(x[0])

	for j in range(n):
		rocks = 0
		for i in range(m-1,-1,-1):
			if x[i][j] == "O":
				rocks += 1
				x[i][j] = "."
			elif x[i][j] == "#":
				while rocks > 0:
					x[i+rocks][j] = "O"
					rocks -= 1

		while rocks > 0:
			x[i+rocks-1][j] = "O"
			rocks -= 1

	t = []

	for row in zip(*x):
		t.append(list(row)[::-1])

	return t

def calc_load(x):
	m,n = len(x), len(x[0])

	load = 0
	for j in range(n-1,-1,-1):
		for i in range(m):
			if x[i][j] == "O":
				load += m-i


	return load

def hash_table(x):
	return ''.join(''.join(t) for t in x)


def print_table(x):
	print()
	for k in x:
		print(*k)
	print()

def part_two(input_data):
	x = input_data
	total = 0

	cache = {}
	cost_cache = {}
	cost_cache[0] = calc_load(x)

	cycle = 0

	while True:
		if hash_table(x) in cache:
			cycle_start = cache[hash_table(x)] 
			mod = cycle - cycle_start
			rem = (10**9-cycle_start) % mod
			print(cycle_start, cycle, mod, rem, rem + cycle_start)
			return cost_cache[rem + cycle_start]
		else:
			cache[hash_table(x)] = cycle
			for _ in range(4):
				x = tilt_and_rotate(x)
			cycle += 1

			cost_cache[cycle] = calc_load(x)


input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)









