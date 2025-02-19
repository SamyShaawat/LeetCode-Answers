class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3 * (2 ** (n-1))
        res = []
        choices = "abc"
        left, right = 1, total_happy
        for i in range(n):
             cur = left
             partition_size = (right - left + 1) // len(choices)

             for c in choices:
                if k in range(cur, cur + partition_size):
                    res.append(c)
                    left = cur 
                    right = cur + partition_size - 1
                    choices = "abc".replace(c,"") 
                    break

                cur += partition_size

        return "".join(res)
        