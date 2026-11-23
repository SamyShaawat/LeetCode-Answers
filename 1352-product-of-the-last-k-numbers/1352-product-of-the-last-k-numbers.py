class ProductOfNumbers:

    def __init__(self):
        self.p = [1]

    def add(self, num: int) -> None:
        if num:
            p = self.p
            p.append(p[-1] * num)
        else:
            self.p = [1]

    def getProduct(self, k: int) -> int:
        p = self.p
        n = len(p)
        return 0 if k >= n else p[-1] // p[n - 1 - k]
