class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        return ["." * n] + ["#" * (n - 1) + "."] * (m - 1)
