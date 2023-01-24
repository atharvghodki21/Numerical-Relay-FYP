import pandas as pd
data=pd.DataFrame({'vm':["a","b","c","d"]})
data_to_excel=pd.ExcelWriter("newexcel.xlsx")