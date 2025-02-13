class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        number_of_operation = 0
        heapq.heapify(nums)
        while nums[0] < k:
            heapq.heappop(nums)
            number_of_operation +=1

        return number_of_operation

        