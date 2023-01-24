from pandas import *
import xlsxwriter
import math

df= read_csv("data.csv")
s = df['Sampleno.'].tolist()

df1=read_csv("sampleDATA.csv")
v=df['v'].to_list()

df2=read_csv("sampleDATA.csv")
t=df['t'].to_list()

df3= read_csv("sampleDATA.csv")                                
z = df['i'].tolist()

n=len(v)
w=314
v_dash=[]
vsquare=[]
v_dash_w=[]
a=[] #v_dash^2*w^2
vm=[]
b=[]
c=[]
phi_v=[]
#for v_dash and voltage parameters
for i in range(0,n-2):
    vd= (v[i+1]-v[i-1])/(2*0.00004)
    v_dash.append(vd)
for i in range(n):
    vsquare.append(v[i]*v[i])    #v**2

for i in range(0,n-2):
    v_dash_w.append(v_dash[i]/w)
    a.append((v_dash_w[i])*(v_dash_w[i]))

for i in range(0,n-2):
    v1=math.sqrt((vsquare[i])+(a[i])/2)
    vm.append(v1)
    b.append(math.atan(v[i]/v_dash_w[i]))
    c.append(314*t[i])
    pv=b[i]-c[i]
    phi_v.append(pv)

#current parameters
m=len(z)
i_dash=[]
isquare=[]
i_dash_w=[]  #i_dash/w
d=[] #i_dash**2/w**2
im=[]
e=[]   #ti1
f=[] #wt  
phi_i=[]

for i in range(0,m-2):
    id= (z[i+1]-z[i-1])/(2*0.00004)   #i_dash
    i_dash.append(id) 

for i in range(m):
    isquare.append(z[i]*z[i])

for i in range(0,m-2):
    i_dash_w.append(i_dash[i]/w)
    d.append((i_dash_w[i])*(i_dash_w[i]))

for i in range(0,m-2):
    i1=((isquare[i])+(d[i]))**(1/2)
    im.append(i1)
    e.append(math.atan(z[i]/i_dash_w[i]))
    f.append(314*t[i])
    ti=e[i]-f[i]
    phi_i.append(ti)

#calculation of z

Z=[]
phi_z=[]
for i in range(0,n-2):
    Z.append(vm[i]/im[i])
for i in range(0,n-2):
    phi_z.append(phi_v[i]-phi_i[i])

#writing into excel 

workbook = xlsxwriter.Workbook('newsheet.xlsx')
worksheet = workbook.add_worksheet()

#for rows and columns

worksheet.write('A1', 'Sample no.')
worksheet.write('B1', 'V')
worksheet.write('C1', 'I')
worksheet.write('D1', 'Time(sec')
worksheet.write('E1', 'V_dash')
worksheet.write('F1', 'I_dash')
worksheet.write('G1', 'Vsquare')
worksheet.write('H1', 'Isquare')
worksheet.write('I1', 'V_dash/w')
worksheet.write('J1', 'I_dash/w')
worksheet.write('K1', 'V_dash/w^2')
worksheet.write('L1', 'I_dash/w^2')
worksheet.write('M1', 'Vm')
worksheet.write('N1', 'Im')
worksheet.write('O1', 'phi_v')
worksheet.write('P1', 'phi_i')
worksheet.write('Q1', 'Z')
worksheet.write('R1', 'phi_z')

#inserting data in excel

row=1
column=0
for i in s:
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 1
for i in t :
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 2
for i in v:
    worksheet.write(row, column, i)
    row += 1
row = 1
column = 3
for i in z:
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 4
for i in v_dash :
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 5
for i in i_dash :
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 6
for i in vsquare :
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 7
for i in isquare :
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 8
for i in v_dash_w :
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 9
for i in i_dash_w :
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 10
for i in a :
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 11
for i in d :
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 12
for i in vm :
    worksheet.write(row, column, i)
    row += 1
row = 1
column = 13
for i in im :
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 14
for i in phi_v :
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 15
for i in phi_i :
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 16
for i in Z :
    worksheet.write(row, column, i)
    row += 1
row = 1
column = 17
for i in phi_z :
    worksheet.write(row, column, i)
    row += 1

workbook.close()

  







