from static import *

pbr=pd.read_csv('goodinfo/pbr.csv')
baseInfo=pd.read_csv('goodinfo/baseInfo.csv')
cash=pd.read_csv('goodinfo/year/cash.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')
balance=pd.read_csv('goodinfo/last4Season/balance.csv')
month=pd.read_csv('goodinfo/month/month.csv')
monthBefore=pd.read_csv('goodinfo/month/monthBefore.csv')
eps4Season=pd.read_csv('goodinfo/last4Season/eps.csv')
roe4Season=pd.read_csv('goodinfo/last4Season/roe.csv')
dividendRatio=pd.read_csv('goodinfo/year/dividendRatio.csv')
stockYoYcsv=pd.read_csv('goodinfo/last4Season/stockYoY.csv')

todayPrice=baseDfTrans(pbr)[commonDict['price']]
industry=baseDfTrans(baseInfo)[commonDict['industry']]