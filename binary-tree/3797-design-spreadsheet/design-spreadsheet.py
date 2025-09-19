class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}
        # start = 65
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
        op1, op2 = formula.replace("=","").split("+")
        if op1[0] in self.cols:
            col1 = op1[0]
            cel1 = op1[1:]
            operand1 = self.sheet[col1][cel1] if cel1 in self.sheet[col1] else "0"
        else:
            operand1 = op1
        if op2[0] in self.cols:
            col2 = op2[0]
            cel2 = op2[1:]
            operand2 = self.sheet[col2][cel2] if cel2 in self.sheet[col2] else "0"
        else:
            operand2 = op2

        return int(operand1) + int(operand2)

        # op2
        return 10
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)