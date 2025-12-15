class Distance:
    def __init__(self, meters=0):
        self.meters = meters

    def __isub__(self, other):
        self.meters -= other.meters
        return self

    def display(self):
        print("Distance:", self.meters, "meters")


# Driver code
d1 = Distance(100)
d2 = Distance(40)

d1 -= d2
d1.display()
