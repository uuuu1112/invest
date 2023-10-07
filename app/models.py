from app.stats import *
from app.base import Today,SeasonBalance,BaseInfo
# ,SeasonEpsLoseExtraEarn,CashLoseExtraEarn
# ,Cash,SeasonEps
from app.growth import *
from app.cashList import *

today=Today()
baseDf=pd.DataFrame({commonDict['price']:today.todayPrice()})

class InvestBase:
    def filterCondition(self):
        return ""
    def priceGoal(self):
        return
    def expectEarn(self):
        self.df=self.priceGoal()
        return expectEarnTrans(self.df,self.filterCondition())
    def expectEarnApi(self):
        self.df=self.expectEarn().reset_index() 
        allContent={'table':self.df,'descrip':self.descrip()}
        return allContent

# 清算價值=總資產-()-()
# (短期負債 長期負債)
# (存貨 應收帳款 長期投資)
# 市價小於清算價值３０％買近（沒設）
# 市價大於清算價值３０％賣出

class LiquidationInvest(InvestBase):
    def __init__(self,seasonBalance):
        self.seasonBalance=seasonBalance
    def descrip(self):
        return '''
<h3>清算價值投資法</h3>
定義 : 
清算價值 = 總資產 - (短期負債 長期負債) - (存貨 應收帳款 長期投資)<br>
投資策略: 
市價小於清算價值３０％買進，市價大於清算價值３０％賣出<br>
預期報酬率 : 
市價到清算價值*1.3的報酬率
'''
    def getLiquidation(self):
        return self.seasonBalance.getNetWorth()-self.seasonBalance.getDebt()-self.seasonBalance.getStock()-self.seasonBalance.getInvest()-self.seasonBalance.getReceive()
    def baseDf(self):
        self.df=baseDf.copy()
        self.df[balaceDict['liquidationValue']]=self.getLiquidation()
        return self.df
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=self.df[balaceDict['liquidationValue']]*1.3>self.df[commonDict['price']]
        return self.filterCondition
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.getLiquidation()*1.3
        return self.df.round(1)

# 凡人說存股策略
# 近一年股息殖利率大於５％
# 近五年平均股息殖利率大於５％
# 連續５年發放股利
# 股息發放率五年平均大於50%

# 慶龍存股策略
# 選擇進５年 年年都配息的股票
# 以近５年現金股利的平均值 來計算殖利率
# 當現金殖利率來到７％時買進
# 當現金來到５％時賣出

# be true 存股筆記
# 近一年股息殖利率大於５％
# 近五年平均股息殖利率大於５％
# 連續５年發放股利
# 股息發放率五年平均大於50%
# 以近５年現金股利的平均值 來計算殖利率
# 當現金來到５％時賣出
# 依股息成長率估的報酬率

class CashInvest(InvestBase):
    def __init__(self,cashList,dividendRatio):
        self.cash=cashList
        self.dividendRatio=dividendRatio
    def descrip(self):
        return '''
        <h3>慶龍存股策略</h3>
        篩選規則 : <br>
        近五年平均股息殖利率大於５％、連續５年發放股利<br>
        投資策略: <br>
        以近５年現金股利的平均值來計算殖利率。 
        當現金殖利率來到７％時買進 ，當現金殖利率來到５％時賣出<br>
        預期報酬率 : 
        市價到現金殖利率來到５％的報酬率
        '''
    def baseDf(self):
        self.df=baseDf.copy()
        self.df.loc[:,cashDict['avgYield']]=(self.cash.avgCashList()/self.df[commonDict['price']])
        self.df.loc[:,cashDict['minCash']]=self.cash.minCashList()
        self.df.loc[:,cashDict['avgDividendRatio']]=self.dividendRatio.avgDividendRatio(5).iloc[-1]
        return self.df
    def priceGoal(self):
        self.df=self.baseDf()
        self.df.loc[:,commonDict['priceGoal']]=self.cash.avgCashList()/0.05
        return self.df.round(2)
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=(self.df[cashDict['avgYield']]>0.05)&(self.df[cashDict['minCash']]>0)
        return self.filterCondition

class CashInvest2(InvestBase):
    def __init__(self,cashList,dividendRatio,baseInfo):
        self.cash=cashList
        self.dividendRatio=dividendRatio
        self.baseInfo=baseInfo
    def descrip(self):
        return '''
        <h3>延伸存股策略</h3>
        篩選規則 : <br>
        近一年股息殖利率大於５％（業內）、近五年平均股息殖利率大於５％（業內）、
        股息發放率五年平均大於50% 、連續５年發放股利<br>
        投資策略: <br>
        以近５年現金股利的平均值來計算殖利率。 
        當現金殖利率來到７％時買進 ，當現金殖利率來到５％時賣出<br>
        預期報酬率 : 
        市價到現金殖利率來到５％的報酬率
        '''
    def baseDf(self):
        self.df=baseDf.copy()
        self.df[lynchDict['industry']]=self.baseInfo.industry()
        self.df.loc[:,cashDict['latestYield']]=(self.cash.latestCash()/self.df[commonDict['price']])
        self.df.loc[:,cashDict['avgYield']]=(self.cash.avgCashList()/self.df[commonDict['price']])
        self.df.loc[:,cashDict['minCash']]=self.cash.minCashList()
        self.df.loc[:,cashDict['avgDividendRatio']]=self.dividendRatio.avgDividendRatio(5).iloc[-1]
        return self.df
    def priceGoal(self):
        self.df=self.baseDf()
        self.df.loc[:,commonDict['priceGoal']]=self.cash.avgCashList()/0.05
        return self.df.round(2)
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=(self.df[cashDict['latestYield']]>0.05)&(self.df[cashDict['avgYield']]>0.05)&(self.df[cashDict['minCash']]>0)&(self.df[cashDict['avgDividendRatio']]>50)
        return self.filterCondition

# 慶龍林區成長股策略
# 近3個月營收年增率都大於30%
# 連續4季的eps都大於0
# 本益比10倍買進(沒設)
# 本益比15倍賣出
# 不要營建股

class LynchInvest(InvestBase):
    def __init__(self,seasonEpsList,baseInfo,shortRevenueGrowth):
        self.shortRevenueGrowth=shortRevenueGrowth
        self.seasonEps=seasonEpsList
        self.baseInfo=baseInfo
    def descrip(self):
        return '''
        <h3>慶龍林區成長股策略</h3>
        篩選規則 : 
        近3個月營收年增率都大於30% 、連續4季的eps都大於0 、不要營建股<br>
        投資策略: 
        本益比10倍買進 本益比15倍賣出<br>
        預期報酬率 : 
        市價到本益比15倍的報酬率
        '''
    def baseDf(self):
        self.df=baseDf.copy()
        self.df[lynchDict['minGrowth']]=self.shortRevenueGrowth.revenue3MinYoY()
        self.df[lynchDict['minEps']]=self.seasonEps.minEpsList()
        self.df[lynchDict['industry']]=self.baseInfo.industry()
        return self.df
    def filterCondition(self):
        self.df=self.priceGoal()
        self.filterCondition=(self.df[lynchDict['minGrowth']]>0.3)&(self.df[lynchDict['minEps']]>0)&(self.df[lynchDict['industry']]!='建材營造業')&(self.df[commonDict['priceGoal']]>self.df[commonDict['price']])
        return self.filterCondition
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.seasonEps.latestEps()*15
        return self.df.round(1)
    
class LynchInvest2(InvestBase):
    def __init__(self,seasonEpsList,baseInfo,shortRevenueGrowth):
        self.shortRevenueGrowth=shortRevenueGrowth
        self.seasonEps=seasonEpsList
        self.baseInfo=baseInfo
    def descrip(self):
        return '''
        <h3>成長股策略(延伸)</h3>
        篩選規則 : 
        近3個月營收年增率都大於0% 、連續4季的eps(業內)都大於0<br>
        投資策略: 
        eps*3個月的最小月營收年增率(%)/2賣出<br>
        預期報酬率 : 
        市價到(eps*3個月的最小月營收年增率(%))/2的報酬率
        '''
    def baseDf(self):
        self.df=baseDf.copy()
        self.df[lynchDict['minGrowth']]=self.shortRevenueGrowth.revenue3MinYoY()
        self.df[lynchDict['minEps']]=self.seasonEps.minEpsList()
        self.df[lynchDict['industry']]=self.baseInfo.industry()
        return self.df
    def filterCondition(self):
        self.df=self.priceGoal()
        self.filterCondition=(self.df[lynchDict['minGrowth']]>0)&(self.df[lynchDict['minEps']]>0)&(self.df[commonDict['priceGoal']]>self.df[commonDict['price']])
        return self.filterCondition
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.seasonEps.latestEps()*self.df[lynchDict['minGrowth']]*100/2
        return self.df.round(1)

# 林區巴菲特選股
# 近4季ROE在20%以上
# 近4季EPS本益比在10以下(沒設)
# 近4季皆有獲利  

class BuffettInvest(InvestBase):
    def __init__(self,seasonRoe,seasonEpsList,dividendRatio):
        self.seasonRoe=seasonRoe
        self.seasonEps=seasonEpsList
        self.dividendRatio=dividendRatio
        self.innerGrowth=InnerGrowth(self.dividendRatio,self.seasonRoe)
    def descrip(self):
        return '''
        <h3>林區巴菲特選股</h3>
        篩選規則 : 
        近4季ROE在20%以上、近4季EPS本益比在10以下、近4季皆有獲利<br>
        預期報酬率 : 
        市價到 ( 內部成長率(%)*EPS ) 的報酬率
        '''        
    def baseDf(self):
        self.df=baseDf.copy()
        self.df[roeDict['roe']]=self.seasonRoe.seasonRoeTrans.loc[roeDict['roe']]
        self.df[commonDict['eps']]=self.seasonRoe.seasonRoeTrans.loc[commonDict['eps']]
        self.df[lynchDict['dividendRatio']]=self.dividendRatio.dividendRatioTrans.iloc[-1]
        self.df[lynchDict['minEps']]=self.seasonEps.minEps(4).iloc[-1]
        self.df[lynchDict['innerGrowth']]=self.innerGrowth.getInnerGrowth()*100
        return self.df
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=(self.df[roeDict['roe']]>20)&(self.df[lynchDict['minEps']]>0)&(self.df[commonDict['price']]<self.df[commonDict['eps']]*10)
        return self.filterCondition
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.df[lynchDict['innerGrowth']]*self.df[commonDict['eps']]
        return self.df.round(1) 

class ShortTerm(InvestBase):
    def __init__(self,seasonStock,revenue):
        self.seasonStock=seasonStock
        self.revenue=revenue
        self.shortGrowth=ShortGrowth(self.seasonStock,self.revenue)
        self.seasonEps=SeasonEpsList('on')
    def descrip(self):
        return '''
 
        '''  
    def baseDf(self):
        self.df=baseDf.copy()
        self.df[dictTextMap('latest4SeasonEPS',cashListDict)]=self.seasonEps.latestEps()
        self.df[dictTextMap('min3n5CAGR',growthDict)]=getGrowth(dictMap('min3n5CAGR',growthDict),0.4)
        self.df[dictTextMap('revenue3MinYOY',growthDict)]=getGrowth(dictMap('revenue3MinYOY',growthDict),0.4)
        self.df[dictTextMap('innerGrowth',growthDict)]=getGrowth(dictMap('innerGrowth',growthDict),0.4)
        self.df[shortGrowthDict['avgGrowth']]=self.df[[dictTextMap('min3n5CAGR',growthDict),dictTextMap('revenue3MinYOY',growthDict),dictTextMap('innerGrowth',growthDict)]].mean(axis=1)
        per=round(self.df[commonDict['price']]/self.df[dictTextMap('latest4SeasonEPS',cashListDict)],0)
        # self.df[shortGrowthDict['potentialGrowth']]=per
        # self.df[cashDistDict['discount']]=dcf.dcfEstimate(self.df[dictTextMap('latest4SeasonEPS',cashListDict)],self.df[shortGrowthDict['avgGrowth']])
        self.df[shortGrowthDict['stockSellCond']]=self.shortGrowth.shortCond()
        return self.df
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=(self.df[dictTextMap('latest4SeasonEPS',cashListDict)].notna())
        return self.filterCondition
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=dcf.dcfEstimate(self.df[dictTextMap('latest4SeasonEPS',cashListDict)],self.df[shortGrowthDict['avgGrowth']])
        return self.df.round(1) 
    
# 所有基本投資策略的總結
def integrateInvest(selectValue):
    seasonEpsList=SeasonEpsList()
    dividendRatio=DividendRatio()
    if selectValue==dictMap('LiquidationInvest',InvestDict):
        seasonBalance=SeasonBalance()
        liquidationInvest=LiquidationInvest(seasonBalance)
        return liquidationInvest.expectEarnApi()
    elif selectValue==dictMap('CashInvest',InvestDict):
        cashList=CashList()
        cashInvest=CashInvest(cashList,dividendRatio)
        return cashInvest.expectEarnApi()
    elif selectValue==dictMap('LynchInvest',InvestDict):
        revenue=Revenue()
        shortRevenueGrowth=ShortRevenueGrowth(revenue)
        baseInfo=BaseInfo()
        lynchInvest=LynchInvest(seasonEpsList,baseInfo,shortRevenueGrowth)        
        return lynchInvest.expectEarnApi()
    elif selectValue==dictMap('BuffettInvest',InvestDict):
        seasonRoe=SeasonRoe()
        buffettInvest=BuffettInvest(seasonRoe,seasonEpsList,dividendRatio)        
        return buffettInvest.expectEarnApi()
    elif selectValue==dictMap('CashInvest2',InvestDict):
        cashList=CashList('on')
        baseInfo=BaseInfo()
        cashInvest2=CashInvest2(cashList,dividendRatio,baseInfo)
        return cashInvest2.expectEarnApi()
    elif selectValue==dictMap('LynchInvest2',InvestDict):
        revenue=Revenue()
        shortRevenueGrowth=ShortRevenueGrowth(revenue)
        baseInfo=BaseInfo()
        seasonEpsList2=SeasonEpsList('on')
        lynchInvest2=LynchInvest2(seasonEpsList2,baseInfo,shortRevenueGrowth)
        return lynchInvest2.expectEarnApi() 
    elif selectValue==dictMap('shortTerm',InvestDict):
        seasonStock=SeasonStock()
        revenue=Revenue()
        shortTerm=ShortTerm(seasonStock,revenue)
        return shortTerm.expectEarnApi() 

class CashDiscount(InvestBase):
    def __init__(self,cashList,growth):
        self.cashList=cashList
        self.growth=growth
        self.baseInfo=BaseInfo()
    def descrip(self):
        return dcfDescrip
    def baseDf(self):
        self.df=baseDf.copy()
        self.df[lynchDict['industry']]=self.baseInfo.industry()
        self.df[cashDistDict['beginCash']]=self.cashList
        self.df[cashDistDict['expectGrowth']]=self.growth
        return self.df
    def getCashDiscount(self):
        self.df=self.baseDf()
        return dcf.dcfEstimate(self.df[cashDistDict['beginCash']],self.df[cashDistDict['expectGrowth']]).fillna(0)
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.getCashDiscount()
        return self.df
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=(self.df[cashDistDict['beginCash']]>0)&(self.df[cashDistDict['expectGrowth']].notna())& (~self.df[cashDistDict['expectGrowth']].isin([float('inf')]))
        return self.filterCondition
    
class InnerValue(InvestBase):
    def __init__(self,cashDiscount,liquidationInvest):
        self.cashDiscount=cashDiscount
        self.liquidationInvest=liquidationInvest
    def descrip(self):
        return dcfDescrip
    def priceGoal(self):
        self.df=self.cashDiscount.priceGoal()
        self.df.rename(columns={commonDict['priceGoal']:cashDistDict['discount']},inplace=True)
        self.df[balaceDict['liquidationValue']]=self.liquidationInvest.getLiquidation()
        self.df[commonDict['priceGoal']]=self.df[balaceDict['liquidationValue']]+self.df[cashDistDict['discount']]
        return self.df.round(1)  
    
def getPridictValue(selectCash,selectGrowth,maxValue='none',withLiqui='none',loseExtra=None):
    # print('getPridictValue')
    cashList=getCashList(selectCash,loseExtra)
    growth=getGrowth(selectGrowth,maxValue)
    cashDiscount=CashDiscount(cashList,growth)
    if withLiqui=="on":
        seasonBalance=SeasonBalance()
        liquidationInvest=LiquidationInvest(seasonBalance)
        innerValue=InnerValue(cashDiscount,liquidationInvest)
        return innerValue.expectEarnApi()
    else:
        return cashDiscount.expectEarnApi()
