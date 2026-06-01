class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet=defaultdict(int)
        self.letters=set()
        for i in range(26):
            ch=chr(65+i)
            self.letters.add(ch)
    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell]=value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell]=0

    def getValue(self, formula: str) -> int:
        formula=formula[1:]
        plus=formula.find("+")
        first_num=formula[:plus]
        sec_num=formula[plus+1:]
        if(first_num[0] in self.letters):
            first_num=self.sheet[first_num]
        if(sec_num[0] in self.letters):
            sec_num=self.sheet[sec_num]
        return int(first_num)+int(sec_num)

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)