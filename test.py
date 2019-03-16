from fd import fdc
f=fdc(10,100,7,"hdfc")
f.set_fd_date(10,10,2012,"start")
f.set_fd_date(10,10,2013,"end")
print(f.get_fd_date("start"))
print(f.get_fd_date("end"))
