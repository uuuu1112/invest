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
    # shareDf[cashDict['avgYield']]=shareDf.iloc[:,2]/shareDf[commonDict['price']]
    shareDf[cashDict['avgYield']]=shareDf[cashDict['avgDividend']] /shareDf[commonDict['price']]
    shareDf[commonDict['priceGoal']]=shareDf[cashDict['avgDividend']]/0.05
    shareDf[commonDict['expectEarn']]=shareDf[commonDict['priceGoal']]/shareDf[commonDict['price']]-1
    return shareDf

def cashTable(shareDf,columnList,filterFunction,sortValue):
    columns=dictList(cashDict,columnList)
    cashShareData=cashShareDf(shareDf)
    filterCondition=filterFunction(cashShareData)
    filterDf=shareDf[filterCondition]
    filterDf=filterDf[columns]
    filterDf=filterDf.sort_values(by=cashDict[sortValue],ascending=False)
    return filterDf.applymap(to_percentage_with_one_decimal)


# 凡人說存股策略
# 近一年股息殖利率大於５％
# 近五年平均股息殖利率大於５％
# 連續５年發放股利
# 股息發放率五年平均大於50%
def starkFilter(cashShareDf):
    return (cashShareDf[cashDict['latestYield']]>0.05)&(cashShareDf[cashDict['avgYield']]>0.05)&(cashShareDf[cashDict['cashCount']]==5)&(cashShareDf[cashDict['avgDividendRatio']]>50)

def starkCash(shareDf):
    return cashTable(shareDf,starkList,starkFilter,'avgYield')
    
# 慶龍存股策略
# 選擇進５年 年年都配息的股票
# 以近５年現金股利的平均值 來計算殖利率
# 當現金殖利率來到７％時買進
# 當現金來到５％時賣出
def longFilter(cashShareDf):
    return cashShareDf[cashDict['avgYield']]>0.07

def longCash(shareDf):
    return cashTable(shareDf,longLIst,longFilter,'expectEarn')

