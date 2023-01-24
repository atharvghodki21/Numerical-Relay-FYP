from pandas import *
import xlsxwriter
import math
import time # import the time module


start_time = time.time()




df = read_csv(r"C:\Users\HP\Documents\sampleDATA.csv")
s = df['sample no.'].tolist()

df1 = read_csv(r"C:\Users\HP\Documents\sampleDATA.csv")
v = df['v'].to_list()

df2 = read_csv(r"C:\Users\HP\Documents\sampleDATA.csv")
t = df['t'].to_list()

df3 = read_csv(r"C:\Users\HP\Documents\sampleDATA.csv")
z = df['i'].tolist()

n = len(v)
w = 314
v_dash = []
vsquare = []
v_dash_w = []
a = []
a2=[]# v_dash^2*w^2
vm = []
b = []
c = []
phi_v = []
# for v_dash and voltage parameters
for i in range(1, n - 1):
    vd = (v[i + 1] - v[i - 1]) / (2 * (t[i]-t[i-1]))
    v_dash.append(vd)
for i in range(1,n-1):
    vsquare.append(v[i] * v[i])  # v**2

for i in range(0, n - 2):
    a.append((v_dash[i]/w))

for i in range(0,n-2):
    a2.append(a[i]*a[i])

for i in range(0, n - 2):
    v1 = math.sqrt((v[i]*2)+((v[i+1]-v[i-1])/(w*0.00004))*2)
    vm.append(v1)
    b.append(math.atan(v[i]/a[i]))
    pv = math.degrees(b[i] - (w*t[i]))
    phi_v.append(pv)

# current parameters
m = len(z)
i_dash = []
isquare = []
i_dash_w = []  # i_dash/w
d = []
d2=[]# i_dash*2/w*2
im = []
e = []  # ti1
f = []  # wt
phi_i = []

for i in range(1, m - 1):
    id = (z[i + 1] - z[i - 1]) / (2 * (t[i]-t[i-1]))  # i_dash
    i_dash.append(id)

for i in range(1,m-1):
    isquare.append(z[i] * z[i])

for i in range(0, m - 2):
    d.append((i_dash[i])/w)

for i in range(0,m-2):
    d2.append(d[i]*d[i])

for i in range(0, m - 2):
    i1=math.sqrt((z[i]*2)+((z[i+1]-z[i-1])/(w*0.00004))*2)
    im.append(i1)
    e.append(math.atan(z[i]/d[i]))
    phii=math.degrees(e[i]-(w*t[i]))
    phi_i.append(phii)

# calculation of z

Z = []
phi_z = []
for i in range(0, n - 2):
    Z.append(vm[i] / im[i])
for i in range(0, n - 2):
    phi_z.append(phi_v[i] - phi_i[i])

#print(vm)
#print(im)






#-------------------------------------------------------------------------------------------------------------------






for j in range(1,n-1):
    #vdash = ((v[j + 1] - v[j - 1]) / (0.00004))
    #v_dash.append(vdash)
    #vm=math.sqrt((v[j]*2)+((v[j+1]-v[j-1])/(w*0.00004))*2)
    #v1.append(vm)
    if (v1>253 or v1<207):
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
    
print(vm) #it is vm



    






#------------------------------------------------------------------------------------------------------------

# writing into excel

workbook = xlsxwriter.Workbook('newsheet5.xlsx')
worksheet = workbook.add_worksheet()

# for rows and columns

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

# inserting data in excel

row = 1
column = 0
for i in s:
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 1
for i in t:
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
for i in v_dash:
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 5
for i in i_dash:
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 6
for i in vsquare:
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 7
for i in isquare:
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 8
for i in a:
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 9
for i in d:
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 10
for i in a2:
    worksheet.write(row, column, i)
    row += 1

row = 2
column = 11
for i in d2:
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 12
for i in vm:
    worksheet.write(row, column, i)
    row += 1
row = 1
column = 13
for i in im:
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 14
for i in phi_v:
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 15
for i in phi_i:
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 16
for i in Z:
    worksheet.write(row, column, i)
    row += 1
row = 1
column = 17
for i in phi_z:
    worksheet.write(row, column, i)
    row += 1

workbook.close()






end_time = time.time()

execution_time = end_time - start_time

print("Execution Time:", execution_time)
