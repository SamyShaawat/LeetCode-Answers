class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.freq = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        old = self.n2[index]
        self.freq[old] -= 1
        self.n2[index] += val
        self.freq[self.n2[index]] += 1
        

    def count(self, tot: int) -> int:
        res = 0
        for x in self.n1:
            res += self.freq[tot - x]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)