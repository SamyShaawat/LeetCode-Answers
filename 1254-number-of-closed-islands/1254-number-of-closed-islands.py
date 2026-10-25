class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0
        m1 = m - 1
        n1 = n - 1
        res = 0
        for i in range(m):
            row = grid[i]
            edge = i == 0 or i == m1
            for j in range(n):
                if row[j] == 0:
                    row[j] = 1
                    ok = 1
                    if edge or j == 0 or j == n1:
                        ok = 0
                    st = [(i, j)]
                    while st:
                        x, y = st.pop()
                        if x > 0 and grid[x - 1][y] == 0:
                            grid[x - 1][y] = 1
                            if x == 1:
                                ok = 0
                            st.append((x - 1, y))
                        if x < m1 and grid[x + 1][y] == 0:
                            grid[x + 1][y] = 1
                            if x + 1 == m1:
                                ok = 0
                            st.append((x + 1, y))
                        r = grid[x]
                        if y > 0 and r[y - 1] == 0:
                            r[y - 1] = 1
                            if y == 1:
                                ok = 0
                            st.append((x, y - 1))
                        if y < n1 and r[y + 1] == 0:
                            r[y + 1] = 1
                            if y + 1 == n1:
                                ok = 0
                            st.append((x, y + 1))
                    res += ok
        return res
