from static import *
from base import Cash,DividendRatio,Today

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
    def __init__(self,Cash,DividendRatio,Today):
        self.cash=Cash()
        self.dividendRatio=DividendRatio()
        self.todayPrice=Today().todayPrice
    def expectEarn(self):
        self.df=pd.DataFrame({})
        self.df[cashDict['latestYield']]=(self.cash.latestCash()/self.todayPrice)
        self.df[cashDict['avgYield']]=(self.cash.avgCash(5)/self.todayPrice)
        self.df[cashDict['minCash']]=self.cash.minCash(5)
        self.df[cashDict['avgDividendRatio']]=self.dividendRatio.avgDividendRatio(5)
        self.df[cashDict['expectEarn']]=(self.cash.avgCash(5)/0.05/self.todayPrice-1)
        self.filterCondition=(self.df[cashDict['latestYield']]>0.05)&(self.df[cashDict['avgYield']]>0.05)&(self.df[cashDict['minCash']]>0)&(self.df[cashDict['avgDividendRatio']]>50)
        self.df=self.df[self.filterCondition]
        self.df=self.df.sort_values(by=cashDict['expectEarn'],ascending=False)
        self.df[cashDict['expectEarn']]=self.df[cashDict['expectEarn']].apply(lambda x: f'{x*100:.2f}%')
        return self.df