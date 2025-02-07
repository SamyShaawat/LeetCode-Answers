class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColor = {} # track color of each ball 
        colorCount = {} # count occurance of colors
        result = []
        for ball, color in queries:
            if ball in ballToColor:
                colorCount[ballToColor[ball]] -= 1

                if colorCount[ballToColor[ball]] == 0:
                    del colorCount[ballToColor[ball]]
                ballToColor[ball] = color
                colorCount[color] = colorCount.get(color, 0) + 1

            else:
                colorCount[color] = colorCount.get(color, 0) + 1
                ballToColor[ball] = color
            result.append(len(colorCount.keys()))

        return result