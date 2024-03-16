import pandas as pd
df=pd.read_csv("df_bars.csv")
dims=df.columns[3:]
print(dims)
countries=df["country"].unique().tolist()
dimDict={}
for el in dims:
  dimDict[el]={}
  dimlst=df[el].tolist()
  for c in countries:
    cdf=df[df["country"]==c]
    lst=cdf[el].tolist()
    dimDict[el][c]=lst
  mini=min(dimlst)
  maxi=max(dimlst)
  if mini>0:
     dimDict[el]["mini"]=mini
  else:
     dimDict[el]["mini"]=0
  dimDict[el]["maxi"]=maxi
print(dimDict)