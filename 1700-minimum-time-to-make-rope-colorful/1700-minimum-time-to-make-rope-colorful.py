class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time, curr_max_time = 0, 0

        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                curr_max_time = 0
            total_time += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])

        return total_time
