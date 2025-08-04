
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        n = len(fruits)
        fruitCounts = defaultdict(int)
        window_start = 0
        max_length = 0

        for window_end in range(n):
            fruitCounts[fruits[window_end]] += 1

            while len(fruitCounts) > 2:
                fruitCounts[fruits[window_start]] -= 1
                if fruitCounts[fruits[window_start]] == 0:
                    del fruitCounts[fruits[window_start]]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length
