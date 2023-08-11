from static import *

def stockYoY():
    from base import stockYoYcsv
    return baseDfTrans(stockYoYcsv)

class RevenueGrowth:
    from base import month,monthBefore
    def __init__(self):
        self.revenueGrowthCount=revenueGrowthNum(self.month,self.monthBefore,lynchDict['revenueGrowthOver30'])
        self.minGrowth=revenueGrowthMin(self.month,self.monthBefore,lynchDict['minGrowth'])

class InnerGrowth:
    from base import dividendRatio,roe4Season
    def __init__(self):
        self.roeEps=baseDfTrans(self.roe4Season)[roeEpsList]
        self.dividendRatioDf=self.getDividendRatioDf()
    def getDividendRatioDf(self):
        dividendRatioDf=baseDfTrans(self.dividendRatio).iloc[:,-1]
        dividendRatioDf.name=lynchDict['dividendRatio']
        return dividendRatioDf
    def getInnerGrowth(self):
        innerGrowthDf=concatDf([self.roeEps,self.dividendRatioDf])
        innerGrowth=innerGrowthDf[roeEpsList[0]]*(1-innerGrowthDf[lynchDict['dividendRatio']]/100)
        return innerGrowth