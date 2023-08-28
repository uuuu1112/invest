from app.stats import *
from app.base import Cash,SeasonEps,YearEps

class SeasonEpsList(SeasonEps):
    def __init__(self):
        super().__init__()
    def latestEps(self):
        return self.sumEps(4).iloc[-1]
    
class YearEpsList(YearEps):
    def __init__(self):
        super().__init__()
    def avgEps(self,n=5):
        return cacul.nPeriodMean(self.epsTrans,n).iloc[-1]
    
class CashList(Cash):
    def __init__(self):
        super().__init__()
    def latestCash(self):
        return self.latest()
    def avgCashList(self,n=5):
        return self.avgCash(n).iloc[-1]

class AllCashList(SeasonEpsList):
    def __init__(self):
        super().__init__()
        self.cashList=CashList()
        self.yearEpsList=YearEpsList()
    def latestSeasonEpsList(self):
        return self.latestEps()
    def avgYearEpsList(self,n=5):
        return self.yearEpsList.avgEps(n)
    def latestCashList(self):
        return self.cashList.latestCash()
    def avgCashList(self,n=5):
        return self.cashList.avgCashList(n)
