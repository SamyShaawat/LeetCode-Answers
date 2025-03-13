class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        left, right = 0, len(queries)

        # Zero array isn't formed after all queries are processed
        if not self.can_form_zero_array(nums, queries, right):
            return -1

        # Binary Search
        while left <= right:
            middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        # Return earliest query that zero array can be formed
        return left

    def can_form_zero_array(
        self, nums: List[int], queries: List[List[int]], k: int
    ) -> bool:
        n = len(nums)
        total_sum = 0
        difference_array = [0] * (n + 1)

        # Process query
        for query_index in range(k):
            start, end, val = queries[query_index]

            # Process start and end of range
            difference_array[start] += val
            difference_array[end + 1] -= val

        # Check if zero array can be formed
        for num_index in range(n):
            total_sum += difference_array[num_index]
            if total_sum < nums[num_index]:
                return False
        return True