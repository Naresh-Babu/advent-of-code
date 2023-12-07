# com.workingnaresh.adventofcode

import io 

def fetch_input():
	input_string = io.open("./input.txt", "r").read()
	input_lines = input_string.split("\n")

	card_value = [list(string.strip().split(" ")) for string in input_lines]

	for i in range(len(card_value)):
		card_value[i][1] = int(card_value[i][1])
	
	return card_value




def get_type(hand):
	unique_cards = set(hand)
	unique_card_count = len(unique_cards)
	if unique_card_count == 1:
		return 0
	if unique_card_count == 2:
		if hand.count(next(iter(unique_cards))) in [4,1]:
			return 1
		else:
			return 2
	if unique_card_count == 3:
		if 3 in [hand.count(card) for card in unique_cards]:
			return 3
		else:
			return 4
	if unique_card_count == 4:
		return 5
	return 6

def get_type_with_joker(hand):
	unique_cards = set(hand)
	unique_card_count = len(unique_cards)

	if "J" in hand:
		joker_count = hand.count("J")

		if unique_card_count in [1,2]:
			return 0
		if joker_count == 1 and unique_card_count == 3:
			if 3 in [hand.count(card) for card in unique_cards]:
				return 1
			return 2
		if unique_card_count == 3:
			return 1
		if unique_card_count == 4:
			return 3
		return 5

	return get_type(hand)

def calculate_total_winnings(card_value):
	card_strengths = "AKQJT98765432"
	strength_map = {}
	for strength, card in enumerate(card_strengths):
		strength_map[card] = strength

	# Strength based sorting 
	card_value.sort(key = lambda card_set: [strength_map[card] for card in card_set[0]], reverse = True)

	# Type based sorting
	card_value.sort(key = lambda card_set: get_type(card_set[0]), reverse = True)

	winnings = 0
	for index, value in enumerate(card_value):
		(hand, bid) = value
		winnings += (index+1) * bid

	return winnings


def calculate_second_winnings(card_value):
	card_strengths = "AKQT98765432J"
	strength_map = {}
	for strength, card in enumerate(card_strengths):
		strength_map[card] = strength

	# Strength based sorting 
	card_value.sort(key = lambda card_set: [strength_map[card] for card in card_set[0]], reverse = True)

	# Type based sorting
	card_value.sort(key = lambda card_set: get_type_with_joker(card_set[0]), reverse = True)

	winnings = 0
	for index, value in enumerate(card_value):
		(hand, bid) = value
		winnings += (index+1) * bid

	return winnings


card_values = fetch_input()
winnings = calculate_total_winnings(card_values)
print(winnings)
second_winnings = calculate_second_winnings(card_values)
print(second_winnings)






