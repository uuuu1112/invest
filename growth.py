from static import *
from base import DividendRatio,SeasonRoe,Eps,cacul

# class RevenueGrowth(Revenue):
#     # revenue=Revenue()
#     # def __init__(self):

#     def minGrowth(self,n,k):
#         return cacul.nPeriodMin(self.revenueGrowth(n),k).iloc[-1]
#         # self.month=self.revenue.month
#         # self.monthBefore=self.revenue.monthBefore
#         # self.revenueGrowthCount=revenueGrowthNum(self.month,self.monthBefore,lynchDict['revenueGrowthOver30'])
#         # self.minGrowth=revenueGrowthMin(self.month,self.monthBefore,lynchDict['minGrowth'])

class InnerGrowth:
    # dividendRatio=DividendRatio()
    # seasonRoe=SeasonRoe()
    def __init__(self,dividendRatio,seasonRoe):
        # self.roeEps=seasonRoe.roeEps
        # self.dividendRatioDf=dividendRatio.dividendRatioDf
        self.seasonRoe=seasonRoe
        self.dividendRatio=dividendRatio
    def getInnerGrowth(self):
        self.df=pd.DataFrame({})
        self.df[roeEpsList[0]]=self.seasonRoe.seasonRoeTrans.loc[roeEpsList[0]]
        # self.df[roeEpsList[1]]=self.seasonRoe.seasonRoeTrans.loc[roeEpsList[1]]
        self.df[lynchDict['dividendRatio']]=self.dividendRatio.dividendRatioTrans.iloc[-1]/100
        self.df=self.df[roeEpsList[0]]*(1-self.df[lynchDict['dividendRatio']])
        return self.df
        # innerGrowthDf=concatDf([self.roeEps,self.dividendRatioDf])
        # innerGrowth=innerGrowthDf[roeEpsList[0]]*(1-innerGrowthDf[lynchDict['dividendRatio']]/100)
        # return innerGrowth
    
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

