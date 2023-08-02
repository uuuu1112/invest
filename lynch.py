from base import *

month=pd.read_csv('goodinfo/month/month.csv')
monthBefore=pd.read_csv('goodinfo/month/monthBefore.csv')
eps4Season=pd.read_csv('goodinfo/last4Season/eps.csv')

todayPER=baseDfTrans(pbr)[todayPricePerColumn]
epsPositiveCount=countConditionNum(eps4Season,lynchDict['epsOver0'],0,1,4)
revenueGrowthCount=revenueGrowth(month,monthBefore)
# 這是主要的df
lynchShareBaseDf=concatDf([todayPER,epsPositiveCount,revenueGrowthCount])

def lynchShareDf(shareDf):
    shareDf[commonDict['expectEarn']]=(15/shareDf[todayPricePerColumn[0]]/shareDf[todayPricePerColumn[1]])-1
    return shareDf

def lynchTable(shareDf,columnList,filterFunction,sortKey):
    columns=dictList(lynchDict,columnList)
    lynchShareData=lynchShareDf(shareDf)
    sortValue=lynchDict[sortKey]
    lynchTable=shareTable(lynchShareData,columns,filterFunction,sortValue)
    return lynchTable

# 慶龍林區成長股策略
# 近3個月營收年增率都大於30%
# 連續4計的eps都大於0
# 本益比10倍買進
# 本益比15倍賣出
def lynchFilter(lynchShareDf):
    return (lynchShareDf[lynchDict['revenueGrowthOver30']]==3)&(lynchShareDf[lynchDict['epsOver0']]==4)

def lynchGrowth(shareDf):
    return lynchTable(shareDf,lynchList,lynchFilter,'expectEarn')