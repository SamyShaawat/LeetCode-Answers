class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):

            one = nums[i]
            two = nums[i+1]
            three = nums[i+2]

            if  ( ( three - one ) <= k ):
                res.append( [ one, two, three ] )
            else:
                return []

        return res