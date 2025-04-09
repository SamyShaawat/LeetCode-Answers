class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        # Initialize an array to count how many times each bit position (0-30) has a 1
        bits = [0] * 31  # We assume 31-bit integers (enough for constraints)

        # Count how many numbers have each bit set
        for num in nums:
            i = 0
            while num:
                # If the least significant bit is 1, increment the count for that bit position
                bits[i] += num & 1
                # Right shift the number to check the next bit
                num = num >> 1
                i += 1

        # Now, we compute the result number based on the bit counts
        res = 0
        multiplier = 1  # This is 2^i, starting with 2^0 = 1

        for i in range(31):
            # If the i-th bit is set in at least k numbers, include this bit in the result
            if bits[i] >= k:
                res += multiplier  # Set the i-th bit in the result
            multiplier *= 2  # Move to the next bit position (2^i → 2^(i+1))

        return res
