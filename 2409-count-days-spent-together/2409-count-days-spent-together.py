class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        c = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
        s = max(arriveAlice, arriveBob)
        e = min(leaveAlice, leaveBob)
        if s > e:
            return 0
        return c[int(e[:2]) - 1] + int(e[3:]) - c[int(s[:2]) - 1] - int(s[3:]) + 1
