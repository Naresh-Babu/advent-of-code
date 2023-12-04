package com.workingnaresh.adventofcode

import java.io.File
import kotlin.math.pow

data class Rations(
	val cardId: Int,
	val winningNumbers: Set<Int>,
	val holdingNumbers: Set<Int>
)

fun prepareForVoyage(line: String): Rations {
	val numberRegex = """(\d+)""".toRegex()

	val (cardSection, numbersSection) =  line.split(":").run { get(0) to get(1) }
	val (winningNumbersSection, holdingNumbersSection) = numbersSection.split("|").run { get(0) to get(1) }

	val cardId = cardSection.run(numberRegex::find)!!.value.toInt()
	val winningNumbers = winningNumbersSection.run(numberRegex::findAll).flatMap(MatchResult::groupValues).map(String::toInt).toSet()
	val holdingNumbers = holdingNumbersSection.run(numberRegex::findAll).flatMap(MatchResult::groupValues).map(String::toInt).toSet()

	return Rations(cardId, winningNumbers, holdingNumbers)
}

fun explore(lines: List<String>): String {
	var gains = 0;
	lines.map(::prepareForVoyage).forEach {
		it.run {
			//Daily code

			 val winCount = holdingNumbers.intersect(winningNumbers).size
			 gains += if (winCount == 0) 0 else 2.0.pow(winCount - 1).toInt()

			//End of daily code
		}
	}

	return gains.toString()
}

fun venture(lines: List<String>): String {
	var gains = 0
	val cardInstances: Array<Int> = Array(lines.size) { 1 }

	lines.map(::prepareForVoyage).forEachIndexed { i,it ->
		it.run {
			//Daily code

			val winCount = holdingNumbers.intersect(winningNumbers).size

			for (j in i+1 .. i+winCount) {
				cardInstances[j] += cardInstances[i]
			}
			gains += cardInstances[i]

			//End of daily code

		}
	}

	return gains.toString()
}


fun main() {
	val inputFileString = File("./input.txt").readText()
	val inputLines = inputFileString.split("\n").map(String::trim)

	val treasure = explore(inputLines)
	println(treasure)

	val glory = venture(inputLines)
	println(glory)
}
