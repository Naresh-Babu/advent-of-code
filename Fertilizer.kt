package com.workingnaresh.adventofcode

import java.io.File
import kotlin.math.min

fun explore(lines: List<String>): String {
	// Pre-process
	val numberRegex = """(\d+)""".toRegex()

	val seeds = lines[0].run(numberRegex::findAll).map(MatchResult::value).map(String::toLong).toList()
	val rangeMaps = Array(7) { mutableListOf<List<Long>>()}
	var iter = 0

	for (l in 3 until lines.size) {
		val curLine = lines[l]
		if (curLine == "") continue
		if (curLine.contains(":")) {
			iter++
			continue
		}

		val numbers = curLine.run(numberRegex::findAll).map(MatchResult::value).map(String::toLong).toList()

		rangeMaps[iter] += numbers
	}

	// Logic - Part 1

	val locations: List<Long> = seeds.map { seed -> 
		var searcher = seed
		rangeMaps.forEach { mapList ->
			for ((destination, source, range) in mapList ) {
				if (searcher >= source && searcher < source+range) {
					searcher = searcher - source + destination
					break
				}
			}
		}
		searcher
	}

	return locations.min().toString()
}

fun venture(lines: List<String>): String {
	// Pre-process
	val numberRegex = """(\d+)""".toRegex()

	val seeds = lines[0].run(numberRegex::findAll).map(MatchResult::value).map(String::toLong).toList()
	val rangeMaps = Array(7) { mutableListOf<List<Long>>()}
	var iter = 0

	for (l in 3 until lines.size) {
		val curLine = lines[l]
		if (curLine == "") continue
		if (curLine.contains(":")) {
			iter++
			continue
		}

		val numbers = curLine.run(numberRegex::findAll).map(MatchResult::value).map(String::toLong).toList()

		rangeMaps[iter] += numbers
	}

	// Logic - Part 2

	var location = Long.MAX_VALUE

	val expandedSeeds = mutableListOf<Long>()
	(0 until seeds.size step 2).toList().parallelStream().forEach { i ->
		for (seed in seeds[i] until (seeds[i]+seeds[i+1])) {
			var searcher = seed
			rangeMaps.forEach { mapList ->
				for ((destination, source, range) in mapList ) {
					if (searcher >= source && searcher < source+range) {
						searcher = searcher - source + destination
						break
					}
				}
			}
			location = min(location,searcher)
		}
	}

	return location.toString()
}


fun main() {
	val inputFileString = File("./input.txt").readText()
	val inputLines = inputFileString.split("\n").map(String::trim)

	val treasure = explore(inputLines)
	println(treasure)

	val glory = venture(inputLines)
	println(glory)
}
