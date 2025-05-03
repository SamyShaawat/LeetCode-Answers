class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for i in [tops[0],bottoms[0]]:

            if all(i in d for d in zip(tops, bottoms)):

                mod = max(tops.count(i), bottoms.count(i))

                return len(tops) - mod
        return -1