class Solution:
    def calc(self, part1: int, part2: int, part3: int) -> int:
        return max(part1, part2, part3) - min(part1, part2, part3)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        e = [[] for _ in range(n)]
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)

        total = 0
        for x in nums:
            total ^= x

        res = float("inf")

        def dfs2(x: int, f: int, oth: int, anc: int) -> int:
            son = nums[x]
            for y in e[x]:
                if y == f:
                    continue
                son ^= dfs2(y, x, oth, anc)
            if f == anc:
                return son
            nonlocal res
            res = min(res, self.calc(oth, son, total ^ oth ^ son))
            return son

        def dfs(x: int, f: int) -> int:
            son = nums[x]
            for y in e[x]:
                if y == f:
                    continue
                son ^= dfs(y, x)
            for y in e[x]:
                if y == f:
                    dfs2(y, x, son, x)
            return son

        dfs(0, -1)
        return res