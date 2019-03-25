import datetime
from openpyxl import load_workbook
class fdc:
    def __init__(self,accno,amount,roi,bank,file):
        self.accno=accno
        self.amount=amount
        self.roi=roi
        self.bank=bank
        self.fdate=dict()
        self.file='C:\\Users\\Madusudanan\\Documents\\finance-data\\finance.xlsx'

    def set_fd_date(self,day,month,year,fg):
        self.fdate[fg]=datetime.date(year,month,day)

    def get_fd_date(self,fg):
        day=str(self.fdate[fg].day)
        month=str(self.fdate[fg].month)
        year=str(self.fdate[fg].year)
        print(day+"/"+month+"/"+year)

    def save(self):
        wb = load_workbook(self.file)
        ws = wb.worksheets[0]
        data1 = [self.accno,self.amount,self.fdate["start"],self.fdate["end"],self.bank]
        ws.append(data1)
        wb.save(self.file)

    def fetch_fd(self):
        
