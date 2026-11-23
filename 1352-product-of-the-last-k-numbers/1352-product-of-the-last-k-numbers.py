class ProductOfNumbers:
    __slots__ = ('p',)

    def __init__(self):
        self.p = [1]

    def add(self, num: int) -> None:
        p = self.p
        if num:
            p.append(p[-1] * num)
        else:
            self.p = [1]

    def getProduct(self, k: int) -> int:
        p = self.p
        return p[-1] // p[~k] if k < len(p) else 0
