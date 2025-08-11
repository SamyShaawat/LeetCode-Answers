class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            return ''.join(sorted(str(x)))

        target = count_digits(n)
        
        for i in range(31):
            if count_digits(1 << i) == target:
                return True
        return False