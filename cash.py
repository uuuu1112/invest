from goodinfodata import *

cash=pd.read_csv('goodinfo/year/cash.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')

avgDividendRatio=lastNMeans(dividendRatio,cashDict['avgDividendRatio'])
avgCash=lastNMeans(cash,cashDict['avgDividend'])
countCash=countConditionNum(cash,cashDict['cashCount'])
lastCash=baseDfTrans(cash).iloc[:,-1]
shareDf=concatDf([todayPrice,lastCash,avgCash,countCash,avgDividendRatio])

def cashShareDf(shareDf):
    shareDf[cashDict['latestYield']]=shareDf.iloc[:,1]/shareDf[commonDict['price']]
    shareDf[cashDict['avgYield']]=shareDf.iloc[:,2]/shareDf[commonDict['price']]
    return shareDf

# 凡人說存股策略
# 近一年股息殖利率大於５％
# 近五年平均股息殖利率大於５％
# 連續５年發放股利
# 股息發放率五年平均大於50%
def starkFilter(cashShareDf):
    return (cashShareDf[cashDict['latestYield']]>0.05)&(cashShareDf[cashDict['avgYield']]>0.05)&(cashShareDf[cashDict['cashCount']]==5)&(cashShareDf[cashDict['avgDividendRatio']])

def starkCash(shareDf):
    starkColumn=dictList(cashDict, starkList)
    cashShareData=cashShareDf(shareDf)
    filterCondition=starkFilter(cashShareData)
    filterDf=shareDf[filterCondition]
    filterDf= filterDf[starkColumn]
    filterDf= filterDf.sort_values(by=cashDict['avgYield'], ascending=False)
    return filterDf.applymap(to_percentage_with_one_decimal)
    