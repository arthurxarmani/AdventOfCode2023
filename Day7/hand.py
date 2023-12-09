class Hand:
    def __init__(self, cards, bid: int):
        self.cards = cards
        self.keys = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2 }
        self.rank = self.determine_rank()
        self.bid = bid
        self.final_rank = None
    
    def determine_rank(self):
        """
        Returns the type of hand. 
        Rank goes from 7 to 1, where 7 is the highest and 1 is the lowest.
        """
        print("evaluating " + str(self.cards))
        if(len(set(self.cards))) == 5:
            print("high card")
            # High card
            # ABCDE [ABCDE]
            return 1
        elif(len(set(self.cards))) == 4:
            print("one pair")
            # One pair
            # AABCD [ABCD]
            return 2
        elif(len(set(self.cards))) == 3:
            for char in self.cards:
                if self.cards.count(char) == 2:
                    print("two pair")
                    # Two pairs
                    # AABBC [ABC]
                    # AABCC [ABC]
                    return 3
                if self.cards.count(char) == 3:
                    print("three of a kind")
                    # Three of a kind
                    # AAABC [ABC]
                    # AABAC [ABC]
                    return 4
        elif(len(set(self.cards))) == 2:
            for char in self.cards:
                if self.cards.count(char) == 4:
                    print("four of a kind")
                    # Four of a kind
                    return 6
                if self.cards.count(char) == 3:
                    print("full house")
                    # Full house
                    return 5
        elif(len(set(self.cards))) == 1:
            print("five of a kind")
            # Five of a kind
            # AAAAA [a]
            return 7 
        


    def __lt__(self, other):
        if self.rank == other.rank:
            for i in range(5):
                if self.keys[self.cards[i]] < self.keys[other.cards[i]]:
                    return True
                elif self.keys[self.cards[i]] > self.keys[other.cards[i]]:
                    return False
            return False
        else:
            return self.rank < other.rank
    
    def __gt__(self, other):
        if self.rank == other.rank:
            for i in range(5):
                if self.keys[self.cards[i]] > self.keys[other.cards[i]]:
                    return True
                elif self.keys[self.cards[i]] < self.keys[other.cards[i]]:
                    return False
            return False
        else:
            return self.rank > other.rank
    
    def __eq__(self, other) -> bool:
        return self.cards == other.cards
    
    def set_final_rank(self, rank: int):
        self.final_rank = rank

    def calculate_winnings(self):
        return self.bid * self.final_rank