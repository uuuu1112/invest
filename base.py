from static import *

pbr=pd.read_csv('goodinfo/pbr.csv')
baseInfo=pd.read_csv('goodinfo/baseInfo.csv')

cash=pd.read_csv('goodinfo/year/cash.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')
eps=pd.read_csv('goodinfo/year/eps.csv')

eps4Season=pd.read_csv('goodinfo/last4Season/eps.csv')
seasonRoe=pd.read_csv('goodinfo/last4Season/roe.csv')
balance=pd.read_csv('goodinfo/last4Season/balance.csv')
stock=pd.read_csv('goodinfo/last4Season/stock.csv')

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

class Revenue:
    def __init__(self):
        self.month=month
        self.monthBefore=monthBefore