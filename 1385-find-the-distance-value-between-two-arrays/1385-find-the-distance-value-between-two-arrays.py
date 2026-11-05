class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        bad = bytearray(2001)
        for y in set(arr2):
            lo = y + 1000 - d
            hi = y + 1001 + d
            if lo < 0:
                lo = 0
            if hi > 2001:
                hi = 2001
            bad[lo:hi] = b"\x01" * (hi - lo)
        c = 0
        for x in arr1:
            if not bad[x + 1000]:
                c += 1
        return c
