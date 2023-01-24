from pandas import *
import xlsxwriter
import math

#######################################################################################
#for voltage signal
#array for v
df= read_csv("data.csv")                                
v = df['v(t)'].tolist()

#array for t
df1= read_csv("data.csv")                           
t = df['Time'].tolist()

#array for sample no.
df2= read_csv("data.csv")
s = df['Sampleno.'].tolist()

n=len(v)
v_dash=[]

#for finding vt_dash
for i in range(1,n-1):
    v_d= (v[i+1]-v[i-1])/(2*(t[i]-t[i-1]))
    v_dash.append(v_d)
    
#initialising
w=2*3.14*50
wsq=w**2
vsq=[]
v_dash_w=[]
v_dashsq_wsq=[]
v_m=[]
tv1=[]
wt=[]
theta_v=[]

#for finding vsq
for i in range(n):
    vsq.append(v[i]*v[i])
#print(vsq)
   
#for find remaining parameters
for i in range(0,n-2):
    v_dash_w.append(v_dash[i]/w)
    v_dashsq_wsq.append((v_dash_w[i])*(v_dash_w[i]))
    
for i in range(0,n-2):
    vm=((vsq[i])+(v_dashsq_wsq[i]))**(1/2)
    v_m.append(vm)
    tv1.append(math.atan(v[i]/v_dash_w[i]))
    wt.append(2*3.14*50*t[i])
    tv=tv1[i]-wt[i]
    theta_v.append(tv)
    
#################################################################################
#for current signal
#array for i
df= read_csv("data.csv")                                
c = df['i(t)'].tolist()

m=len(c)
i_dash=[]

#for finding it_dash
for i in range(1,m-1):
    i_d= (c[i+1]-c[i-1])/(2*(t[i]-t[i-1]))
    i_dash.append(i_d)
    
#initialising
w=2*3.14*50
wsq=w**2
isq=[]
i_dash_w=[]
i_dashsq_wsq=[]
i_m=[]
ti1=[]
wt=[]
theta_i=[]

#for finding isq
for i in range(m):
    isq.append(c[i]*c[i])
   
#for find remaining parameters
for i in range(0,m-2):
    i_dash_w.append(i_dash[i]/w)
    i_dashsq_wsq.append((i_dash_w[i])*(i_dash_w[i]))
    
for i in range(0,m-2):
    im=((isq[i])+(i_dashsq_wsq[i]))**(1/2)
    i_m.append(im)
    ti1.append(math.atan(c[i]/i_dash_w[i]))
    wt.append(2*3.14*50*t[i])
    ti=ti1[i]-wt[i]
    theta_i.append(ti)
    
############################################################################
#calculating Z
z=[]
theta_z=[]
for i in range(0,n-2):
    z.append(v_m[i]/i_m[i])
for i in range(0,n-2):
    theta_z.append(theta_v[i]-theta_i[i])
    
###########################################################################
'''
#checking for Z fault
z_ref_high=#vlue
z_ref_low=#value
for i in range(0,n-2):
    if z_ref_low<z[i]<z_ref_high:
        continue
    else:
        print('Fault has occured')
    break
###########################################################################
#checking for i fault
i_ref_high=#vlue
i_ref_low=#value
for i in range(0,n-2):
    if i_ref_low<i_m[i]<i_ref_high:
        continue
    else:
        print('Fault has occured')
    break

'''
#########################################################################
#writing data into excel sheet
workbook = xlsxwriter.Workbook('Mannmorrison.xlsx')
worksheet = workbook.add_worksheet()

#for writing column names
worksheet.write('A1', 'Sample no.')
worksheet.write('B1', 'V(t)')
worksheet.write('C1', 'I(t)')
worksheet.write('D1', 'Time')
worksheet.write('E1', 'V(t)_dash')
worksheet.write('F1', 'I(t)_dash')
worksheet.write('G1', 'V(t)^2')
worksheet.write('H1', 'I(t)^2')
worksheet.write('I1', 'V(t)_dash/w')
worksheet.write('J1', 'I(t)_dash/w')
worksheet.write('K1', 'V(t)_dash/w^2')
worksheet.write('L1', 'I(t)_dash/w^2')
worksheet.write('M1', 'V_m')
worksheet.write('N1', 'I_m')
worksheet.write('O1', 'Theta_v')
worksheet.write('P1', 'Theta_i')
worksheet.write('Q1', 'Z')
worksheet.write('R1', 'Theta_z')

#inserting data into columns(mention row and column from where you need to start filling excel sheet)
row = 1
column = 0
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
for i in c:
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
for i in vsq :
    worksheet.write(row, column, i)
    row += 1
row = 2
column = 7
for i in isq :
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
for i in v_dashsq_wsq :
    worksheet.write(row, column, i)
    row += 1
row = 2
column = 11
for i in i_dashsq_wsq :
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 12
for i in v_m :
    worksheet.write(row, column, i)
    row += 1
row = 1
column = 13
for i in i_m :
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 14
for i in theta_v :
    worksheet.write(row, column, i)
    row += 1
row = 1
column = 15
for i in theta_i :
    worksheet.write(row, column, i)
    row += 1

row = 1
column = 16
for i in z :
    worksheet.write(row, column, i)
    row += 1
row = 1
column = 17
for i in theta_z :
    worksheet.write(row, column, i)
    row += 1

workbook.close()
