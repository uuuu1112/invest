from static import *
from base import Revenue,DividendRatio,SeasonRoe,Eps

class RevenueGrowth:
    revenue=Revenue()
    def __init__(self):
        self.month=self.revenue.month
        self.monthBefore=self.revenue.monthBefore
        self.revenueGrowthCount=revenueGrowthNum(self.month,self.monthBefore,lynchDict['revenueGrowthOver30'])
        self.minGrowth=revenueGrowthMin(self.month,self.monthBefore,lynchDict['minGrowth'])

class InnerGrowth:
    dividendRatio=DividendRatio()
    seasonRoe=SeasonRoe()
    def __init__(self):
        self.roeEps=self.seasonRoe.roeEps
        self.dividendRatioDf=self.dividendRatio.dividendRatioDf
    def getInnerGrowth(self):
        innerGrowthDf=concatDf([self.roeEps,self.dividendRatioDf])
        innerGrowth=innerGrowthDf[roeEpsList[0]]*(1-innerGrowthDf[lynchDict['dividendRatio']]/100)
        return innerGrowth
    
class PastGrowth:
    epsObject=Eps()
    def __init__(self):
        self.eps=self.epsObject.eps
        self.epsTrend=cagrTrend(self.eps).applymap(to_percentage_with_one_decimal)
        self.epsMinGrowth=self.epsTrend[[cashDict['cagr5'],cashDict['cagr3']]].min(axis=1)

class ShortGrowht:
    def __init__(self,Revenue,Stock):
        self.revenue=Revenue()
        self.stock=Stock()

