# com.workingnaresh.adventofcode

import io 
from dataclasses import dataclass
from functools import lru_cache

@dataclass
class CodedDocument:
	unknown: list[chr]
	defect: list[int]

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.split("\n")



	x = []
	for i in input_lines:
		(unknown, defect) = i.strip().split(" ")
		x.append(CodedDocument(unknown, list(map(int,defect.split(",")))))
	return x


code = []
defects = []

@lru_cache
def calculate_poss(i,j,c):
	global code, defects
	if i == len(code):
		return int(j == len(defects) and 0 == c or j == len(defects) - 1 and c == defects[-1])
	if j >= len(defects) or j == len(defects) - 1 and c == defects[-1]:
		if code[i] == "#":
			return 0
		else:
			return calculate_poss(i+1,j,c)

	cur = 0
	if code[i] != ".":
		if defects[j] >= c+1:
			cur += calculate_poss(i+1,j,c+1)
	if code[i] != "#":
		if c == 0:
			cur += calculate_poss(i+1,j,0)
		elif defects[j] == c:
			cur += calculate_poss(i+1,j+1,0)
	return cur

			

def part_one(input_data):
	global code, defects
	codes = input_data

	total = 0

	for value in codes:
		(ucode, udefects) = value.unknown, value.defect

		code = ucode
		defects = udefects
		total += calculate_poss(0,0,0)
		calculate_poss.cache_clear()

	return total

def part_two(input_data):
	global code, defects
	codes = input_data

	total = 0

	for value in codes:
		(ucode, udefects) = value.unknown, value.defect

		ucode += ("?"+ucode) * 4
		udefects = udefects * 5
		code = ucode
		defects = udefects
		total += calculate_poss(0,0,0)
		calculate_poss.cache_clear()


	return total


input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)









