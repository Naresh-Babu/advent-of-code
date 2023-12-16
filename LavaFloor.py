#!/usr/bin/python3
# com.workingnaresh.adventofcode

import io 
import sys
from dataclasses import dataclass
from functools import lru_cache


sys.setrecursionlimit(5000)

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.strip().split("\n")

	x = []
	for line in input_lines:
		x.append(list(line))

	coding = {".":0, "\\": 1, "/": 2, "|": 3, "-": 4}
	for i in range(len(x)):
		for j in range(len(x[0])):
			x[i][j] = coding[x[i][j]]
	return x

paths = {
	(1, (0,1)): [(1,0)],
	(1, (1,0)): [(0,1)],
	(1, (0,-1)): [(-1,0)],
	(1, (-1,0)): [(0,-1)],
	(2, (0,1)): [(-1,0)],
	(2, (1,0)): [(0,-1)],
	(2, (0,-1)): [(1,0)],
	(2, (-1,0)): [(0,1)],
	(3, (0,1)): [(1,0), (-1,0)],
	(3, (1,0)): [(1,0)],
	(3, (0,-1)): [(1,0), (-1,0)],
	(3, (-1,0)): [(-1,0)],
	(4, (0,1)): [(0,1)],
	(4, (1,0)): [(0,1), (0,-1)],
	(4, (0,-1)): [(0,-1)],
	(4, (-1,0)): [(0,1), (0,-1)]
}


visited = set()
visited_direction = set()
def dfs(cur,x):
	global visited_direction, visited
	m,n = len(x), len(x[0])
	location, direction = cur
	i,j = location
	if not(0<=i<m and 0<=j<n) or cur in visited_direction: return
	visited.add((i,j))
	visited_direction.add(cur)


	future = [] 
	symbol = x[i][j]
	if symbol == 0:
		future.append(((i+direction[0], j+direction[1]), direction))
	else:
		possibles = paths[(symbol, direction)]
		for r,c in possibles:
			future.append(((i+r,j+c), (r,c)))

	for curFuture in future:
		if curFuture not in visited_direction:
			dfs(curFuture, x)

		


def part_one(input_data):
	global visited_direction, visited

	x = input_data
	start = ((0,0), (0,1))

	visited = set()
	visited_direction = set()

	dfs(start,x)

	return len(visited)


def part_two(input_data):
	global visited_direction, visited

	x = input_data
	m,n = len(x), len(x[0])

	maxEnergy = 0

	startEdges = [
		((0,0), (0,1)),
		((0,0), (1,0)),
		((0,n-1), (0,-1)),
		((0,n-1), (1,0)),
		((m-1,0), (0,1)),
		((m-1,0), (-1,0)),
		((m-1,n-1), (0,-1)),
		((m-1,n-1), (-1,0))
	]

	for i in range(1, n-1):
		startEdges.append(((0,i), (1,0)))
		startEdges.append(((m-1,i), (-1,0)))

	for i in range(1, m-1):
		startEdges.append(((i, 0), (0,1)))
		startEdges.append(((i, n-1), (0,-1)))

	for edge in startEdges:
		visited = set()
		visited_direction = set()
		dfs(edge, x)
		maxEnergy = max(maxEnergy, len(visited))

	return maxEnergy


input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)









