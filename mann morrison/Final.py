import pandas as pd
import math
import xlsxwriter
from openpyxl import load_workbook
df = pd.read_excel(r"D:\R&D_2023\sample1.xlsx")
#print(df)
v=df['v(t)']
T=df['time(sec)']
T=list(df['time(sec)'])
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
    if (vm>253 or vm<207):
        print("Fault detected")
        print(v1)  # it is vm
        print(T[j + 1])
        print("this is time at which fault occured")
        break
    else:
        continue


    #v1.append(vm)
#d1={}
#d1 = dict(zip(vm,T))
#print(d1)
#d1 = dict(map(lambda m,n : (m,n) , vm,T))
#print(d1)
#print("vm")
print(v1) #it is vm
#print(T[j+1])
# print("this is time at which fault occured")
#vm.to_excel("sample1.xlsx",index=false)


