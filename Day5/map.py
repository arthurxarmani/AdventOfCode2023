class Map: 
    """
    A map has its line interpretation and its list of ranges.
    """

    def __init__(self, ranges):
        self.ranges = ranges
    
    def __repr__(self):
        return str(self.ranges)
    
    def __eq__(self, other):     
        return self.ranges == other.ranges