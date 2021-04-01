import pandas as pd

excel1 = 'excel-1.xlsx'
excel2 = 'excel-2.xlsx'

df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2)

merge = pd.merge(df1, df2, on="fruit")

print(merge)

merge.to_excel("output1.xlsx")
