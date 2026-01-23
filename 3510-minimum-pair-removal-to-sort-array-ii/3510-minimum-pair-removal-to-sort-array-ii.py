class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        arr = [int(x) for x in nums]
        removed = [False] * n
        heap = []
        asc = 0
        for i in range(1, n):
            heapq.heappush(heap, (arr[i - 1] + arr[i], i - 1))
            if arr[i] >= arr[i - 1]:
                asc += 1
        if asc == n - 1:
            return 0

        rem = n
        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 for i in range(n)]

        while rem > 1:
            if not heap:
                break
            sumv, left = heapq.heappop(heap)
            right = nxt[left]
            if right >= n or removed[left] or removed[right] or arr[left] + arr[right] != sumv:
                continue

            pre = prev[left]
            after = nxt[right]

            if arr[left] <= arr[right]:
                asc -= 1
            if pre != -1 and arr[pre] <= arr[left]:
                asc -= 1
            if after != n and arr[right] <= arr[after]:
                asc -= 1

            arr[left] += arr[right]
            removed[right] = True
            rem -= 1

            if pre != -1:
                heapq.heappush(heap, (arr[pre] + arr[left], pre))
                if arr[pre] <= arr[left]:
                    asc += 1
            else:
                prev[left] = -1

            if after != n:
                prev[after] = left
                nxt[left] = after
                heapq.heappush(heap, (arr[left] + arr[after], left))
                if arr[left] <= arr[after]:
                    asc += 1
            else:
                nxt[left] = n

            if asc == rem - 1:
                return n - rem

        return n
