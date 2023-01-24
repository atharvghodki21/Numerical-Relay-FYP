import pandas as pd
import math
from openpyxl import load_workbook

df = pd.read_excel(r"D:\R&D_2023\sample_data.xlsx")
print(df)
v=df['V'].tolist()
print(v)
#df = pd.DataFrame({'vm': [0,229.99,229.99,0]})
#print(df)
with pd.ExcelWriter('sample_data.xlsx',mode='a') as writer:
    df.to_excel(writer, sheet_name='sample data')


# #load excel file
# workbook = load_workbook(filename="D:\R&D_2023\sample_data.xlsx")
#
# #open workbook
# sheet = workbook.active
#
# # modify the desired cell
# sheet["A1"] = "Full Name"
#
# #save the file
# workbook.save(filename="D:\R&D_2023\sample_data.xlsx")




#df=pd.read_excel(r"C:\Users\HP\Documents\sample_data.xlsx")
