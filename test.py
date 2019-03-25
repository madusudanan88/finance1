from fd import fdc
import datetime
f=fdc("C:\\Users\\Madusudanan\\Documents\\finance-data\\finance.xlsx")
print(f.fetch_fd_value_all())
'''f=fdc(10,100,7,"hdfc","C:\\Users\\Madusudanan\\Documents\\finance-data\\finance.xlsx")
f.set_fd_date(10,10,2012,"start")
f.set_fd_date(10,10,2013,"end")
print(f.get_fd_date("start"))
print(f.get_fd_date("end"))
f.save()
import pandas as pd
import numpy as np
from openpyxl import load_workbook

# Assign spreadsheet filename to `file`
file = 'C:\\Users\\Madusudanan\\Documents\\finance-data\\finance.xlsx'
wb = load_workbook(file)
ws = wb.worksheets[0]
for i in ws.values:
    print(i[0],102)
    print("break")
#data1 = [101, 12500,datetime.date(2017,1,1),datetime.date(2018,1,1),'hdfc']
#ws.append(data1)
#wb.save(file)
# Load spreadsheet
xl = pd.ExcelFile(file)
df = pd.read_excel(file, "FD")
print(df)
# Print the sheet names

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('FD')
writer = pd.ExcelWriter(file, engine='xlsxwriter',mode='a')
data = np.array([['Acc no', 'Amount','start date','end date','bank'],[100, 10000,datetime.date(2017,2,1),datetime.date(2018,2,1),'sbi']])
data1 = np.array([['Acc no', 'Amount','start date','end date','bank'],[101, 12500,datetime.date(2017,1,1),datetime.date(2018,1,1),'hdfc']])
df1=pd.DataFrame(data=data[1:, 0:],index=data[1:, 0],columns=data[0, :])
df2=pd.DataFrame(data=data1[1:, 0:],index=data1[1:, 0],columns=data1[0, :])
print(df1)
print(df2)
df1.append(df2).to_excel(writer,'FD')
#df2=pd.DataFrame([[101,12500,datetime.date(2017,2,1),datetime.date(2018,2,1),'sbi']])
#df3=df.append(df2,ignore_index=True,sort=False)
#print(df3)
#print(df3)
pd.DataFrame(data=df[1:, 1:],
                   index=df[1:, 0],
                   columns=df[0, 1:]).to_excel(writer, 'FD')
df1.to_excel(writer,'FD')
df2.to_excel(writer,'FD')'''
#writer.save()
#writer.write_cells()