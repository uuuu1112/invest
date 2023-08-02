from cagr import *
from dcf import *

def lastNMeans(df,columnStr=commonDict['latestAvg'],n=5):
    df=baseDfTrans(df)
    df[columnStr]=df.iloc[:,-n:].mean(axis=1)
    return df[columnStr]

def countCondition(df,columnStr=commonDict['conditionCount'],compareBase=0.3,bigger=1,n=3):
    # df=baseDfTrans(df)
    if bigger==1:
        values_count = (df.iloc[:, -n:] > compareBase).sum(axis=1)
    else:
        values_count = (df.iloc[:, -n:] < compareBase).sum(axis=1)
    df[columnStr]=values_count
    return df[columnStr]

def countConditionNum(df,columnStr=commonDict['conditionCount'],compareBase=0,bigger=1,n=5):
    df=baseDfTrans(df)
    return countCondition(df,columnStr,compareBase,bigger,n)

def to_percentage_with_one_decimal(num):
    return f'{num * 100:.1f}%'

def revenueGrowth(month,monthBefore,columnStr=lynchDict['revenueGrowthOver30']):
    revenue=revenueDfTrans(month)
    revenueBefore=revenueDfTrans(monthBefore)
    result=revenue/revenueBefore-1
    result=result.iloc[:, :-2]
    result=countCondition(result,columnStr)
    return result