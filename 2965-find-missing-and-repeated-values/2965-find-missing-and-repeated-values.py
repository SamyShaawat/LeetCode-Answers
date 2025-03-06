class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        original = list(range(1, (n**2)+1))
        flatten = sorted([n for sublist in grid  for n in sublist])
        hashmap = Counter(flatten)
        repeated = [key for key, value in hashmap.items() if value > 1 ]
        missing = [n  for n in original if n not in flatten]
        res = repeated + missing
        return res
        print(res)
        print(repeated)
        print(missing)

        print(original)
        print(flatten)

        