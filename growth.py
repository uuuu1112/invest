from static import *
from base import stockYoYcsv,month,monthBefore

stockYoY=baseDfTrans(stockYoYcsv)

revenueGrowthCount=revenueGrowthNum(month,monthBefore,lynchDict['revenueGrowthOver30'])
minGrowth=revenueGrowthMin(month,monthBefore,lynchDict['minGrowth'])