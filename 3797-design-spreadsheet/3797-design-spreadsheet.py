class Spreadsheet:
    def __init__(self, rows: int):
        self.dict = defaultdict(int)
    def setCell(self, cell: str, value: int) -> None:
        self.dict[cell] = value
    def resetCell(self, cell: str) -> None:
        self.dict[cell] = 0
    def getValue(self, formula: str) -> int:
        ops = formula.split('=')[1].split('+')
        res = 0
        for op in ops:
            if op in self.dict:
                res += self.dict[op]
            elif op.isdigit():
                res += int(op)
        return res
