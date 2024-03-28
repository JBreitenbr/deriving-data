import pandas as pd
import warnings
warnings.filterwarnings("ignore")
pathDict={"life_expectancy":"API_SP.DYN.LE00.IN_DS2_en_csv_v2_107.csv","hiv":"API_SH.DYN.AIDS.ZS_DS2_en_csv_v2_9.csv","fertility":"API_SP.DYN.TFRT.IN_DS2_en_csv_v2_570.csv","pop_density":"API_EN.POP.DNST_DS2_en_csv_v2_1512.csv","infant_deaths":"API_SP.DYN.IMRT.IN_DS2_en_csv_v2_31.csv","pop_under_15":"API_SP.POP.0014.TO.ZS_DS2_en_csv_v2_3732.csv","neonatal_deaths":"API_SH.DYN.NMRT_DS2_en_csv_v2_3414.csv","under5_deaths":"API_SH.DYN.MORT_DS2_en_csv_v2_1984.csv","undernourish":"API_SN.ITK.DEFC.ZS_DS2_en_csv_v2_36.csv","urban_pop":"API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_702.csv","gdp":"API_NY.GDP.PCAP.CD_DS2_en_csv_v2_184.csv","electricity":"API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_452.csv","mobile_phone":"API_IT.CEL.SETS.P2_DS2_en_csv_v2_2987.csv","pop":"API_SP.POP.TOTL_DS2_en_csv_v2_85.csv","homicides":"API_VC.IHR.PSRC.P5_DS2_en_csv_v2_3892.csv","unemployment":"API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_80.csv","agri":"API_AG.LND.AGRI.ZS_DS2_en_csv_v2_1675.csv","forest":"API_AG.LND.FRST.ZS_DS2_en_csv_v2_123.csv","afofi":"API_NV.AGR.TOTL.ZS_DS2_en_csv_v2_79.csv","phone":"API_IT.MLT.MAIN.P2_DS2_en_csv_v2_2984.csv"}
def regional(dfr,region,cols,pcols):
    y_dict={}
    if region=="Africa (all countries)":
      df=dfr
    else:
      df=dfr[dfr["region"]==region]
    for i in range(len(cols)):
      df["prod"]=df[cols[i]]*df[pcols[i]]
      plst=df["prod"].tolist()
      pcol=df[pcols[i]].tolist()
      sn=0
      for el in plst:
         if el>0:
            sn+=el
      y_dict[cols[i]]=sn/sum(pcol)
      l=pd.DataFrame(y_dict,index=[region])
      l["region"]=region
      l["country"]=region
    return l

def create_dim(dim):
    afr=pd.read_csv("africa.csv")
    path="World Bank Data/"+pathDict[dim]
    d0=pd.read_csv(path,skiprows=4)
    pop0=pd.read_csv("World Bank Data/API_SP.POP.TOTL_DS2_en_csv_v2_85.csv",skiprows=4)
    d0["land"]=d0["Country Name"]
    pop0["land"]=pop0["Country Name"]
    cols=["land","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
    pcols=[]
    for el in cols[1:]:
       ex="p"+el
       pcols.append(ex)
       pop0[ex]=pop0[el]
    pcols=["land"]+pcols
    d=d0[cols]
    pop=pop0[pcols]
    mrg=pd.merge(d,afr,on="land",how="right")
    df=pd.merge(mrg,pop,on="land",how="inner")
    nulls=df.isnull().sum()
    #print(nulls)
    #print(nulls.index)
    yr=nulls[nulls>0]
    pz=yr.index.tolist()
    print(pz)
    print(dim)
    for el in pz:
      print(df[df[el].isnull()])
    y_c=cols[1:]
    y_p=pcols[1:]
    dfList=[df]
    regions=["Africa (all countries)"]+df["region"].unique().tolist()
    for el in regions:
      dfList.append(regional(df,el,y_c,y_p))
    ges=pd.concat(dfList)
    for el in y_p:
      del ges[el]
    del ges["land"]
    del ges["prod"]
    melted=pd.melt(ges,id_vars=["region","country"],value_vars=y_c)
    melted[dim]=round(melted["value"],2)
    melted["year"]=melted["variable"]
    del melted["value"]
    del melted["variable"]
    melted=melted[["region","country","year",dim]]
    sub=melted[melted["region"]==melted["country"]]
    del sub["country"]
    hlp=dim+"_"
    sub[hlp]=sub[dim]
    del sub[dim]
    melted=pd.merge(melted,sub,on=["region","year"],how="right")
    for i in range(len(melted)):
      if pd.isnull(melted.loc[i,dim]):
         melted.loc[i,dim]=melted.loc[i,hlp]
    del melted[hlp]
    melted=melted.sort_values(by=["region","country","year"])
    return melted


   
  