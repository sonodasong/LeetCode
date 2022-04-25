class UndergroundSystem:

    def __init__(self):
        self.p = {}
        self.r = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        p = self.p
        if id in p: assert False
        p[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        p = self.p; r = self.r
        if id not in p: assert False
        s0, t0 = p[id]
        del p[id]
        if (s0, stationName) in r:
            r = r[(s0, stationName)]
            r[0] += t - t0; r[1] += 1
        else:
            r[(s0, stationName)] = [t - t0, 1]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        r = self.r[(startStation, endStation)]
        return r[0] / r[1]


if __name__ == '__main__':
    undergroundSystem = UndergroundSystem()
    print(undergroundSystem.checkIn(45, "Leyton", 3))
    print(undergroundSystem.checkIn(32, "Paradise", 8))
    print(undergroundSystem.checkIn(27, "Leyton", 10))
    print(undergroundSystem.checkOut(45, "Waterloo", 15))  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
    print(undergroundSystem.checkOut(27, "Waterloo", 20))  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
    print(undergroundSystem.checkOut(32, "Cambridge", 22)) # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
    print(undergroundSystem.getAverageTime("Paradise", "Cambridge")) # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))    # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
    print(undergroundSystem.checkIn(10, "Leyton", 24))
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))    # return 11.00000
    print(undergroundSystem.checkOut(10, "Waterloo", 38))  # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))    # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
