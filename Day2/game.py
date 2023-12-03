class Game:
    def __init__(self, red, green, blue):
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)


    def __eq__(self, other):
        return (self.red, self.green, self.blue) == (other.red, other.green, other.blue)


    def __str__(self):
        return "Game(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ")"


    def is_possible(self):
        """ 
        Returns True if the game is possible, False otherwise.
        A game is possible if the sum of the number of red, green and blue cubes.
        """
        return self.red <= 12 and self.green <= 13 and self.blue <= 14
    