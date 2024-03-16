import pandas as pd
df1=pd.read_csv("df_choro.csv")
del df1["land"]
del df1["region"]
choroDict={}
for year in range(2011,2022):
   df_y=df1[df1["year"]==year]
   lst=[]
   for i in range(10):
    lst.append(df_y.iloc[i].to_dict())
   choroDict[str(year)]=lst
   print(choroDict)