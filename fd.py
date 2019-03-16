import datetime
class fdc:
    def __init__(self,accno,amount,roi,bank):
        self.accno=accno
        self.amount=amount
        self.roi=roi
        self.bank=bank
        self.fdate=dict()

    def set_fd_date(self,day,month,year,fg):
        self.fdate[fg]=datetime.date(year,month,day)

    def get_fd_date(self,fg):
        day=str(self.fdate[fg].day)
        month=str(self.fdate[fg].month)
        year=str(self.fdate[fg].year)
        print(day+"/"+month+"/"+year)
