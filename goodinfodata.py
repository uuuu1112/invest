import pandas as pd
from commonWord import *

pbr=pd.read_csv('goodinfo/pbr.csv')



def baseDfTrans(df):
    df=df.replace(removeStr,'',regex=True)
    df=df.set_index(keyList)
    return df

def lastNMeans(df,columnStr=commonDict['latestAvg'],n=5):
    df=baseDfTrans(df)
    df[columnStr]=df.iloc[:,-5:].mean(axis=1)
    return df[columnStr]

def countConditionNum(df,columnStr=commonDict['conditionCount'],compareBase=0,bigger=1,n=5):
    df=baseDfTrans(df)
    if bigger==1:
        values_count = (df.iloc[:, -n:] > compareBase).sum(axis=1)
    else:
        values_count = (df.iloc[:, -n:] < compareBase).sum(axis=1)
    df[columnStr]=values_count
    return df[columnStr]

def concatDf(dfList):
    return pd.concat(dfList,axis=1)

def to_percentage_with_one_decimal(num):
    return f'{num * 100:.1f}%'

# def tableList()

todayPrice=baseDfTrans(pbr)[todayPriceColumn]