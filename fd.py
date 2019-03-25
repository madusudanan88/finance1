import datetime
from dateutil.relativedelta import relativedelta
from openpyxl import load_workbook
class fdc:
    def __init__(self,file):
        self.fdate=dict()
        self.file='C:\\Users\\Madusudanan\\Documents\\finance-data\\finance.xlsx'

    def set_fd_date(self,day,month,year,fg):
        self.fdate[fg]=datetime.date(year,month,day)

    def get_fd_date(self,fg):
        day=str(self.fdate[fg].day)
        month=str(self.fdate[fg].month)
        year=str(self.fdate[fg].year)
        print(day+"/"+month+"/"+year)

    def set_value(self,accno,amount,roi,bank):
        self.accno = accno
        self.amount = amount
        self.roi = roi
        self.bank=bank


    def save(self):
        wb = load_workbook(self.file)
        ws = wb.worksheets[0]
        data1 = [self.accno,self.amount,self.roi,self.fdate["start"],self.fdate["end"],self.bank]
        ws.append(data1)
        wb.save(self.file)

    def fetch_fd_value(self,accno):
        wb = load_workbook(self.file)
        ws = wb.worksheets[0]
        for i in ws.rows:
            if(i[0].value==accno):
                amount=i[1].value
                roi=i[2].value
                sdate=i[3].value
                edate=i[4].value
                break
        cdate=datetime.datetime.now()
        if(cdate>edate):
            rdelta = relativedelta(edate, sdate)
            interest = (int(rdelta.years) * roi * amount) / 100
            interest = interest + ((rdelta.years * roi * amount) / 1200)
        else:
            rdelta = relativedelta(cdate, sdate)
            interest=(int(rdelta.years)*roi*amount)/100
            interest=interest+((rdelta.years*roi*amount)/1200)
        return(int(interest)+amount)



        
