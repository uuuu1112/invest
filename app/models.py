from stats import *
from base import Today,SeasonBalance,Cash,DividendRatio,SeasonEps,BaseInfo,Revenue,SeasonRoe
from growth import InnerGrowth

# 清算價值=總資產-()-()
# (短期負債 長期負債)
# (存貨 應收帳款 長期投資)
# 市價小於清算價值３０％買近（沒設）
# 市價大於清算價值３０％賣出

class LiquidationInvest:
    def __init__(self,seasonBalance,today):
        self.seasonBalance=seasonBalance
        self.todayPrice=today.todayPrice()
    def getLiquidation(self):
        return self.seasonBalance.getNetWorth()-self.seasonBalance.getDebt()-self.seasonBalance.getStock()-self.seasonBalance.getInvest()-self.seasonBalance.getReceive()
    def expectEarn(self):
        self.df=pd.DataFrame({})
        self.df[balaceDict['price']]=self.todayPrice
        self.df[balaceDict['liquidationValue']]=self.getLiquidation()
        self.df[balaceDict['expectEarn']]=self.getLiquidation()*1.3/self.todayPrice-1
        self.filterCondition=(self.df[balaceDict['liquidationValue']]>0)
        return expectEarnTrans(self.df,self.filterCondition)



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
    def __init__(self,cash,dividendRatio,today):
        self.cash=cash
        self.dividendRatio=dividendRatio
        self.todayPrice=today.todayPrice()
    def expectEarn(self):
        self.df=pd.DataFrame({})
        self.df[cashDict['latestYield']]=(self.cash.latestCash().iloc[-1]/self.todayPrice)
        self.df[cashDict['avgYield']]=(self.cash.avgCash(5).iloc[-1]/self.todayPrice)
        self.df[cashDict['minCash']]=self.cash.minCash(5).iloc[-1]
        self.df[cashDict['avgDividendRatio']]=self.dividendRatio.avgDividendRatio(5).iloc[-1]
        self.df[cashDict['expectEarn']]=(self.cash.avgCash(5).iloc[-1]/0.05/self.todayPrice-1)
        self.filterCondition=(self.df[cashDict['latestYield']]>0.05)&(self.df[cashDict['avgYield']]>0.05)&(self.df[cashDict['minCash']]>0)&(self.df[cashDict['avgDividendRatio']]>50)
        return expectEarnTrans(self.df,self.filterCondition)

# 慶龍林區成長股策略
# 近3個月營收年增率都大於30%
# 連續4季的eps都大於0
# 本益比10倍買進(沒設)
# 本益比15倍賣出
# 不要營建股

class LynchInvest:
    def __init__(self,today,revenue,seasonEps,baseInfo):
        self.todayPrice=today.todayPrice()
        self.revenue=revenue
        self.seasonEps=seasonEps
        self.baseInfo=baseInfo
    def expectEarn(self):
        self.df=pd.DataFrame({})
        self.df[lynchDict['minGrowth']]=self.revenue.minGrowth(12,3).iloc[-1]
        self.df[lynchDict['minEps']]=self.seasonEps.minEps(4).iloc[-1]
        self.df[lynchDict['industry']]=self.baseInfo.industry()
        self.df[lynchDict['expectEarn']]=self.seasonEps.sumEps(4).iloc[-1]*15/self.todayPrice
        self.filterCondition=(self.df[lynchDict['minGrowth']]>0.3)&(self.df[lynchDict['minEps']]>0)&(self.df[lynchDict['industry']]!='建材營造業')
        return expectEarnTrans(self.df,self.filterCondition)

# 林區巴菲特選股
# 近4季ROE在20%以上
# 近4季EPS本益比在10以下(沒設)
# 近4季皆有獲利  

class Buffett:
    def __init__(self,today,seasonRoe,seasonEps,dividendRatio):
        self.today=today
        self.seasonRoe=seasonRoe
        self.seasonEps=seasonEps
        self.dividendRatio=dividendRatio
        self.innerGrowth=InnerGrowth(self.dividendRatio,self.seasonRoe)
    def expectEarn(self):
        self.df=pd.DataFrame({})
        self.df[roeEpsList[0]]=self.seasonRoe.seasonRoeTrans.loc[roeEpsList[0]]
        self.df[roeEpsList[1]]=self.seasonRoe.seasonRoeTrans.loc[roeEpsList[1]]
        self.df[lynchDict['dividendRatio']]=self.dividendRatio.dividendRatioTrans.iloc[-1]
        self.df[lynchDict['minEps']]=self.seasonEps.minEps(4).iloc[-1]
        self.df[lynchDict['expectEarn']]=self.innerGrowth.getInnerGrowth()*self.df[roeEpsList[1]]/self.today.todayPrice()-1
        self.filterCondition=(self.df[roeEpsList[0]]>20)&(self.df[lynchDict['minEps']]>0)
        return expectEarnTrans(self.df,self.filterCondition)

# be true 成長股策略
# 近3個月營收年增率都大於0%
# 連續4計的eps都大於0
# 最小年增率乘以50當成本益比賣出
# 不要營建股

class BeTrue:
    def __init__(self,today,liquidationInvest,revenue,seasonRoe):
        self.today=today
        self.liquidationInvest=liquidationInvest
        self.revenue=revenue
        self.seasonRoe=seasonRoe
    def expectEarn(self):
        self.df=pd.DataFrame({})
        self.df[balaceDict['liquidationValue']]=self.liquidationInvest.getLiquidation()
        self.df[roeEpsList[1]]=self.seasonRoe.seasonRoeTrans.loc[roeEpsList[1]]
        self.df[lynchDict['minGrowth']]=self.revenue.minGrowth(12,3).iloc[-1]
        return self.df