class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}
        self.cols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for col in self.cols:
            self.sheet[col] = {}

        

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        cel = cell[1:]
        self.sheet[col][cel] = value
        

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        cel = cell[1:]
        if cel in self.sheet[col]:
            del self.sheet[col][cel]
        

    def getValue(self, formula: str) -> int:
        ops = formula.replace("=","").split("+")
        operands = []
        for op in ops:
            if op[0] in self.cols:
                col = op[0]
                cel = op[1:]
                operands.append(self.sheet[col][cel] if cel in self.sheet[col] else "0")
            else:
                operands.append(op)


        return int(operands[0]) + int(operands[1])

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)