from static import *

pbr=pd.read_csv('goodinfo/pbr.csv')
todayPrice=baseDfTrans(pbr)[todayPriceColumn]