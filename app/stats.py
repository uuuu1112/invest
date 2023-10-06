from app.baseDf import *
import datetime

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
    def halfGrowthEpsList(self,eps,startGrowth,n=5,normalGrowth=0.02):
        epsNow=eps
        epsList=[]
        growhNow=startGrowth
        for i in range(n):
            epsNow=epsNow*(1+startGrowth)
            epsList.append(epsNow)
        for j in range(5-n):
            growhNow=growhNow*0.5
            epsNow=epsNow*(1+growhNow)
            epsList.append(epsNow)
        for k in range(5):
            epsNow=epsNow*(1+normalGrowth)
            epsList.append(epsNow)
        return epsList
    
    def futureEpsList(self, eps, startGrowth, n=5, normalGrowth=0.02):
        epsNow=eps
        epsList=[]
        growhNow=startGrowth
        for i in range(n):
            epsNow=epsNow*(1+startGrowth)
            epsList.append(epsNow)
        for j in range(10-n):
            growhNow=growhNow*0.5
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
    def dcfEstimate(self,eps,startGrowth,halfGrowthMode=False,n=5,normalGrowth=0.02,discountRate=0.1,gdpGrowth=0.02):
        if halfGrowthMode:
            epsList=self.halfGrowthEpsList(eps,startGrowth,n,normalGrowth)
        else:
            epsList=self.futureEpsList(eps,startGrowth,n,normalGrowth)
        listDiscountValue=self.discountValue(epsList,discountRate,gdpGrowth)
        return listDiscountValue
    def dcfTrans(self,startGrowth):
        return round(self.dcfEstimate(1,startGrowth),0) 
    def disRate(self,per=10):
        growthList = np.arange(-0.4, 0.41, 0.01).tolist()
        perMap=map(self.dcfTrans,growthList)
        perList=list(perMap)
        perDict=dict(zip(perList,growthList))
        if per<perList[0]:
            per=perList[0]
        elif per>perList[-1]:
            per=perList[-1]
        return round(perDict[per],2)
dcf=DCF()

def setMax(series,maxValue='none'):
    if maxValue=='none':
        return series
    else:
        return series.clip(upper=maxValue)
def setRange(series,maxValue=100,minValue=-100):
    return series.clip(upper=maxValue,lower=minValue)

class DateManage():
    # 今天的日期
    def todayDate(self):
        return datetime.date.today()
    # 轉化成日期
    def transToDate(self,dateString):
        return datetime.datetime.strptime(dateString,'%Y-%m-%d')
    # get time stamp
    def getTimeStamp(self,dateString):
        date=self.transToDate(dateString)
        return datetime.datetime.timestamp(date)
    # 日期轉為文字    
    def transToString(self,date):
        return date.strftime('%Y-%m-%d')

# class ReportData(DateManage):
#     def dateToQuater(self,dateStr):
#         date=self.transToDate(dateStr)
#         timeStamp=self.getTimeStamp(dateStr)
#         if timeStamp>str(date.year)+dictMap('Q4',reportRelease)
#         return