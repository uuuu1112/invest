from static import *
from base import SeasonRoe,SeasonStock,DividendRatio,YearEps,cacul


class InnerGrowth:
    def __init__(self,dividendRatio,seasonRoe):
        self.seasonRoe=seasonRoe
        self.dividendRatio=dividendRatio
    def getInnerGrowth(self):
        self.df=pd.DataFrame({})
        self.df[roeEpsList[0]]=self.seasonRoe.seasonRoeTrans.loc[roeEpsList[0]]
        self.df[lynchDict['dividendRatio']]=self.dividendRatio.dividendRatioTrans.iloc[-1]/100
        self.df=self.df[roeEpsList[0]]*(1-self.df[lynchDict['dividendRatio']])
        return self.df
    
class YearCAGR(CAGR):
    def __init__(self,yearEps):
        self.epsTrans=yearEps.epsTrans
    def year10Cagr(self):
        return self.baseCagr(self.epsTrans,10)
    def year5Cagr(self):
        return self.baseCagr(self.epsTrans,5)
    def year3Cagr(self):
        return self.baseCagr(self.epsTrans,3)
    def minCagr(self):
        index=self.year3Cagr().index
        min_values = [min(val1, val2) for val1, val2 in zip(self.year3Cagr(), self.year5Cagr())]
        return pd.Series(min_values, index=index)
    
class ShortGrowht:
    def __init__(self,revenue,stock):
        self.revenue=revenue
        self.stock=stock
    def revenueMoM(self):
        return self.revenue.revenueGrowth(1)
    def revenueYoY(self):
        return self.revenue.revenueGrowth(12)
    def revenue3Growth(self):
        return self.revenue.revenueNGrowth(3,1)
    def revenue3YoY(self):
        return self.revenue.revenueNGrowth(3,12)
    def stockQoQ(self):
        return self.stock.stockGrowth(1)
    def stockYoY(self):
        return self.stock.stockGrowth(4)

