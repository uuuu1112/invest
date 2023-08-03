from static import *

pbr=pd.read_csv('goodinfo/pbr.csv')
baseInfo=pd.read_csv('goodinfo/baseInfo.csv')

todayPrice=baseDfTrans(pbr)[commonDict['price']]
industry=baseDfTrans(baseInfo)[commonDict['industry']]