class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # If any number in the list is less than k, it's impossible to make all nums equal to k
        # because we are only allowed to decrease values, not increase.
        if any(x < k for x in nums):
            return -1
        print(set(x for x in nums if x>k))
        # The number of operations required is equal to the number of unique values > k,
        # because in each operation, we can reduce all instances of the current maximum
        # to the next smaller value.
        return len(set(x for x in nums if x>k))
        
        