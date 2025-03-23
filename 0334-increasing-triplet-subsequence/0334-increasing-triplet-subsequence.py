class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                # Update the smallest number seen so far
                first = num
            elif num <= second:
                # Update the second smallest number that is greater than 'first'
                second = num
            else:
                # We have found a number greater than both first and second
                return True
        return False     
        