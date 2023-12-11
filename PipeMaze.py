# com.workingnaresh.adventofcode

import io 

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.split("\n")

	x = []
	for i in input_lines:
		x.append(list(i.strip()))
	return x


directions = {
	"F":{"N": "E", "W":"S"},
	"J":{"S": "W", "E":"N"},
	"7":{"E": "S", "N":"W"},
	"L":{"W": "N", "S":"E"},
	"|":{"N": "N", "S":"S"},
	"-":{"E": "E", "W":"W"},
}

territory = {
	"F":{"N": [], "W":["N", "W"]},
	"J":{"S": [], "E":["S", "E"]},
	"7":{"E": [], "N":["E", "N"]},
	"L":{"W": [], "S":["W", "S"]},
	"|":{"N": ["E"], "S":["W"]},
	"-":{"E": ["S"], "W":["N"]},
}

travel = {
	"N":(-1,0),
	"E":(0,1),
	"W":(0,-1),
	"S":(1,0)
}

def part_one(input_data):
	x = input_data
	m,n = len(x), len(x[0])

	start = (0,0)
	for i in range(m):
		for j in range(n):
			if x[i][j] == "S":
				start = (i,j)

	cur = (start[0], start[1], "E") #hard coding initial direction
	steps = 0
	while True:
		d = travel[cur[2]]
		i = cur[0] + d[0]
		j = cur[1] + d[1]
		c = x[i][j]
		steps += 1
		if c == "S":
			break
		nex = directions[c][cur[2]]
		updated_direction = nex[int(cur[2] == nex[0])] if c not in ["|", "-"] else cur[2]

		cur = (i,j,updated_direction)
		
	return steps//2

def dfs(i,j,x):
	m,n = len(x), len(x[0])
	for (ci, cj) in travel.values():
		if i+ci < m and 0 <= i+ci and j+cj < n and 0 <= j+cj:
			if x[i+ci][j+cj] == ".":
				x[i+ci][j+cj] = "I"
				dfs(i+ci, j+cj, x)

def part_two(input_data):
	x = input_data
	m,n = len(x), len(x[0])

	start = (0,0)
	for i in range(m):
		for j in range(n):
			if x[i][j] == "S":
				start = (i,j)

	cur = (start[0], start[1], "E") #hard coding initial direction
	while True:
		d = travel[cur[2]]
		i = cur[0] + d[0]
		j = cur[1] + d[1]
		c = x[i][j]

		if c == "S":
			break
		nex = directions[c][cur[2]]
		ter = territory[c][cur[2]]
		for dirs in ter:
			for dir in dirs:
				td = travel[dir]
				ti = cur[0] + td[0]
				tj = cur[1] + td[1]
				if ti < m and 0 <= ti and tj < n and 0 <= tj and x[ti][tj] == ".":
					x[ti][tj] = "I"
					dfs(ti,tj,x)

		updated_direction = nex[int(cur[2] == nex[0])] if c not in ["|", "-"] else cur[2]

		x[i][j] = "*"

		cur = (i,j,updated_direction)
	
	count = 0
	for i in range(m):
		print(*x[i], sep='')
		for j in range(n):
			if x[i][j] == "I":
				count += 1

	return count



input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)









