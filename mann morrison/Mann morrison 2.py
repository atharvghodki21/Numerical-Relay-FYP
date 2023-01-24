import pandas as pd
import math
import xlsxwriter
from openpyxl import load_workbook
df = pd.read_excel(r"D:\R&D_2023\sample_data.xlsx")
#print(df)
v=df['V']
T=[0, 0.00002, 0.00004, 0.00006]
n=len(v)
deltaT=0.00002
v1=[]
v_dash=[]
v2=[]
a=[] #vdash/w
b=[] #(vdash/w)^2
c=[] #v^2+(vdash/w)^2
d=[] #v/(vdash/w)
w=(math.pi)*100
#for i in range(1,n-1):
    #vdash=((v[i+1]-v[i-1])/(0.00004))
    #v_dash.append(vdash)
#print(v_dash)
for j in range(1,n-1):
    vdash = ((v[j + 1] - v[j - 1]) / (0.00004))
    v_dash.append(vdash)
    vm=math.sqrt((v[j]**2)+((v[j+1]-v[j-1])/(w*0.00004))**2)
    v1.append(vm)
    vsquare=math.pow(v[j],2)
    v2.append(vsquare)
    A=(v[j+1]-v[j-1])/0.01256
    a.append(A)
    B=A**2
    b.append(B)
    C=math.pow(v[j],2)+B
    c.append(C)
    D=v[j]/A
    d.append(D)
print("vdash")
print(v_dash)
print("vm")
print(v1) #it is vm
print("v^2")
print(v2) #v^2
print("vdash/w")
print(a) #vdash/w
print("(vdash/w)^2")
print(b) #(vdash/w)^2
print("v^2+(vdash/w)^2")
print(c) #v^2+(vdash/w)^2
print("v/(vdash/w)")
print(d) #v/(vdash/w)
workbook=xlsxwriter.Workbook('output_vm.xlsx')
worksheet=workbook.add_worksheet()
worksheet.write('B1', 'vm')
row = 2
column = 1
for k in v1:
    worksheet.write(row,column,k)
    row+=1
workbook.close()

