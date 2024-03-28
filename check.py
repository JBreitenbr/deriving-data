import pandas as pd
df1=pd.read_csv("africa.csv")
df2=pd.read_csv("alpha3.csv")

lst1=df1["adm0_a3_is"].tolist()
lst2=df2["alpha-3"].tolist()
added=[]
for i in range(len(lst2)):
  if lst2[i] not in lst1:
    added.append(lst2[i])
pt=df2[df2["alpha-3"].isin(added)]
pt.to_csv("added.csv",index=False)