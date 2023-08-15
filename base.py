from static import *
cacul=CaCul()

pbr=pd.read_csv('goodinfo/pbr.csv')
today=pd.read_csv('goodinfo/today.csv')
baseInfo=pd.read_csv('goodinfo/baseInfo.csv')

cash=pd.read_csv('goodinfo/year/cash.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')
eps=pd.read_csv('goodinfo/year/eps.csv')

seasonEps=pd.read_csv('goodinfo/season/eps.csv')
seasonRoe=pd.read_csv('goodinfo/season/roe.csv')
balance=pd.read_csv('goodinfo/season/balance.csv')
seasonStock=pd.read_csv('goodinfo/season/stock.csv')

month=pd.read_csv('goodinfo/month/month.csv')
monthBefore=pd.read_csv('goodinfo/month/monthBefore.csv')

todayPrice=baseDfTrans(pbr)[commonDict['price']]
industry=baseDfTrans(baseInfo)[commonDict['industry']]

class Eps:
    def __init__(self):
        self.eps=eps

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
        # self.dividendRatio=dividendRatio
        self.dividendRatioTrans=self.transDf(dividendRatio)
        # self.dividendRatioDf=self.getDividendRatioDf()
    # def latestDividendRatio(self):
    #     return self.dividendRatioTrans.iloc[-1]
    def avgDividendRatio(self,n):
        return cacul.nPeriodMean(self.dividendRatioTrans,n)
    # def getDividendRatioDf(self):
    #     dividendRatioDf=baseDfTrans(dividendRatio).iloc[:,-1]
    #     dividendRatioDf.name=lynchDict['dividendRatio']
    #     return dividendRatioDf

class SeasonRoe(BaseTrans):
    def __init__(self):
        # self.seasonRoe=seasonRoe
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
        # self.today=today
        self.todayTrans=self.transDf(today)
        # self.todayPer=self.todayTrans.loc['PER']
        # self.todayPbr=self.todayTrans.loc['PBR']
        # self.todayPrice=self.todayTrans.loc['成交']
    def todayPrice(self):
        return self.todayTrans.loc['成交']

class BaseInfo(BaseTrans):
    def __init__(self):
        self.baseInfoTrans=self.baseTrans(baseInfo)
    def industry(self):
        return self.baseInfoTrans.loc['產業別']


