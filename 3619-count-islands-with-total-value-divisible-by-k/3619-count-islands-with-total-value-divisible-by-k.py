class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid[0]) + 1
        g = [0] * n
        for r in grid:
            g += r
            g.append(0)
        g += [0] * n
        ans = 0
        for i, s in enumerate(g):
            if s:
                g[i] = 0
                st = [i]
                pop = st.pop
                push = st.append
                while st:
                    j = pop()
                    t = j - 1
                    v = g[t]
                    if v:
                        s += v
                        g[t] = 0
                        push(t)
                    t = j + 1
                    v = g[t]
                    if v:
                        s += v
                        g[t] = 0
                        push(t)
                    t = j - n
                    v = g[t]
                    if v:
                        s += v
                        g[t] = 0
                        push(t)
                    t = j + n
                    v = g[t]
                    if v:
                        s += v
                        g[t] = 0
                        push(t)
                if s % k == 0:
                    ans += 1
        return ans
