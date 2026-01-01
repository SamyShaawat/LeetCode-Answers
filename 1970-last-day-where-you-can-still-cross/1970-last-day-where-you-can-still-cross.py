class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        dsu = DSU(row * col + 2)
        grid = [[0] * col for _ in range(row)]
        dirs = ((0,1),(0,-1),(1,0),(-1,0))

        for i in range(len(cells) - 1, -1, -1):
            r = cells[i][0] - 1
            c = cells[i][1] - 1
            grid[r][c] = 1

            id1 = r * col + c + 1
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    id2 = nr * col + nc + 1
                    dsu.union(id1, id2)

            if r == 0:
                dsu.union(0, id1)
            if r == row - 1:
                dsu.union(row * col + 1, id1)
            if dsu.find(0) == dsu.find(row * col + 1):
                return i
        return -1

class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.size[rx] > self.size[ry]:
            rx, ry = ry, rx
        self.root[rx] = ry
        self.size[ry] += self.size[rx]
