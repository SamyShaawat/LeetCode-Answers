class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        m1 = m - 1
        n1 = n - 1
        res = 0
        for i in range(1, m1):
            row = grid[i]
            for j in range(1, n1):
                if row[j] == 0:
                    row[j] = 1
                    st = [(i, j)]
                    ok = 1
                    while st:
                        x, y = st.pop()
                        if x == 0 or y == 0 or x == m1 or y == n1:
                            ok = 0
                            continue
                        for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                            if grid[a][b] == 0:
                                grid[a][b] = 1
                                st.append((a, b))
                    res += ok
        return res
