from base import *

month=pd.read_csv('goodinfo/month/month.csv')
monthBefore=pd.read_csv('goodinfo/month/monthBefore.csv')

def revenueGrowth(month,monthBefore):
    revenue=baseDfTrans(month).apply(pd.to_numeric, errors='coerce')
    revenueBefore=baseDfTrans(monthBefore).apply(pd.to_numeric, errors='coerce')
    result=revenue.iloc[:,-3]/revenueBefore.iloc[:,-3]-1
    return result