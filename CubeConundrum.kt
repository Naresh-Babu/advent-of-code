package com.workingnaresh.adventofcode

import java.io.File

data class Rations(
	val gameId: Int,
	val red: Int,
	val green: Int,
	val blue: Int
	)

fun prepareForVoyage(line: String): Rations {
	val gameIdRegex = """Game (\d+):""".toRegex()
	val redRegex = """ (\d+) red""".toRegex()
	val blueRegex = """ (\d+) blue""".toRegex()
	val greenRegex = """ (\d+) green""".toRegex()

	fun getCount(regex:Regex): Int {
		return regex
			.findAll(line)
			.map(MatchResult::groupValues)
			.map { it.get(1) }
			.map(String::toInt)
			.maxOrNull()
			?: 0
	}

	val gameId = gameIdRegex.find(line)!!.groupValues.get(1).toInt()
	val red = getCount(redRegex)
	val green = getCount(greenRegex)
	val blue = getCount(blueRegex)

	return Rations(gameId, red, green, blue)
}

fun explore(lines: List<String>): String {
	var res = 0;
	lines.map(::prepareForVoyage).forEach {
		it.run {
			//Daily code

			if (red <= 12 && green <= 13 && blue <= 14) {
				res += gameId
			}

			//End of daily code
		}
	}

	return res.toString()
}

fun venture(lines: List<String>): String {
	var res = 0;
	lines.map(::prepareForVoyage).forEach {
		it.run {
			//Daily code

			res += red * green * blue

			//End of daily code
		}
	}

	return res.toString()
}


fun main() {
	val inputFileString = File("./input.txt").readText()
	val inputLines = inputFileString.split("\n").map(String::trim)

	val treasure = explore(inputLines)
	println(treasure)

	val glory = venture(inputLines)
	println(glory)
}
