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

	x = []
	for line in input_lines:
		d, l, c = line.split(" ")
		x.append((d, int(l), c))
	return x

directions = {
	"R": (0, 1),
	"D": (1, 0),
	"L": (0, -1),
	"U": (-1, 0),
	"0": (0, 1),
	"1": (1, 0),
	"2": (0, -1),
	"3": (-1, 0)
}

def part_one(input_data):

	# max_x = 0
	# min_x = 0
	x = 0

	# min_y = 0
	# max_y = 0
	y = 0

	# path = []

	area = 0
	perimeter = 0

	for d,l,c in input_data:
		dx,dy = directions[d]
		# path.append((dx,dy,l))
		dx,dy = dx*l, dy*l
		x = x+dy

		area += x * dx
		perimeter += l


	# plot border and try counting line by line
	#
	# 	x+=dx
	# 	max_x = max(max_x, x)
	# 	min_x = min(min_x, x)

	# 	y+=dy
	# 	max_y = max(max_y, y)
	# 	min_y = min(min_y, y)


	# m = max_x + abs(min_x) + 1
	# n = max_y + abs(min_y) + 1

	# x = m - max_x - 1
	# y = n - max_y - 1

	# world = [[0 for _ in range(n)] for _ in range(m)]

	# world[x][y] = 1
	# for dx,dy,l in path:
	# 	for _ in range(l):
	# 		x+=dx
	# 		y+=dy
	# 		world[x][y] = 1

	# total = 0
	# for i in range(m):
	# 	cur = False
	# 	for j in range(n):
	# 		if j!=0 and world[i][j-1] and world[i][j]:
	# 			print(1, end='')
	# 			total+=1
	# 			continue
	# 		if world[i][j]:
	# 			if not cur: 
	# 				total += 1
	# 			cur = not cur
	# 		total += cur
	# 		print(int(cur), end='')
	# 	print()

	return area+perimeter//2+1


#Picks theorem

def part_two(input_data):
	x,y = 0,0
	a,p = 0,0
	for d,l,c in input_data:
		(dx,dy),l = directions[c[-2]], int(c[-7:-2],16)
		x += dy*l
		a+=x*dx*l
		p+=l
	return a+p//2+1


input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)










