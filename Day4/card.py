class Card:
    """
    A class representing a scratch card.
    The card has a list of winning numbers and a list of your numbers.
    """
    def __init__(self, winning_numbers, your_numbers):
        self.winning_numbers = winning_numbers
        self.your_numbers= your_numbers
        self.count = 1

    def __eq__(self, other):
        return (self.winning_numbers, self.your_numbers) == (other.winning_numbers, other.your_numbers)


    def __str__(self):
        return "Card(" + str(self.winning_numbers) + " | " + str(self.your_numbers) + ")"

    def points_worth(self):
        """ 
        Returns the number of points the card is worth, based on the number of winning numbers.
        Each winning number doubles the point worth. The first winning number is worth 1 point.

        Two winning numbers would be, 2 points, three winning numbers would be 4 points, etc.
        """
        worth = 0
        for number in self.your_numbers:
            if number in self.winning_numbers:
                if worth == 0:
                    worth = 1
                else: 
                    worth *= 2
        return worth
    
    def num_matching(self):
        """
        Returns the number of matching numbers between the winning numbers and your numbers.
        """
        num_matching = 0
        for number in self.your_numbers:
            if number in self.winning_numbers:
                num_matching += 1
        return num_matching