class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = defaultdict(int)
        for i in range(len(names)):
            hashmap[names[i]] = heights[i]
        print(list(dict(hashmap)))
        