from app.stats import *
from app.base import Cash,SeasonEps,YearEps

class SeasonEpsList(SeasonEps):
    def __init__(self):
        super().__init__()
    def latestEps(self):
        return self.sumEps(4).iloc[-1]
    def minEpsList(self):
        return self.minEps(4).iloc[-1]
    
class YearEpsList(YearEps):
    def __init__(self):
        super().__init__()
    def avgEps(self,n=5):
        return cacul.nPeriodMean(self.epsTrans,n).iloc[-1]
    
class CashList(Cash):
    def __init__(self):
        super().__init__()
    def latestCash(self):
        return self.cashTrans.iloc[-1]
    def avgCashList(self,n=5):
        return self.avgCash(n).iloc[-1]
    def minCashList(self,n=5):
        return self.minCash(n).iloc[-1]
    
def getCashList(selectCash):
    cashList=CashList()
    if selectCash==cashListDict['latest4SeasonEPS']:
        seasonEpsList=SeasonEpsList()
        return seasonEpsList.latestEps()
    elif selectCash==cashListDict['avg5YearsEPS']:
        yearEpsList=YearEpsList()
        return yearEpsList.avgEps()
    elif selectCash==cashListDict['latestCash']:
        return cashList.latestCash()
    elif selectCash==cashListDict['avg5YearsCash']:
        return cashList.avgCashList()


