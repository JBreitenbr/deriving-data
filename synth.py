import pandas as pd
colorSchemes=["BuGn","BuPu","GnBu","Greens","OrRd","PuBu","PuBuGn","PuRd","RdPu","YlGn","YlGnBu","YlOrBr","Reds","Oranges","Blues","Greys","Purples","YlOrRd"]
df=pd.read_csv("df_choro.csv")
dims=df.columns[2:-7]
dimDesc={}
dimDesc["life_expectancy"]="Life expectancy at birth, total (years)"
#dimDesc["hiv"]="Prevalence of HIV, total (% of population ages 15-49)"
dimDesc["fertility"]="Fertility rate, total (births per woman)"
#dimDesc["pop_density"]="Population density (people per sq. km of land area)"
dimDesc["infant_deaths"]="Mortality rate, infant (per 1,000 live births)"
dimDesc["pop_under_15"]="Population ages 0-14 (% of total population)"
dimDesc["neonatal_deaths"]="Mortality rate, neonatal (per 1,000 live births)"
dimDesc["under5_deaths"]="Mortality rate, under-5 (per 1,000 live births)"
dimDesc["undernourish"]="Prevalence of undernourishment (% of population)"
dimDesc["urban_pop"]="Urban population (% of total population)"
#dimDesc["gdp"]="GDP per capita (current US$)"
dimDesc["electricity"]="Access to electricity (% of population)"

colorDict={}
for i in range(len(dims)):
  colorDict[dims[i]]="d3.interpolate"+colorSchemes[i]
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
  #dimDict[el]["colorScheme"]=colorDict[el]
print("export let dimsDict=",dimDict)


