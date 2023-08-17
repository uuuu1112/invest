from stats import *

today=pd.read_csv(dataPath+'/today.csv')
baseInfo=pd.read_csv(dataPath+'/baseInfo.csv')

cash=pd.read_csv(dataPath+'/year/cash.csv')
dividendRatio=pd.read_csv(dataPath+'/year/dividendRatio.csv')
yearEps=pd.read_csv(dataPath+'/year/eps.csv')

seasonEps=pd.read_csv(dataPath+'/season/eps.csv')
seasonRoe=pd.read_csv(dataPath+'/season/roe.csv')
seasonBalance=pd.read_csv(dataPath+'/season/balance.csv')
seasonStock=pd.read_csv(dataPath+'/season/stock.csv')

month=pd.read_csv(dataPath+'/month/month.csv')
monthBefore=pd.read_csv(dataPath+'/month/monthBefore.csv')

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
        # self.roeEps=baseDfTrans(seasonRoe)[roeEpsList]
        self.seasonRoeTrans=self.transDf(seasonRoe)

class SeasonEps(BaseTrans):
    def __init__(self):
        self.seasonEpsTrans=self.transDf(seasonEps)
    def minEps(self,n):
        return cacul.nPeriodMin(self.seasonEpsTrans,n)
    def sumEps(self,n):
        return cacul.nPeriodSum(self.seasonEpsTrans,n)

class SeasonStock(BaseTrans):
    def __init__(self):
        self.stockTrans=self.dropRows(seasonStock,baseDropRows+['平均存貨(億)'])
    def stockGrowth(self,n):
        return cacul.nPeriodGrowth(self.stockTrans,n)

class SeasonBalance(BaseTrans):
    def __init__(self):
        self.balanceTrans=self.transDf(seasonBalance)
    def getNetWorth(self):
        return self.balanceTrans.loc['每股淨值(元)']
    def getDebt(self):
        return self.balanceTrans.loc['負債總額(%)']*self.getNetWorth()/100
    def getStock(self):
        return self.balanceTrans.loc['存貨(%)']*self.getNetWorth()/100
    def getInvest(self):
        return self.balanceTrans.loc['投資(%)']*self.getNetWorth()/100
    def getReceive(self):
        return self.balanceTrans.loc['應收帳款(%)']*self.getNetWorth()/100

class Revenue(BaseTrans):
    def __init__(self):
        self.monthTrans=self.dropRows(month,baseDropRows+monthDrop)
        self.monthBeforeTrans=self.dropRows(monthBefore,baseDropRows+monthDrop)
        self.revenueDf=pd.concat([self.monthBeforeTrans,self.monthTrans])
    def revenueGrowth(self,n):
        return cacul.nPeriodGrowth(self.revenueDf,n)
    def minGrowth(self,n,k):
        return cacul.nPeriodMin(self.revenueGrowth(n),k)
    def revenueNGrowth(self,n,k):
        revenueNSum=cacul.nPeriodMin(self.revenueDf,n)
        revenueNGrowth=cacul.nPeriodGrowth(revenueNSum,k)
        return revenueNGrowth

class Today(BaseTrans):
    def __init__(self):
        self.todayTrans=self.transDf(today)
    def todayPrice(self):
        return self.todayTrans.loc['成交']
    def todayPBR(self):
        return self.todayTrans.loc['PBR']

class BaseInfo(BaseTrans):
    def __init__(self):
        self.baseInfoTrans=self.baseTrans(baseInfo)
    def industry(self):
        return self.baseInfoTrans.loc['產業別']


