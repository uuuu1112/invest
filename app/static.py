from baseDf import *

class CaCul:
    def nPeriodSum(self,transDf,n):
        return transDf.rolling(window=n,min_periods=n).sum()
    def nPeriodGrowth(self,transDf,n):
        return transDf/transDf.shift(n)-1
    def nPeriodMin(self,transDf,n):
        return transDf.rolling(window=n,min_periods=n).min()
    def nPeriodMean(self,transDf,n):
        return transDf.rolling(window=n,min_periods=n).mean()

cacul=CaCul()

class CAGR:
    def baseCagr(self,transDf,n):
        result=cacul.nPeriodGrowth(transDf,n)+1
        result=np.power(result,1/n)-1
        return result.iloc[-1].apply(lambda x: f'{x*100:.2f}%')       
