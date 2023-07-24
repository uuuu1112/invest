from date import *
import requests
import pandas as pd
import copy

url="https://api.finmindtrade.com/api/v4/data"
parameter = {
    "dataset":"",
    "start_date": "",
    "token": "", # 參考登入，獲取金鑰
}

class BaseParam:
    def __init__(self,token=''):
        self.token=token

class StockPrice(BaseParam):
    def __init__(self,data_id='2330',start_date=n_years_ago(10),end_date=today, token=''):
        super().__init__(token)
        self.param=copy.copy(parameter)
        self.param['dataset']='TaiwanStockPrice'
        self.param['data_id']=data_id
        self.param['start_date']=start_date
        self.param['end_date']=end_date
        self.param['token']=token
        self.url=copy.copy(url)
    # 預設拿10年股價
    def getStockPrice(self):
        resp=requests.get(self.url,params=self.param)
        data=resp.json()
        data=pd.DataFrame(data["data"])
        return data

class MonthRevenue(BaseParam):
    def __init__(self,data_id='2330',current_date=current_date,n=10, token=''):
        super().__init__(token)
        self.param=copy.copy(parameter)
        self.param['dataset']='TaiwanStockMonthRevenue'
        self.param['data_id']=data_id
        self.param['start_date']=get_previous_month_date(latestRevenueDate(current_date),n*12-1) 
        self.param['token']=token
        self.url=copy.copy(url)
    def getMonthRevenue(self):
        resp=requests.get(self.url,params=self.param)
        data=resp.json()
        data=pd.DataFrame(data["data"])
        return data