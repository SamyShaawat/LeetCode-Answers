class NumArray:
    # comment to test leet hub 
    def __init__(self, nums: List[int]):
        self.prefix = []
        sum_till_now = 0
        for n in nums:
            sum_till_now += n
            self.prefix.append(sum_till_now)

    def sumRange(self, left: int, right: int) -> int:
        rSum = self.prefix[right]
        if left > 0 :
            lSum = self.prefix[left - 1]
        else:
            lSum = 0
        return rSum - lSum




        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)