class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        size = 2 ** n

        nu = [0] * size

        for num in nums:
            val = int(num, 2)
            nu[val] += 1

        for i in range(size):
            if nu[i] == 0:
                ans = bin(i)[2:]
                return "0" * (n - len(ans)) + ans

        return "0" * n