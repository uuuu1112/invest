from static import *

pbr=pd.read_csv('goodinfo/pbr.csv')
today=pd.read_csv('goodinfo/today.csv')
baseInfo=pd.read_csv('goodinfo/baseInfo.csv')

cash=pd.read_csv('goodinfo/year/cash.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')
yearEps=pd.read_csv('goodinfo/year/eps.csv')

seasonEps=pd.read_csv('goodinfo/season/eps.csv')
seasonRoe=pd.read_csv('goodinfo/season/roe.csv')
balance=pd.read_csv('goodinfo/season/balance.csv')
seasonStock=pd.read_csv('goodinfo/season/stock.csv')

month=pd.read_csv('goodinfo/month/month.csv')
monthBefore=pd.read_csv('goodinfo/month/monthBefore.csv')

todayPrice=baseDfTrans(pbr)[commonDict['price']]
industry=baseDfTrans(baseInfo)[commonDict['industry']]

class YearEps(BaseTrans):
    def __init__(self):
        self.epsTrans=self.transDf(yearEps)

class Cash(BaseTrans):
    def __init__(self):
        self.cashTrans=self.transDf(cash)
    def latestCash(self):
        return self.cashTrans
    def avgCash(self,n):
        return cacul.nPeriodMean(self.cashTrans,n)
    def minCash(self,n):
        return cacul.nPeriodMin(self.cashTrans,n)

class DividendRatio(BaseTrans):
    def __init__(self):
        self.dividendRatioTrans=self.transDf(dividendRatio)
    def avgDividendRatio(self,n):
        return cacul.nPeriodMean(self.dividendRatioTrans,n)

class SeasonRoe(BaseTrans):
    def __init__(self):
        self.roeEps=baseDfTrans(seasonRoe)[roeEpsList]
        self.seasonRoeTrans=self.transDf(seasonRoe)

class SeasonEps(BaseTrans):
    def __init__(self):
        self.seasonEpsTrans=self.transDf(seasonEps)
    def minEps(self,n):
        return cacul.nPeriodMin(self.seasonEpsTrans,n)
    def sumEps(self,n):
        return cacul.nPeriodSum(self.seasonEpsTrans,n)

class Stock(BaseTrans):
    def __init__(self):
        self.stockTrans=self.dropRows(seasonStock,baseDropRows+['平均存貨(億)'])

class Revenue(BaseTrans):
    def __init__(self):
        self.monthTrans=self.dropRows(month,baseDropRows+monthDrop)
        self.monthBeforeTrans=self.dropRows(monthBefore,baseDropRows+monthDrop)
        self.revenueDf=pd.concat([self.monthBeforeTrans,self.monthTrans])
    def revenueGrowth(self,n):
        return cacul.nPeriodGrowth(self.revenueDf,n)
    def minGrowth(self,n,k):
        return cacul.nPeriodMin(self.revenueGrowth(n),k)

class Today(BaseTrans):
    def __init__(self):
        self.todayTrans=self.transDf(today)
    def todayPrice(self):
        return self.todayTrans.loc['成交']

class BaseInfo(BaseTrans):
    def __init__(self):
        self.baseInfoTrans=self.baseTrans(baseInfo)
    def industry(self):
        return self.baseInfoTrans.loc['產業別']


