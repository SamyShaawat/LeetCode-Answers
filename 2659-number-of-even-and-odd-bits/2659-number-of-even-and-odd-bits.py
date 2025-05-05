class Solution:
    def evenOddBit(self, n: int) -> List[int]:                 
        evens, odds = int('0101010101',2), int('1010101010',2)

        return [(evens&n).bit_count(),(odds&n).bit_count()]