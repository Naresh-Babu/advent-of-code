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
		x.append(list(map(int,list(line))))

	return x


Right = (0, 1)
Down = (1, 0)
Left = (0, -1)
Up = (-1, 0)

def dis_pathfind(world_map, min_conse, max_conse):
	visited = set()
	worklist = [(0, 0, 0, Right, 1), (0, 0, 0, Down, 1)] # cost, x, y, _dir, _dir_count
	l_c = -1
	while len(worklist) > 0:
	    cost, x, y, _dir, _dir_count = heapq.heappop(worklist)
	    if (x, y, _dir, _dir_count) in visited:
	      continue
	    else:
	      visited.add((x, y, _dir, _dir_count))
	    new_x = x + _dir[1]
	    new_y = y + _dir[0]
	    if new_x < 0 or new_y < 0 or new_x >= len(world_map[0]) or new_y >= len(world_map):
	      continue
	    new_cost = cost + world_map[new_y][new_x]
	    if _dir_count >= min_conse and _dir_count <= max_conse:
	      if new_x == len(world_map[0]) - 1 and new_y == len(world_map) - 1:
	        return new_cost
	    for d in [Right, Down, Left, Up]:
	      # no reverse
	      if d[0] + _dir[0] == 0 and d[1] + _dir[1] == 0:
	        continue
	      new_d_count = _dir_count + 1 if d == _dir else 1
	      if (d != _dir and _dir_count < min_conse) or new_d_count > max_conse:
	        continue
	      heapq.heappush(worklist, (new_cost, new_x, new_y, d, new_d_count))

# Doesn't work check above code
def part_one(input_data):
	x = input_data
	m,n = len(x), len(x[0])


	visited=set()
	q = [(0, (0, 0), (1,0), 1), (0, (0, 0), (0, 1), 1)]


	mini = float('inf')
	while len(q) > 0:
		cur = heapq.heappop(q)

		loss, (i,j), (di,dj), dc = cur


		if ((i,j), (di,dj), dc) in visited:
			continue

		visited.add(((i,j), (di,dj), dc))

		ni = i + di
		nj = j + dj

		if ni < 0 or nj < 0 or ni >= m or nj >= n:
			continue

		nl = loss + x[ni][nj]

		if (ni,nj) == (m-1,n-1):
			return nl


		possible_directions = [
			(0, 1),
			(0, -1),
			(1, 0),
			(-1, 0)
		]

		
		possible_directions.remove((-di,-dj))
		if dc == 3:
			possible_directions.remove((di,dj))


		for r,c in possible_directions:
			if (r,c) == (di,dj):
				dc += 1
			else:
				dc = 1
			# if ((i+r, j+c), (r,c), dc) not in visited:
			# 	visited.add(((i+r, j+c), (r,c), dc))
			heapq.heappush(q, (nl, (ni, nj), (r,c), dc))


	# for i in range(m):
	# 	for j in range(n):
	# 		if (i,j) not in visited:
	# 			print("*", end = " ")
	# 		else:
	# 			print(visited[(i,j)], end = ' ')
	# 	print()
	return mini


def part_two(input_data):

	x = input_data
	m,n = len(x), len(x[0])

	maxEnergy = 0

	return maxEnergy


input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)

print(f"Part 1: {dis_pathfind(input_data, 1, 3)}")
print(f"Part 2: {dis_pathfind(input_data, 4, 10)}")









