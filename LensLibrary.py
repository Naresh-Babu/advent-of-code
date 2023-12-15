#!/usr/bin/python3
# com.workingnaresh.adventofcode

import io 
from dataclasses import dataclass
from functools import lru_cache


def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.replace("\n","").split(",")


	return input_lines
			

def gen_hash(word: str) -> int:
	hash = 0
	for char in word:
		hash += ord(char)
		hash = (hash*17)%256
	return hash
def part_one(input_data):
	ciphers = input_data
	total = 0
	for word in ciphers:
		total += gen_hash(word)
	return total


def part_two(input_data):
	ciphers = input_data
	h = [[] for _ in range(256)]

	total = 0
	for word in ciphers:
		if word[-1] != "-":
			text, operation, focal = word[:-2], word[-2], int(word[-1])
		else:
			text, operation = word[:-1], word[-1]

		hash = gen_hash(text)
		lens = h[hash]


		for i in range(len(lens)):
			if lens[i][0] == text:
				if operation == "=":
					lens[i] = (text, focal)
				else:
					lens.pop(i)
				break
		else:
			if operation == "=":
				lens.append((text, focal))
		h[hash] = lens

	for i in range(256):
		lens = h[i]
		for pos, focal in enumerate(lens):
			total += (i+1) * (pos+1) * focal[1]
	return total


input_data = fetch_input()
one = part_one(input_data)
print(one)

two = part_two(input_data)
print(two)









