from static import *

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
    
class PastGrowth:
    from base import eps
    def __init__(self):
        self.epsTrend=cagrTrend(self.eps).applymap(to_percentage_with_one_decimal)
        self.epsMinGrowth=self.epsTrend[[cashDict['cagr5'],cashDict['cagr3']]].min(axis=1)

class StockGrowht:
    from base import stockYoYcsv
    def __init__(self):
        self.stockYoY=baseDfTrans(self.stockYoYcsv)