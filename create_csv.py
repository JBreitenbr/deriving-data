import pandas as pd
from functools import reduce
import derive
def create_csv(imputed,output_csv):
    dimList=["life_expectancy","fertility","infant_deaths","under5_deaths","undernourish","electricity","mobile_phone","unemployment","afofi","wparl","industry","hiv","tub"]
    dimDataList=[]
    for dim in dimList:
      dimDataList.append(derive.create_dim(dim,imputed))
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['region','country','year'],how="inner"),dimDataList)
    pop=derive.create_dim("pop",True)
    #pop=pop[pop["region"]!=pop["country"]]

    df_choro=pd.merge(df_merged,pop,on=["region","country","year"],how="outer")
    #df_choro=df_merged[df_merged["region"]!=df_merged["country"]]
    popList=df_choro["pop"].tolist()
    popList2=[]
    for el in popList:
      popList2.append(int(el))

    df_choro["population"]=popList2
    del df_choro["pop"]
    a=pd.read_csv("africa.csv")
    #a["Code"]=a["code"]

    df_choro=pd.merge(df_choro,a,on=["region","country"],how="outer")
    df_choro["Year"]=df_choro["year"]
    del df_choro["year"]
    df_choro.to_csv(output_csv,index=False)
