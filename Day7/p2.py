import sys
from hand2 import Hand

file = open(sys.argv[1], "r")
lines = file.readlines()

hands = []

for line in lines:
    hand = line.split()[0]
    bid = line.split()[1]
    hands.append(Hand(hand, int(bid)))

hands.sort()
winnings = []
for i in range(len(hands)):
    hands[i].set_final_rank(i+1)
    print(hands[i].cards.replace("J", "1") + " " + str(hands[i].final_rank) + " " + str(hands[i].bid) + " $" + str(hands[i].calculate_winnings()))
    winnings.append(hands[i].calculate_winnings())

print(str(sum(winnings)))
# 
# The answer to the problem is 248781813


