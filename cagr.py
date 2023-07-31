from baseDf import *

def cagrBase(dfStart,dfEnd,n):
    result=dfEnd/dfStart
    result=np.power(result,1/n)-1
    return result

def nYearCagr(df,n=5):
    cagrStr=str(n)+commonDict['cagr']
    df=baseDfTrans(df)
    startDf=df.iloc[:,-n-1]
    endDf=df.iloc[:,-1]
    df[cagrStr]=cagrBase(startDf,endDf,n)
    return df[cagrStr]

def cagrTrend(df):
    dfs=[nYearCagr(df,10),nYearCagr(df,5),nYearCagr(df,3)]
    merged_df=pd.concat(dfs,axis=1)
    return merged_df