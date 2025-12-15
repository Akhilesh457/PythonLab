class Meters:
    def __init__(self, m=0):
        self.m = m

    def to_kilometres(self):
        print("Kilometres =", self.m / 1000)


class Kilometres:
    def __init__(self, km=0):
        self.km = km

    def to_meters(self):
        print("Meters =", self.km * 1000)


# Driver code
m = Meters(1500)
k = Kilometres(2.5)

m.to_kilometres()
k.to_meters()
