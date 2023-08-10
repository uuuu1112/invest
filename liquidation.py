from static import *
from base import pbr,balance

todayPBR=baseDfTrans(pbr)[todayPricePbrColumn]
deduct=baseDfTrans(balance)[dictList(balaceDict,deductList)].fillna(0)
# 這是主要的df
liquiShareBaseDf=concatDf([todayPBR,deduct])

def liquiShareDf(shareDf):
    netWorth=shareDf[todayPricePbrColumn[0]]/shareDf[todayPricePbrColumn[1]]
    deductRatio=100-shareDf[balaceDict['debt']]-shareDf[balaceDict['stock']]-shareDf[balaceDict['receive']]-shareDf[balaceDict['invest']]
    shareDf[balaceDict['liquidationValue']]=netWorth*deductRatio/100
    shareDf[balaceDict['liquidEarn']]=(shareDf[balaceDict['liquidationValue']]*1.3/shareDf[todayPricePbrColumn[0]]-1)
    return shareDf

def liquiTable(shareDf,columnList,filterFunction,sortKey):
    columns=dictList(balaceDict,columnList)
    liquiShareData=liquiShareDf(shareDf)
    sortValue=balaceDict[sortKey]
    liquiTable=shareTable(liquiShareData,columns,filterFunction,sortValue)
    return liquiTable.applymap(to_percentage_with_one_decimal)


# 清算價值=總資產-()-()
# (短期負債 長期負債)
# (存貨 應收帳款 長期投資)
# 市價小於清算價值３０％買近（沒設）
# 市價大於清算價值３０％賣出

def liquiFilter(liquiShareDf):
    return liquiShareDf[balaceDict['liquidEarn']]>0

def liquidationModel(shareDf):
    return liquiTable(shareDf,liquidationModelList,liquiFilter,'liquidEarn')
