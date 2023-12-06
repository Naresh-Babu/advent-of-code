package com.workingnaresh.adventofcode

import java.io.File
import kotlin.math.pow

data class Rations(
	val time: List<Long>,
	val distance: List<Long>
	)

//Pre Process
fun prepareForVoyage(lines: List<String>): Rations {
	val numberRegex = """(\d+)""".toRegex()



	val time = lines[0].run(numberRegex::findAll).map(MatchResult::value).map(String::toLong).toList()
	val distance = lines[1].run(numberRegex::findAll).map(MatchResult::value).map(String::toLong).toList()


	return Rations(time, distance)
}

//Part 1
fun explore(lines: List<String>): String {

	val (time, distance) = prepareForVoyage(lines)

	var gains = 1;
	for(i in 0 until time.size) {
		val availableTime = time[i]
		val distanceToBeat = distance[i]
		var waysToBeat = 0

		for (usedTime in 0..availableTime) {
			val speed = usedTime
			val remainingTime = availableTime - usedTime
			val travelledDistance = speed * remainingTime
			if (travelledDistance > distanceToBeat) waysToBeat++
		}
		gains *= waysToBeat
	}

	return gains.toString()
}

//Part 2
fun venture(lines: List<String>): String {
	var gains = 0

	// Same as part 1 so not repeating in brute force
	// An optimised way is to use Binary search and find valid mountain as the distance would like this   0 1 1 2 3 7 4 2 1 0


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
