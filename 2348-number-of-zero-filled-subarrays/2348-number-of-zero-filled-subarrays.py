class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0  # Total count of zero-filled subarrays
        zeroSeqLength = 0  # Length of the current sequence of zeros
        
        for num in nums:
            if num == 0:
                # Increment the zero sequence length
                zeroSeqLength += 1
                # Add the current sequence length to overall count
                count += zeroSeqLength
            else:
                # Reset the zero sequence length for a non-zero number
                zeroSeqLength = 0
        
        return count
        