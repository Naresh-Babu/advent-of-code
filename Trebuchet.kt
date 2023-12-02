package com.workingnaresh.adventofcode

import java.io.File

fun main() {
	val day = "1"
	val inputFile = File("./${day}_input.txt").readText()
	val input = inputFile.split("\n").map(String::trim)

	val outputFile = File("./${day}_output.txt")
	outputFile.createNewFile()

	// Days code

	var res = 0
	val set = listOf("dummywsvi", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
	input.forEach { word ->
		var first = 0

		for (i in 0 until word.length) {
			if (word[i].isDigit()) {
				first = word[i].toString().toInt()
				break
			}
			for (j in 0 until set.size) {
				var isMatch = true
				if (i + set[j].length > word.length) {
					continue
				}
				for (k in 0 until set[j].length) {
					if (set[j][k] != word[i+k]) {
						isMatch = false
						break
					}

				}

				if (isMatch) {
					first = j
					break
				}

			}

			if (first != 0) {
				break
			}

		}

		var last = 0
		val reverse = word.reversed()

		for (i in 0 until reverse.length) {
			if (reverse[i].isDigit()) {
				last = reverse[i].toString().toInt()
				break
			}
			for (j in 0 until set.size) {
				var isMatch = true
				if (i + set[j].length > reverse.length) {
					continue
				}
				for (k in 0 until set[j].length) {
					if ((set[j].reversed())[k] != reverse[i+k]) {
						isMatch = false
						break
					}
				}

				if (isMatch) {
					last = j
					break
				}

			}

			if (last != 0) {
				break
			}
		}


		res += first * 10 + last

	}
	println(res)
	outputFile.appendText(res.toString())
	outputFile.appendText("\n")

}
