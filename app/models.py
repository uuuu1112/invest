from app.stats import *
from app.base import Today,SeasonBalance,Cash,SeasonEps,BaseInfo
from app.growth import *
from app.cashList import *

today=Today()

# 清算價值=總資產-()-()
# (短期負債 長期負債)
# (存貨 應收帳款 長期投資)
# 市價小於清算價值３０％買近（沒設）
# 市價大於清算價值３０％賣出

class LiquidationInvest:
    def __init__(self,seasonBalance=SeasonBalance()):
        self.seasonBalance=seasonBalance
        self.todayPrice=today.todayPrice()
    def getLiquidation(self):
        return self.seasonBalance.getNetWorth()-self.seasonBalance.getDebt()-self.seasonBalance.getStock()-self.seasonBalance.getInvest()-self.seasonBalance.getReceive()
    def baseDf(self):
        self.df=pd.DataFrame({})
        self.df[balaceDict['liquidationValue']]=self.getLiquidation()
        return self.df
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.getLiquidation()*1.3
        return self.df
    def expectEarn(self):
        self.df=self.priceGoal()
        self.df[commonDict['expectEarn']]=self.df[commonDict['priceGoal']]/self.todayPrice-1
        return expectEarnTrans(self.df)

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

class CashInvest:
    def __init__(self,cash=Cash(),dividendRatio=DividendRatio()):
        self.cash=cash
        self.dividendRatio=dividendRatio
        self.todayPrice=today.todayPrice()
    def baseDf(self):
        self.df=pd.DataFrame({})
        self.df[cashDict['latestYield']]=(self.cash.latest()/self.todayPrice)
        self.df[cashDict['avgYield']]=(self.cash.avgCash(5).iloc[-1]/self.todayPrice)
        self.df[cashDict['minCash']]=self.cash.minCash(5).iloc[-1]
        self.df[cashDict['avgDividendRatio']]=self.dividendRatio.avgDividendRatio(5).iloc[-1]
        return self.df
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.cash.avgCash(5).iloc[-1]/0.05
        return self.df
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=(self.df[cashDict['latestYield']]>0.05)&(self.df[cashDict['avgYield']]>0.05)&(self.df[cashDict['minCash']]>0)&(self.df[cashDict['avgDividendRatio']]>50)
        return self.filterCondition
    def expectEarn(self):
        self.df=self.priceGoal()
        self.df[commonDict['expectEarn']]=self.df[commonDict['priceGoal']]/self.todayPrice-1
        return expectEarnTrans(self.df,self.filterCondition())

# 慶龍林區成長股策略
# 近3個月營收年增率都大於30%
# 連續4季的eps都大於0
# 本益比10倍買進(沒設)
# 本益比15倍賣出
# 不要營建股

class LynchInvest:
    def __init__(self,seasonEps=SeasonEps(),baseInfo=BaseInfo()):
        self.shortRevenueGrowht=ShortRevenueGrowth()
        self.seasonEps=seasonEps
        self.baseInfo=baseInfo
        self.todayPrice=today.todayPrice()
    def baseDf(self):
        self.df=pd.DataFrame({})
        self.df[lynchDict['minGrowth']]=self.shortRevenueGrowht.revenue3MinYoY()
        self.df[lynchDict['minEps']]=self.seasonEps.minEps(4).iloc[-1]
        self.df[lynchDict['industry']]=self.baseInfo.industry()
        return self.df
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=(self.df[lynchDict['minGrowth']]>0.3)&(self.df[lynchDict['minEps']]>0)&(self.df[lynchDict['industry']]!='建材營造業')
        return self.filterCondition
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.seasonEps.sumEps(4).iloc[-1]*15
        return self.df
    def expectEarn(self):
        self.df=self.priceGoal()
        self.df[commonDict['expectEarn']]=self.df[commonDict['priceGoal']]/self.todayPrice-1
        return expectEarnTrans(self.df,self.filterCondition())

# 林區巴菲特選股
# 近4季ROE在20%以上
# 近4季EPS本益比在10以下(沒設)
# 近4季皆有獲利  

class Buffett:
    def __init__(self,seasonRoe=SeasonRoe(),seasonEps=SeasonEps(),dividendRatio=DividendRatio()):
        self.seasonRoe=seasonRoe
        self.seasonEps=seasonEps
        self.dividendRatio=dividendRatio
        self.innerGrowth=InnerGrowth(self.dividendRatio,self.seasonRoe)
        self.todayPrice=today.todayPrice()
    def baseDf(self):
        self.df=pd.DataFrame({})
        self.df[roeDict['roe']]=self.seasonRoe.seasonRoeTrans.loc[roeDict['roe']]
        self.df[commonDict['eps']]=self.seasonRoe.seasonRoeTrans.loc[commonDict['eps']]
        self.df[lynchDict['dividendRatio']]=self.dividendRatio.dividendRatioTrans.iloc[-1]
        self.df[lynchDict['minEps']]=self.seasonEps.minEps(4).iloc[-1]
        self.df[lynchDict['innerGrowth']]=self.innerGrowth.getInnerGrowth()*100
        return self.df
    def filterCondition(self):
        self.df=self.baseDf()
        self.filterCondition=(self.df[roeDict['roe']]>20)&(self.df[lynchDict['minEps']]>0)
        return self.filterCondition
    def priceGoal(self):
        self.df=self.baseDf()
        self.df[commonDict['priceGoal']]=self.df[lynchDict['innerGrowth']]*self.df[commonDict['eps']]
        return self.df
    def expectEarn(self):
        self.df=self.priceGoal()
        self.df[commonDict['expectEarn']]=self.df[commonDict['priceGoal']]/self.todayPrice-1
        return expectEarnTrans(self.df,self.filterCondition())

class CashDiscount:
    def __init__(self,cashList,growth):
        self.cashList=cashList
        self.growth=growth
        self.todayPrice=today.todayPrice()
    def baseDf(self):
        self.df=pd.DataFrame({})
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
    def expectEarn(self):
        self.df=self.priceGoal()
        self.df[commonDict['expectEarn']]=self.df[commonDict['priceGoal']]/self.todayPrice-1
        return expectEarnTrans(self.df,self.filterCondition())
    
class InnerValue:
    def __init__(self,cashDiscount,liquidationInvest=LiquidationInvest()):
        self.cashDiscount=cashDiscount
        self.liquidationInvest=liquidationInvest
        self.todayPrice=today.todayPrice()
    def baseDf(self):
        self.df=self.cashDiscount.priceGoal()
        self.df.rename(columns={commonDict['priceGoal']:cashDistDict['discount']},inplace=True)
        self.df[balaceDict['liquidationValue']]=self.liquidationInvest.getLiquidation()
        self.df[commonDict['price']]=self.todayPrice
        self.df[commonDict['priceGoal']]=self.df[balaceDict['liquidationValue']]+self.df[cashDistDict['discount']]
        return self.df
    def expectEarn(self):
        self.df=self.baseDf()
        self.df[commonDict['expectEarn']]=self.df[commonDict['priceGoal']]/self.todayPrice-1
        return expectEarnTrans(self.df)
    