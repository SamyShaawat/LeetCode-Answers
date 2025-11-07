class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        prefix = [0]
        size = len(stations)
        for i in stations:
            prefix.append(prefix[-1] + i)
        for i in range(size):
            stations[i] = prefix[min(i+r+1, size)] - prefix[max(0, i-r)]

        def check(min_power):
            diff = [0] * size
            cur_diff = 0
            cnt_station = 0
            for i, power in enumerate(stations):
                cur_diff += diff[i]
                power_diff = min_power - power - cur_diff

                if power_diff > 0: 
                    cnt_station += power_diff
                    if cnt_station > k:
                        return False
                    cur_diff += power_diff
                    if i + 2 * r + 1 < size: diff[i + 2 * r + 1] -= power_diff

            return True
        left = min(stations)
        right = left + k
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid): left = mid + 1
            else: right = mid - 1

        return right