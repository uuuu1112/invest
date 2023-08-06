from base import *

balance=pd.read_csv('goodinfo/last4Season/balance.csv')

todayPBR=baseDfTrans(pbr)[todayPricePbrColumn]
deduct=baseDfTrans(balance)[dictList(balaceDict,deductList)].fillna(0)
# 這是主要的df
liquiShareBaseDf=concatDf([todayPBR,deduct])


# 清算價值=總資產-()-()
# (短期負債 長期負債)
# (存貨 應收帳款 長期投資)