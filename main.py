import pandas as pd
from functools import reduce
import derive
dimList=["life_expectancy","hiv","fertility","pop_density","infant_deaths","pop_under_15","neonatal_deaths","under5_deaths","undernourish","urban_pop","gdp","electricity"]
#dimList=["electricity"]
dimDataList=[]
for dim in dimList:
  dimDataList.append(derive.create_dim(dim))


df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['region','country','year'],how="inner"),dimDataList)
pop=derive.create_dim("pop")
pop=pop[pop["region"]!=pop["country"]]

df_merged=pd.merge(df_merged,pop,on=["region","country","year"],how="outer")
df_choro=df_merged[df_merged["region"]!=df_merged["country"]]
popList=df_choro["pop"].tolist()
popList2=[]
for el in popList:
  popList2.append(int(el))

df_choro["population"]=popList2
del df_choro["pop"]
a=pd.read_csv("africa.csv")
df_choro=pd.merge(df_choro,a,on=["region","country"],how="outer")
mar=df_choro[df_choro["country"]=="Morocco"]
mar["country"]="Western Sahara"
mar["capital"]="El Aayoun"
som1=df_choro[df_choro["country"]=="Somalia"]
som1["country"]="Somaliland"
som1["capital"]="Hargeysa"
som2=df_choro[df_choro["country"]=="Somalia"]
som2["country"]="Puntland"
som2["capital"]="Garoowe"
df_choro=pd.concat([df_choro,mar,som1,som2])
df_choro.to_csv("df_choro.csv",index=False)
del df_merged["pop"]
df_merged.to_csv("df_bars.csv",index=False)
