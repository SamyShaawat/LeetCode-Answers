class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        # Start with "1" for n=1
        prev = "1"
        
        # Generate terms from 2 to n
        for i in range(2, n+1):
            curr = ""
            count = 1
            for j in range(len(prev)):
                # If current character is the same as the next one, increment count
                if j+1 < len(prev) and prev[j] == prev[j+1]:
                    count += 1
                else:
                    # Otherwise, add the count and the character to result
                    curr += str(count) + prev[j]
                    count = 1
            prev = curr
        
        return prev