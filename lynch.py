from static import *
from base import SeasonEps,BaseInfo,Revenue,Today,SeasonRoe,DividendRatio
from growth import InnerGrowth

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
    def expectEarn(self):
        self.df=pd.DataFrame({})
        self.df[roeEpsList[0]]=self.seasonRoe.seasonRoeTrans.loc[roeEpsList[0]]
        self.df[roeEpsList[1]]=self.seasonRoe.seasonRoeTrans.loc[roeEpsList[1]]
        self.df[lynchDict['dividendRatio']]=self.dividendRatio.dividendRatioTrans.iloc[-1]
        self.df[lynchDict['minEps']]=self.seasonEps.minEps(4).iloc[-1]
        self.df[lynchDict['expectEarn']]=InnerGrowth(self.dividendRatio,self.seasonRoe).getInnerGrowth()*self.df[roeEpsList[1]]/self.today.todayPrice()-1
        self.filterCondition=(self.df[roeEpsList[0]]>20)&(self.df[lynchDict['minEps']]>0)
        return expectEarnTrans(self.df,self.filterCondition)

# be true 成長股策略
# 近3個月營收年增率都大於0%
# 連續4計的eps都大於0
# 最小年增率乘以50當成本益比賣出
# 不要營建股