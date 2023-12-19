#!/usr/bin/python3
# com.workingnaresh.adventofcode

import io 
import sys
from dataclasses import dataclass
from functools import lru_cache
import heapq
from collections import defaultdict


sys.setrecursionlimit(5000)

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.strip().split("\n")


	is_second = False


	workflows = {}
	parts = []
	for line in input_lines:
		if line == "":
			is_second = True
			continue
		if not is_second:
			name, secondPart = line.split("{")
			commands = secondPart.replace("}", "").split(",")
			workflows[name] = commands
		else:
			splits = line[1:-1].split(",")

			part = []
			for i in splits:
				part.append(int(i.split("=")[1]))
			parts.append(part)

	return (workflows, parts)

def evaluate(part, expression):
	if ":" not in expression:
		return expression
	else:
		condition, jump = expression.split(":")
		i = "xmas".index(condition[0])
		number = int(condition[2:])
		if ">" in condition and part[i] > number or "<" in condition and part[i] < number:
			return jump

	return None




def part_one(input_data):
	(workflows, parts) = input_data
	result = 0
	for part in parts:
		cur = "in"

		while cur not in ("R", "A"):
			for command in workflows[cur]:
				jump_to = evaluate(part, command)
				if jump_to:
					cur = jump_to
					break
		if cur == "A":
			result += sum(part)

	return result


def evaluate_two(high, low, expression):
	if ":" not in expression:
		return expression
	else:
		condition, jump = expression.split(":")
		i = "xmas".index(condition[0])
		number = int(condition[2:])
		if ">" in condition:
			low[i] = max(low[i], number + 1)
		elif "<" in condition:
			high[i] = min(high[i], number - 1)
		return jump
def decimate(high, low, expression):
	if ":" not in expression:
		return (high,low)
	else:
		condition, jump = expression.split(":")
		i = "xmas".index(condition[0])
		number = int(condition[2:])
		if ">" in condition:
			high[i] = min(high[i], number)
		elif "<" in condition:
			low[i] = max(low[i], number)
		return high,low

def calc(high,low):
	total = 1
	for h,l in zip(high,low):
		total *= (h - l + 1)
	return total

def part_two(input_data):
	(workflows, parts) = input_data
	result = 0

	cur = "in"
	high = (4000, 4000, 4000, 4000)
	low = (1,1,1,1)

	q = [(cur,high,low)]

	while len(q)> 0:
		(cur,high,low) = q.pop()
		if cur == "A":
			result += calc(high,low)
			continue
		if cur == "R":
			continue

		for command in workflows[cur]:
			t_high,t_low = list(high), list(low)
			jump_to = evaluate_two(t_high, t_low, command)
			q.append((jump_to, tuple(t_high), tuple(t_low)))
			high,low = decimate(list(high), list(low), command)

	return result

input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)










