package com.workingnaresh.adventofcode

import java.io.File

val directions = listOf(
	Pair(-1,-1), Pair(-1,0), Pair(-1,1), Pair(0,-1), Pair(0,1), Pair(1,-1), Pair(1,0), Pair(1,1)
)

//Part 1
fun explore(lines: List<String>): String {
	var partSum = 0

	for (i in 0 until lines.size) {
		var number = 0
		var isSymbolNear = false
		for (j in 0 until lines[i].length) {
			if (lines[i][j].isDigit()) {
				isSymbolNear = isSymbolNear || directions.any { (di,dj) ->
					val r = i + di
					val c = j + dj
					if (!(r in 0 until lines.size && c in 0 until lines[i].length)) return@any false
					!lines[r][c].isDigit() && lines[r][c] != '.'
				}
				number = (number * 10) + lines[i][j].toString().toInt()
			} else {
				if (isSymbolNear && number > 0) partSum += number
				number = 0
				isSymbolNear = false
			}
		}
		if (isSymbolNear && number > 0) partSum += number
	}

	return partSum.toString()
}

//Part 2
fun venture(lines: List<String>): String {
	var gearRatio = 0

	val gearIndices = mutableMapOf<Pair<Int,Int>, List<Int>>()

	for (i in 0 until lines.size) {
		var number = 0
		var isSymbolNear: Pair<Int,Int>? = null
		for (j in 0 until lines[i].length) {
			if (lines[i][j].isDigit()) {
				if (isSymbolNear == null) {
					val symbolLocations = directions.mapNotNull { (di,dj) ->
						val r = i + di
						val c = j + dj
						if (!(r in 0 until lines.size && c in 0 until lines[i].length)) return@mapNotNull null
						if (lines[r][c] == '*') Pair(r,c) else null
					}
					if (symbolLocations.isNotEmpty()) isSymbolNear = symbolLocations[0]
				}
				number = (number * 10) + lines[i][j].toString().toInt()
			} else {
				if (isSymbolNear != null && number > 0) {
					val value = gearIndices.getOrDefault(isSymbolNear, mutableListOf()).plus(number)
					gearIndices[isSymbolNear] = value
				}
				number = 0
				isSymbolNear = null
			}
		}
		if (isSymbolNear != null && number > 0) {
			val value = gearIndices.getOrDefault(isSymbolNear, mutableListOf()).plus(number)
			gearIndices[isSymbolNear] = value
		}
	}

	for ((location, numbers) in gearIndices) {
		if (numbers.size == 2) {
			gearRatio += numbers[0] * numbers[1]
		}
	}

	return gearRatio.toString()
}


fun main() {
	val inputFileString = File("./input.txt").readText()
	val inputLines = inputFileString.split("\n").map(String::trim)

	//Part 1
	val treasure = explore(inputLines)
	println(treasure)

	//Part 2
	val glory = venture(inputLines)
	println(glory)
}
