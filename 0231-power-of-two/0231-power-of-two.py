class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            num = bin(n)[2::]
        else:
            num = bin(n)[3::]
        hashmap = Counter(num)
        for key, value in hashmap.items():
            if n > 0:
                if key == '1':
                    if value == 1:
                        return True
        return False