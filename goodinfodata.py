import pandas as pd

pbr=pd.read_csv('goodinfo/pbr.csv')
cash=pd.read_csv('goodinfo/year/cash.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')

removeStr=[',','=','"']
keyList=['代號','名稱']
todayPriceColumn=['成交']

def baseDfTrans(df):
    df=df.replace(removeStr,'',regex=True)
    df=df.set_index(keyList)
    return df

def lastNMeans(df,columnStr="近期平均",n=5):
    df=baseDfTrans(df)
    df[columnStr]=df.iloc[:,-5:].mean(axis=1)
    return df[columnStr]

def countConditionNum(df,columnStr="符合個數",bigger=1,compareBase=50,n=5):
    df=baseDfTrans(df)
    if bigger==1:
        values_count = (df.iloc[:, -n:] > compareBase).sum(axis=1)
    else:
        values_count = (df.iloc[:, -n:] < compareBase).sum(axis=1)
    df[columnStr]=values_count
    return df[columnStr]