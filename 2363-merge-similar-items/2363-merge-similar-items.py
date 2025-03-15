class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        total = Counter()
        for x,y in items1:
            total[x] +=y
        for x,y in items2:
            total[x] +=y
        return list(sorted(total.items()))

        