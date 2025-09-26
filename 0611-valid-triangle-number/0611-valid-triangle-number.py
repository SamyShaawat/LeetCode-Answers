class Solution:
    def triangleNumber(self, sides: list[int]) -> int:
        sides.sort()
        n = len(sides)
        totalTriangles = 0

        for longest in range(n - 1, 1, -1):
            left, right = 0, longest - 1
            while left < right:
                if sides[left] + sides[right] > sides[longest]:
                    totalTriangles += (right - left)
                    right -= 1
                else:
                    left += 1

        return totalTriangles