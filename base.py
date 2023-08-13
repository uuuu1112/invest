from static import *

pbr=pd.read_csv('goodinfo/pbr.csv')
today=pd.read_csv('goodinfo/today.csv')
baseInfo=pd.read_csv('goodinfo/baseInfo.csv')

cash=pd.read_csv('goodinfo/year/cash.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')
eps=pd.read_csv('goodinfo/year/eps.csv')

eps4Season=pd.read_csv('goodinfo/last4Season/eps.csv')
seasonRoe=pd.read_csv('goodinfo/last4Season/roe.csv')
balance=pd.read_csv('goodinfo/last4Season/balance.csv')
seasonStock=pd.read_csv('goodinfo/last4Season/stock.csv')

month=pd.read_csv('goodinfo/month/month.csv')
monthBefore=pd.read_csv('goodinfo/month/monthBefore.csv')

todayPrice=baseDfTrans(pbr)[commonDict['price']]
industry=baseDfTrans(baseInfo)[commonDict['industry']]

class Eps:
    def __init__(self):
        self.eps=eps

class DividendRatio:
    def __init__(self):
        self.dividendRatio=dividendRatio
        self.dividendRatioDf=self.getDividendRatioDf()
    def getDividendRatioDf(self):
        dividendRatioDf=baseDfTrans(self.dividendRatio).iloc[:,-1]
        dividendRatioDf.name=lynchDict['dividendRatio']
        return dividendRatioDf

class SeasonRoe:
    def __init__(self):
        self.seasonRoe=seasonRoe
        self.roeEps=baseDfTrans(self.seasonRoe)[roeEpsList]

class Revenue(BaseTrans):
    def __init__(self):
        self.month=month
        self.monthBefore=monthBefore
        self.monthTrans=self.dropRows(self.month,baseDropRows+monthDrop)

class Today(BaseTrans):
    def __init__(self):
        self.today=today
        self.todayTrans=self.transDf(self.today)
        self.todayPer=self.todayTrans.loc['PER']
        self.todayPbr=self.todayTrans.loc['PBR']

class Stock(BaseTrans):
    def __init__(self):
        self.stock=seasonStock
        self.stockTrans=self.dropRows(self.stock,baseDropRows+['平均存貨(億)'])
