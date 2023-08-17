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
        return result.iloc[-1]
        # return result.iloc[-1].apply(lambda x: f'{x*100:.2f}%')   

class DCF:    
    # 做出未來10年的EPS列表
    def futureEpsList(self,eps,startGrowth,n=5,halfGrowthRatio=1,normalGrowth=0.02):
        epsNow=eps
        epsList=[]
        growhNow=startGrowth
        for i in range(n):
            epsNow=epsNow*(1+startGrowth)
            epsList.append(epsNow)
        for j in range(5-n):
            growhNow=growhNow*halfGrowthRatio
            epsNow=epsNow*(1+growhNow)
            epsList.append(epsNow)
        for k in range(5):
            epsNow=epsNow*(1+normalGrowth)
            epsList.append(epsNow)
        return epsList

    # 用EPS列表折現
    def discountValue(self,epsList,discountRate=0.1,gdpGrowth=0.02):
        epsDiscount=0
        for i in range(10):
            epsDiscount=epsDiscount+epsList[i]*((1+discountRate)**(-i-1))
        outOf10Dis=epsList[-1]*(1+gdpGrowth)/(discountRate-gdpGrowth)/((1+discountRate)**10)
        epsDiscount=epsDiscount+outOf10Dis
        return epsDiscount

    # 給EPS和成長率做折現估值
    def dcfEstimate(self,eps,startGrowth,n=5,halfGrowthRatio=1,normalGrowth=0.02,discountRate=0.1,gdpGrowth=0.02):
        epsList=self.futureEpsList(eps,startGrowth,n,halfGrowthRatio,normalGrowth)
        listDiscountValue=self.discountValue(epsList,discountRate,gdpGrowth)
        return listDiscountValue