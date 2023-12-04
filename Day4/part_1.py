import sys
from card import Card
from func import get_winning_numbers, get_your_numbers


"""
Solution for Part 1:
"""
input_file = open(sys.argv[1], 'r')
cards = []
for line in input_file:
    card = Card(get_winning_numbers(line), get_your_numbers(line))
    cards.append(card)

worth = 0
for card in cards:
    worth += card.points_worth()

print("sum: " + str(worth))