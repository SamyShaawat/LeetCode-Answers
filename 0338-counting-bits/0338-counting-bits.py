class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a list of size (n+1) with all zeros
        # arr[i] will store the number of 1's in the binary representation of i
        arr = [0] * (n + 1)

        # Loop through all numbers from 0 to n
        for i in range(len(arr)):
            # Convert the number i to its binary representation as a string (e.g., '101')
            # Count how many '1's are in that string and store it in arr[i]
            arr[i] = bin(i)[2:].count('1')

        # Return the filled array containing the bit counts
        return arr
