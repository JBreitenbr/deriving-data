import pandas as pd
df1=pd.read_csv("df_choro.csv")
df1.drop([594,595,596,597,598,599,600,601,602,603,604],inplace=True)
df1.drop([616,617,618,619,620,621,622,623,624,625,626],inplace=True)
df1.drop([605,606,607,608,609,610,611,612,613,614,615],inplace=True)
del df1["land"]
del df1["region"]
choroDict={}
for year in range(2011,2022):
   df_y=df1[df1["year"]==year]
   del df_y["year"]
   lst=[]
   for i in range(len(df_y)):
     d=df_y.iloc[i].to_dict()
     lst.append(d)
   choroDict["year"+str(year)]=lst
print(choroDict)