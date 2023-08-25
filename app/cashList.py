from app.stats import *
from app.base import Cash,SeasonEps,YearEps

class SeasonEpsList:
    def __init__(self):
        self.seasonEps=SeasonEps()
    def latestEps(self):
        return self.seasonEps.seasonEps.sumEps(4).iloc[-1]
    
class YearEpsList:
    def __init__(self):
        self.yearEps=YearEps()
    def avgEps(self,n=5):
        return cacul.nPeriodMean(self.yearEps.epsTrans,n).iloc[-1]
    
class CashList:
    def __init__(self):
        self.cash=Cash()
    def latestCash(self):
        return self.cash.latest()
    def avgCash(self,n=5):
        return self.cash.avgCash(self.cash.cashTrans,n)