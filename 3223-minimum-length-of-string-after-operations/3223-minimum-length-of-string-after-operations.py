class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        print(freq)
        count = 0
        for value in freq.values():
            print(value)
            if value % 2 == 1:
                count += value - 1
            else:
                count += value - 2
        result = len(s) - count
        return result 
