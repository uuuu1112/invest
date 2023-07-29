import pandas as pd
from commonWord import *

def baseDfTrans(df):
    df=df.replace(removeStr,'',regex=True)
    df=df.set_index(keyList)
    return df

def concatDf(dfList):
    return pd.concat(dfList,axis=1)

def shareTable(shareData,columns,filterFunction,sortValue):
    filterCondition=filterFunction(shareData)
    filterDf=shareData[filterCondition]
    filterDf=filterDf[columns]
    filterDf=filterDf.sort_values(by=sortValue,ascending=False)
    return filterDf

def dictList(dict,keyList):
    return [dict[key] for key in keyList]