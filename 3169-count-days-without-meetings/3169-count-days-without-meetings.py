class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)
        res = days
        current = [meetings[0]]
        print(current)
        for meeting in meetings[1:]:
            print(current[-1][1])
            if meeting[0] <= current[-1][1]:
                current[-1][1] = max(meeting[1], current[-1][1])
            else:
                current.append(meeting)
        for c in current:
            print(c)
            res -= (c[1] - c[0] + 1)
        return res