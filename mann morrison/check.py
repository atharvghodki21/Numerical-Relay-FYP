import pandas as pd
import math
import xlsxwriter
import openpyxl
from openpyxl import load_workbook
df = pd.read_excel(r"D:\R&D_2023\sample1.xlsx")
#print(df)
v=df['v(t)']
#T=df['time(sec)']
n=len(v)
deltaT=0.00002
v1=[]
w=(math.pi)*100
#for i in range(1,n-1):
    #vdash=((v[i+1]-v[i-1])/(0.00004))
    #v_dash.append(vdash)
#print(v_dash)
for j in range(1,n-1):
    #vdash = ((v[j + 1] - v[j - 1]) / (0.00004))
    #v_dash.append(vdash)
    vm=math.sqrt((v[j]**2)+((v[j+1]-v[j-1])/(w*0.00004))**2)
    v1.append(vm)
    if (vm>253 and vm<207):
        print("Fault detected")
        break
    else:
        continue

#print("vm")
print(v1) #it is vm
'''path='sample_data.xlsx'
with pd.ExcelWriter(path) as writer:
    writer.book = openpyxl.load_workbook(path)
    df.to_excel(writer, sheet_name='Sheet1')'''
book = xlsxwriter.Book('sample_data.xlsx')
sheet = book.add_sheet()

# Rows and columns are zero indexed.
row = 0
column = 0

vm1 = []

# iterating through the content list
for item in content:
    # write operation perform
    sheet.write(row, column, item)

    # incrementing the value of row by one with each iterations.
    row += 1

book.close()


