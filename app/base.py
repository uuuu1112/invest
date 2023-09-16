from app.stats import *


todayPath=os.path.join(os.path.dirname(__file__), '..', 'data', 'today.csv')
baseInfoPath=os.path.join(os.path.dirname(__file__), '..', 'data', 'baseInfo.csv')
cashPath=os.path.join(os.path.dirname(__file__), '..', 'data', 'year','cash.csv')
dividendRatioPath=os.path.join(os.path.dirname(__file__), '..', 'data','year', 'dividendRatio.csv')
yearEpsPath=os.path.join(os.path.dirname(__file__), '..', 'data','year', 'eps.csv')
yearRoePath=os.path.join(os.path.dirname(__file__), '..', 'data', 'year','roe.csv')
yearExtraEarnPath=os.path.join(os.path.dirname(__file__),'..','data','year','extraEarn.csv')

seasonEpsPath=os.path.join(os.path.dirname(__file__), '..', 'data','season', 'eps.csv')
seasonRoePath=os.path.join(os.path.dirname(__file__), '..', 'data','season', 'roe.csv')
seasonBalancePath=os.path.join(os.path.dirname(__file__), '..', 'data','season', 'balance.csv')
seasonStockPath=os.path.join(os.path.dirname(__file__), '..', 'data','season', 'stock.csv')
seasonExtraEarnPath=os.path.join(os.path.dirname(__file__),'..','data','season','extraEarn.csv')

monthPath=os.path.join(os.path.dirname(__file__), '..', 'data', 'month','month.csv')
monthBeforePath=os.path.join(os.path.dirname(__file__), '..', 'data', 'month','monthBefore.csv')

today=pd.read_csv(todayPath)
baseInfo=pd.read_csv(baseInfoPath)

cash=pd.read_csv(cashPath)
dividendRatio=pd.read_csv(dividendRatioPath)
yearEps=pd.read_csv(yearEpsPath)
yearRoe=pd.read_csv(yearRoePath)
yearExtraEarn=pd.read_csv(yearExtraEarnPath)

seasonEps=pd.read_csv(seasonEpsPath)
seasonRoe=pd.read_csv(seasonRoePath)
seasonBalance=pd.read_csv(seasonBalancePath)
seasonStock=pd.read_csv(seasonStockPath)
seasonExtraEarn=pd.read_csv(seasonExtraEarnPath)

month=pd.read_csv(monthPath)
monthBefore=pd.read_csv(monthBeforePath)

class YearEps(BaseTrans):
    def __init__(self):
        self.epsTrans=self.transDf(yearEps)

class YearEpsLoseExtraEarn(YearEps):
    def __init__(self,loseExtra='none'):
        self.yearEpsTransWithExtar=self.transDf(yearEps)
        self.epsTrans=self.epsWithExtra(loseExtra)
    def epsWithExtra(self,loseExtra):
        if loseExtra=='none':
            return self.yearEpsTransWithExtar
        else:
            self.yearExtraEarnTrans=self.transDf(yearExtraEarn,removeExtraEarnColums)
            self.yearPureEpsTrans=(1-self.yearExtraEarnTrans/100)*self.yearExtraEarnTrans
            return self.yearPureEpsTrans

class YearRoe(BaseTrans):
    def __init__(self):
        self.roeTrans=self.transDf(yearRoe)
    def avgRoe(self,n):
        return cacul.nPeriodMean(self.roeTrans,n)
class Cash(BaseTrans):
    def __init__(self):
        self.cashTrans=self.transDf(cash)
    def avgCash(self,n):
        return cacul.nPeriodMean(self.cashTrans,n)
    def minCash(self,n):
        return cacul.nPeriodMin(self.cashTrans,n)
class CashLoseExtraEarn(Cash):
    def __init__(self,loseExtra='none'):
        self.cashWithExtra=self.transDf(cash)
        self.temp=yearExtraEarn
    def yearExtraEaraTrans(self):
        self.yearExtraEarnTrans=self.transDf(yearExtraEarn,removeExtraEarnColums)
        # # 创建一个索引映射字典
        # index_mapping = {str(year): str(int(year) + 1) for year in self.yearExtraEarnTrans.index}

        # # 使用 .rename() 方法将索引替换为新的映射索引
        # self.yearExtraEarnTrans.rename(index=index_mapping, inplace=True)
        return self.yearExtraEarnTrans
class DividendRatio(BaseTrans):
    def __init__(self):
        self.dividendRatioTrans=self.transDf(dividendRatio)
    def avgDividendRatio(self,n):
        return cacul.nPeriodMean(self.dividendRatioTrans,n)

class SeasonRoe(BaseTrans):
    def __init__(self):
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
        self.balanceTrans=self.transDf(seasonBalance).fillna(0)
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
    
class SeasonEpsLoseExtraEarn(SeasonEps):
    def __init__(self,loseExtra='none'):
        self.seasonEpsTransWithExtra=self.transDf(seasonEps,removeExtraEarnColums)
        self.seasonEpsTrans=self.epsWithExtra(loseExtra)
    def epsWithExtra(self,loseExtra):
        if loseExtra=='none':
            return self.seasonEpsTransWithExtra
        else:
            self.seasonExtraEarnTrans=self.transDf(seasonExtraEarn,removeExtraEarnColums)
            self.seasonPureEpsTrans=(1-self.seasonExtraEarnTrans/100)*self.seasonEpsTransWithExtra
            return self.seasonPureEpsTrans

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
    
# print(Today().todayPrice())


