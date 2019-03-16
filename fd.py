import datetime
class fd:
    def __init__(self,accno,amount,roi,bank):
        self.accno=accno
        self.amount=amount
        self.roi=roi
        self.bank=bank
        self.date=dict()

    def set_fd_date(self,day,month,year,fg):
        self.fdate[fg]=datetime.date(year,month,day)

    def get_fd_date(self,fg):
        day=self.fdate[fg].day
        month=self.fdate[fg].month
        year=self.fdate[fg].year
        print(day+"/"+month+"/"+year)
