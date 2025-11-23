class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        Find the maximum sum of elements from the array that is divisible by 3.
        
        Strategy: 
        - Sum all numbers first
        - If sum % 3 == 0, we're done
        - If sum % 3 == 1, remove either:
          - smallest number with remainder 1, OR
          - two smallest numbers with remainder 2
        - If sum % 3 == 2, remove either:
          - smallest number with remainder 2, OR
          - two smallest numbers with remainder 1
        """
        
        # Track the two smallest numbers with remainder 1 when divided by 3
        smallest_remainder1 = float('inf')
        second_smallest_remainder1 = float('inf')
        
        # Track the two smallest numbers with remainder 2 when divided by 3
        smallest_remainder2 = float('inf')
        second_smallest_remainder2 = float('inf')
        
        # Calculate total sum of all elements
        total_sum = 0
        
        for num in nums:
            total_sum += num
            
            remainder = num % 3
            
            # If number has remainder 1, update the two smallest trackers
            if remainder == 1:
                if num < smallest_remainder1:
                    # New smallest found, push current smallest to second position
                    second_smallest_remainder1 = smallest_remainder1
                    smallest_remainder1 = num
                elif num < second_smallest_remainder1:
                    second_smallest_remainder1 = num
            
            # If number has remainder 2, update the two smallest trackers
            elif remainder == 2:
                if num < smallest_remainder2:
                    # New smallest found, push current smallest to second position
                    second_smallest_remainder2 = smallest_remainder2
                    smallest_remainder2 = num
                elif num < second_smallest_remainder2:
                    second_smallest_remainder2 = num
        
        # Check what remainder the total sum has
        sum_remainder = total_sum % 3
        
        if sum_remainder == 1:
            # To make sum divisible by 3, we need to remove numbers totaling remainder 1
            # Option 1: Remove one number with remainder 1
            # Option 2: Remove two numbers with remainder 2 (since 2+2 = 4 ≡ 1 mod 3)
            return max(
                0,  # Edge case: if all options make sum negative
                total_sum - smallest_remainder1,
                total_sum - smallest_remainder2 - second_smallest_remainder2
            )
        
        elif sum_remainder == 2:
            # To make sum divisible by 3, we need to remove numbers totaling remainder 2
            # Option 1: Remove one number with remainder 2
            # Option 2: Remove two numbers with remainder 1 (since 1+1 = 2 mod 3)
            return max(
                0,  # Edge case: if all options make sum negative
                total_sum - smallest_remainder2,
                total_sum - smallest_remainder1 - second_smallest_remainder1
            )
        
        # If sum is already divisible by 3, return it as is
        return total_sum