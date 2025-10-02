class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottleDrunk = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            numExchange += 1
            bottleDrunk += 1
            emptyBottles += 1
        return bottleDrunk