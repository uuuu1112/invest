from baseDf import *

def nYearCagr(df,n=5):
    cagrStr=str(n)+commonDict['cagr']
    df=baseDfTrans(df)
    result=df.iloc[:,-1]/df.iloc[:,-n-1]
    result=np.power(result,1/n)-1
    df[cagrStr]=result
    return df[cagrStr]

def cagrTrend(df):
    dfs=[nYearCagr(df,10),nYearCagr(df,5),nYearCagr(df,3)]
    merged_df=pd.concat(dfs,axis=1)
    return merged_df