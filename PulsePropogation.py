#!/usr/bin/python3
# com.workingnaresh.adventofcode

import io 
import sys
from dataclasses import dataclass
from functools import lru_cache
import heapq
from collections import defaultdict


sys.setrecursionlimit(5000)

def reverse_adj_list(adj_list):
    reversed_adj_list = {vertex: [] for vertex in adj_list}

    for vertex, neighbors in adj_list.items():
        for neighbor in neighbors:
            if neighbor == "output": continue
            reversed_adj_list[neighbor].append(vertex)

    return reversed_adj_list

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.strip().split("\n")

	x = defaultdict(list)
	t = {}
	v = {}

	for line in input_lines:
		if "broad" in line:
			entries = line.split(" -> ")[1].split(", ")
			x["broad"] = list(entries)
			v["broad"] = 0
		else:
			name, children = line.split(" -> ")
			operation, name = name[0], name[1:]
			t[name] = operation
			x[name] = list(children.split(", "))
			v[name] = 0

	return (x,v,t, reverse_adj_list(x))

def part_one(input_data):


	'''
	Doesn't work, 

	but assummed theory,  - do BFS but do not add node to queue if 
	already there, maintain flipflop snapshots to find cycle and use 
	that to calculate the value.


	flip-flop (%)

	a b o
	-----
	0 0 1
	0 1 0
	1 0 0
	1 1 1
	
	!(a^b)
	
	conjuction (&)

	a b o
	-----
	0 0 1
	0 1 1
	1 0 1
	1 1 0

	!(a&b&c)

	broadcast (b)

	a o
	---
	0 0
	1 1

	button --0--> broadcast

	'''
	x,v,t,r = input_data
	low = 0
	high = 0

	for _ in range(1):
		q = [("broad",0)]
		low += 1
		visited = set()
		while len(q) > 0:
			module, signal = q.pop(0)
			
			visited.add((module, signal))

			if module == "output":
				continue
			children = x[module]

			if module in t:
				a,b = v[module], signal

				if t[module] == "%":
					signal = int(not a) if not signal else a
				else:
					if all(v[child] == 1 for child in r[module]):
						signal = 0
					else:
						signal = 1

			if signal:
				high += len(children)
			else:
				low += len(children)
			v[module] = signal

			for child in children:
				print(module, signal, child)
				if (child,signal) not in visited:
					q.append((child, signal))
				else:
					print("skipped", (child,signal) ,module)
			print(q)
		print()
	print(high,low)
	return high * low



def part_two(input_data):
	result = 0

	return result

input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)










