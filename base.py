from static import *

pbr=pd.read_csv('goodinfo/pbr.csv')
today=pd.read_csv('goodinfo/today.csv')
baseInfo=pd.read_csv('goodinfo/baseInfo.csv')

cash=pd.read_csv('goodinfo/year/cash.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')
eps=pd.read_csv('goodinfo/year/eps.csv')

eps4Season=pd.read_csv('goodinfo/season/eps.csv')
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

class DividendRatio(BaseTrans):
    def __init__(self):
        # self.dividendRatio=dividendRatio
        self.dividendRatioTrans=self.transDf(dividendRatio)
        # self.dividendRatioDf=self.getDividendRatioDf()
    def latestDividendRatio(self):
        return self.dividendRatioTrans.iloc[-1]
    def getDividendRatioDf(self):
        dividendRatioDf=baseDfTrans(dividendRatio).iloc[:,-1]
        dividendRatioDf.name=lynchDict['dividendRatio']
        return dividendRatioDf

class SeasonRoe:
    def __init__(self):
        # self.seasonRoe=seasonRoe
        self.roeEps=baseDfTrans(seasonRoe)[roeEpsList]

class Revenue(BaseTrans):
    def __init__(self):
        self.month=month
        self.monthBefore=monthBefore
        self.monthTrans=self.dropRows(month,baseDropRows+monthDrop)
        self.monthBeforeTrans=self.dropRows(monthBefore,baseDropRows+monthDrop)
        self.revenueDf=pd.concat([self.monthBeforeTrans,self.monthTrans])

class Today(BaseTrans):
    def __init__(self):
        # self.today=today
        self.todayTrans=self.transDf(today)
        self.todayPer=self.todayTrans.loc['PER']
        self.todayPbr=self.todayTrans.loc['PBR']
        self.todayPrice=self.todayTrans.loc['成交']

class Stock(BaseTrans):
    def __init__(self):
        # self.stock=seasonStock
        self.stockTrans=self.dropRows(seasonStock,baseDropRows+['平均存貨(億)'])
