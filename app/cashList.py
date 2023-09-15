from app.stats import *
from app.base import Cash,SeasonEps,YearEps,SeasonEpsLoseExtraEarn,YearEpsLoseExtraEarn

class SeasonEpsList(SeasonEpsLoseExtraEarn):
    def __init__(self, loseExtra='none'):
        super().__init__(loseExtra)
    def latestEps(self):
        return self.sumEps(4).iloc[-1]
    def minEpsList(self):
        return self.minEps(4).iloc[-1]
    
class YearEpsList(YearEpsLoseExtraEarn):
    def __init__(self, loseExtra='none'):
        super().__init__(loseExtra)
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
    
def getCashList(selectCash, loseExtra='none'):
    cashList=CashList()
    if selectCash==dictMap('latest4SeasonEPS',cashListDict):
        seasonEpsList=SeasonEpsList(loseExtra)
        return seasonEpsList.latestEps()
    elif selectCash==dictMap('avg5YearsEPS',cashListDict):
        yearEpsList=YearEpsList(loseExtra)
        return yearEpsList.avgEps()
    elif selectCash==dictMap('latestCash',cashListDict):
        return cashList.latestCash()
    elif selectCash==dictMap('avg5YearsCash',cashListDict):
        return cashList.avgCashList()


