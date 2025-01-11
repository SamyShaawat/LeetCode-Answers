class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        freq = Counter(s)
        # print(freq)

        
        # Iterate through the frequency map and count how many characters have an odd frequency. 
        # This count determines the minimum number of palindromes needed.

        odd_count = 0
        for count in freq.values():
            if count %2 == 1:
                odd_count +=1 
        # print(odd_count)
        if odd_count <= k:
            return True
        else:
            return False