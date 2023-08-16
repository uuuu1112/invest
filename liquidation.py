from static import *
from base import Today,SeasonBalance

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

