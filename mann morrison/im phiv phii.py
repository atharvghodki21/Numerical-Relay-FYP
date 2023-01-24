from pandas import *
import math
import xlsxwriter
df = pd.read_excel(r"D:\R&D_2023\sample_data.xlsx")
#print(df)
v=df['v']
i=df['i']
T=df['t']
n=len(v)
deltaT=0.00002
v1=[]
phi_v=[]
i1=[]
phi_i=[]
v_dash=[]
i_dash=[]
w=(math.pi)*100
r_perkm=0.01
xbyr=10
linelength=100
R=r_perkm*linelength
X=R*xbyr
Z=math.sqrt(math.pow(R,2)+math.pow(X,2))
for j in range(1,n-1):
    vdash = ((v[j + 1] - v[j - 1]) / (2*0.00002))
    idash = ((i[j + 1] - i[j - 1]) / (2*0.00002))
    v_dash.append(vdash)
    i_dash.append(idash)
    im=math.sqrt((i[j]**2)+((i[j+1]-i[j-1])/(w*0.00004))**2)
    i1.append(im)
    #phi_i
    a=math.atan(i[j]/(idash/w))
    phii=math.degrees(a-(w*T[j]))
    phi_i.append(phii)
    #phi_v
    b=math.atan(v[j]/(vdash/w))
    phiv=b-(w*T[j])
    phi_v.append(phiv)
    #vm
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
#print(v1) #it is vm
#print(T[j+1])
# print("this is time at which fault occured")
#vm.to_excel("sample1.xlsx",index=false)
print('this is vm')
print(v1)
print('this is phi_v')
print(phi_v)
print('this is im')
print(i1)
print('this is phi_i')
print(phi_i)
#print(v_dash)
#print(i_dash)


