import sys
from card import Card
from func import get_winning_numbers, get_your_numbers


"""
Solution for Part 2:
"""
input_file = open(sys.argv[1], 'r')

# Build the card deck from the input file.
cards = []
for line in input_file:
    card = Card(get_winning_numbers(line), get_your_numbers(line))
    cards.append(card)

# Iterate through the base cards.
card_count = 0
for i in range(len(cards)): 
    card = cards[i]
    # The number of times we want to process the card is equal to how many original + copies we have.
    times_to_process = card.count
    for time in range(times_to_process):
        # The number of matching numbers is the number of subsequent cards we need to add to the deck.
        matching_numbers = card.num_matching()
        for j in range(i + 1, i + 1 + matching_numbers):
            # This prevents us from going beyond the end of the deck.
            if j >= len(cards):
                break
            cards[j].count +=1

for card in cards:
    card_count += card.count

print("number of cards: " + str(card_count))