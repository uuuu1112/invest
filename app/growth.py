from app.stats import *
from app.base import SeasonRoe,SeasonStock,DividendRatio,YearEps,Revenue,YearRoe,cacul

class InnerGrowth:
    def __init__(self,dividendRatio,seasonRoe):
        self.seasonRoe=seasonRoe
        self.dividendRatio=dividendRatio
    def getInnerGrowth(self):
        self.df=pd.DataFrame({})
        self.df[roeDict['roe']]=self.seasonRoe.seasonRoeTrans.loc[roeDict['roe']]/100
        self.df[lynchDict['dividendRatio']]=self.dividendRatio.dividendRatioTrans.iloc[-1]/100
        self.df=self.df[roeDict['roe']]*(1-self.df[lynchDict['dividendRatio']])
        return self.df
class AvgInnerGrowth:
    def __init__(self,dividendRatio,yearRoe,n=5):
        self.yearRoe=yearRoe
        self.dividendRatio=dividendRatio
        self.n=n
    def getAvgInnerGrowth(self):
        self.df=pd.DataFrame({})
        self.df[roeDict['avgRoe']]=self.yearRoe.avgRoe(self.n).iloc[-1]/100
        self.df[cashDict['avgDividendRatio']]=self.dividendRatio.avgDividendRatio(self.n).iloc[-1]/100
        self.df=self.df[roeDict['avgRoe']]*(1-self.df[cashDict['avgDividendRatio']])
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
    def allCAGR(self):
        self.df=pd.DataFrame({})
        self.df[cagrDict['year10Cagr']]=self.year10Cagr()
        self.df[cagrDict['year5Cagr']]=self.year5Cagr()
        self.df[cagrDict['year3Cagr']]=self.year3Cagr()
        self.df[cagrDict['minCagr']]=self.minCagr()
        return self.df
    
class ShortRevenueGrowth:
    def __init__(self,revenue):
        self.revenue=revenue
    def revenueMoM(self):
        return self.revenue.revenueGrowth(1).iloc[-1]
    def revenueYoY(self):
        return self.revenue.revenueGrowth(12).iloc[-1]
    def revenue3Growth(self):
        return self.revenue.revenueNGrowth(3,1).iloc[-1]
    def revenue3YoY(self):
        return self.revenue.revenueNGrowth(3,12).iloc[-1]
    def revenue3MinYoY(self):
        return self.revenue.minGrowth(12,3).iloc[-1]
    def allGrowth(self):
        self.df=pd.DataFrame({})
        self.df[shortGrowthDict['mom']]=self.revenueMoM()
        self.df[shortGrowthDict['yoy']]=self.revenueYoY()
        self.df[shortGrowthDict['revenue3Growth']]=self.revenue3Growth()
        self.df[shortGrowthDict['revenue3YoY']]=self.revenue3YoY()
        self.df[lynchDict['minGrowth']]=self.revenue3MinYoY()
        return self.df.applymap(lambda x: f'{x*100:.2f}%') 
    
class ShortStockGrowth:
    def __init__(self,seasonStock):
        self.stock=seasonStock
    def stockQoQ(self):
        return self.stock.stockGrowth(1)
    def stockYoY(self):
        return self.stock.stockGrowth(4)
    def allGrowth(self):
        self.df=pd.DataFrame({})
        self.df[shortGrowthDict['stockQoQ']]=self.stockQoQ().iloc[-1]
        self.df[shortGrowthDict['stockYoY']]=self.stockYoY().iloc[-1]
        return self.df.applymap(lambda x: f'{x*100:.2f}%') 
    
def getGrowth(selectGrowth):
    dividendRatio=DividendRatio()
    yearEps=YearEps()
    yearCAGR=YearCAGR(yearEps)
    if selectGrowth==growthDict['innerGrowth']:
        seasonRoe=SeasonRoe()
        innerGrowth=InnerGrowth(dividendRatio,seasonRoe)
        return innerGrowth.getInnerGrowth()
    elif selectGrowth==growthDict['avg5InnerGrowth']:
        yearRoe=YearRoe()
        avgInnerGrowth=InnerGrowth(dividendRatio,yearRoe)
        return avgInnerGrowth.getAvgInnerGrowth()
    elif selectGrowth==growthDict['year5CAGR']:
        return yearCAGR.year5Cagr()
    elif selectGrowth==growthDict['min3n5CAGR']:
        return yearCAGR.minCagr()
    elif selectGrowth==growthDict['revenue3MinYOY']:
        revenue=Revenue()
        shortRevenueGrowth=ShortRevenueGrowth(revenue)
        return shortRevenueGrowth.revenue3MinYoY()



