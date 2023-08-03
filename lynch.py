from base import *

month=pd.read_csv('goodinfo/month/month.csv')
monthBefore=pd.read_csv('goodinfo/month/monthBefore.csv')
eps4Season=pd.read_csv('goodinfo/last4Season/eps.csv')
roe4Season=pd.read_csv('goodinfo/last4Season/roe.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')

todayPER=baseDfTrans(pbr)[todayPricePerColumn]
roeEps=baseDfTrans(roe4Season)[roeEpsList]
dividendRatioDf=baseDfTrans(dividendRatio).iloc[:,-1]
epsPositiveCount=countConditionNum(eps4Season,lynchDict['epsOver0'],0,1,4)
revenueGrowthCount=revenueGrowthNum(month,monthBefore,lynchDict['revenueGrowthOver30'])
minGrowth=revenueGrowthMin(month,monthBefore,lynchDict['minGrowth'])
# 這是主要的df
lynchShareBaseDf=concatDf([todayPER,industry,epsPositiveCount,revenueGrowthCount,minGrowth,roeEps,dividendRatioDf])

def lynchShareDf(shareDf):
    dividendRationColuumn=dividendRatioDf.name
    shareDf=shareDf.rename(columns={dividendRationColuumn:lynchDict['dividendRatio']})
    shareDf[commonDict['expectEarn']]=15/shareDf[todayPricePerColumn[1]]-1
    shareDf[lynchDict['expectGrowthEarn']]=shareDf[lynchDict['minGrowth']]*50/shareDf[todayPricePerColumn[1]]-1
    shareDf[lynchDict['priceGoal']]=shareDf[roeEpsList[0]]*(1-shareDf[lynchDict['dividendRatio']] /100)*shareDf[roeEpsList[1]]
    shareDf[lynchDict['innerGrowthEarn']]=shareDf[lynchDict['priceGoal']]/shareDf[todayPricePerColumn[0]]-1
    return shareDf

def lynchTable(shareDf,columnList,filterFunction,sortKey):
    columns=dictList(lynchDict,columnList)
    lynchShareData=lynchShareDf(shareDf)
    sortValue=lynchDict[sortKey]
    lynchTable=shareTable(lynchShareData,columns,filterFunction,sortValue)
    return lynchTable.applymap(to_percentage_with_one_decimal)

# 慶龍林區成長股策略
# 近3個月營收年增率都大於30%
# 連續4計的eps都大於0
# 本益比10倍買進(沒設)
# 本益比15倍賣出
# 不要營建股
def lynchFilter(lynchShareDf):
    return (lynchShareDf[lynchDict['revenueGrowthOver30']]==3)&(lynchShareDf[lynchDict['epsOver0']]==4)&(lynchShareDf[commonDict['industry']]!='建材營造業')

def lynchGrowth(shareDf):
    return lynchTable(shareDf,lynchList,lynchFilter,'expectEarn')

def buffettFilter(lynchShareDf):
    return (lynchShareDf[roeEpsList[0]]>20)&(lynchShareDf[lynchDict['epsOver0']]==4)

def buffett(shareDf):
    return lynchTable(shareDf,buffettList,buffettFilter,'innerGrowthEarn')

# be true 成長股策略
# 近3個月營收年增率都大於0%
# 連續4計的eps都大於0
# 最小年增率乘以50當成本益比賣出
# 不要營建股
def beTrueGrowthFilter(lynchShareDf):
    return (lynchShareDf[lynchDict['minGrowth']]>0)&(lynchShareDf[lynchDict['epsOver0']]==4)&(lynchShareDf[commonDict['industry']]!='建材營造業')

def beTrueGrowth(shareDf):
    return lynchTable(shareDf,beTrueGrowthList,beTrueGrowthFilter,'expectGrowthEarn')