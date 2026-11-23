class ProductOfNumbers:

    def __init__(self):
        self.p = [1]
        self.n = 1

    def add(self, num: int) -> None:
        if num:
            self.p.append(self.p[-1] * num)
            self.n += 1
        else:
            self.p = [1]
            self.n = 1

    def getProduct(self, k: int) -> int:
        if k >= self.n:
            return 0
        p = self.p
        return p[-1] // p[~k]
