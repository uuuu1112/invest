import pandas as pd
import numpy as np
import os
from app.commonWord import *
pd.set_option('display.float_format', '{:.2f}'.format)

class BaseTrans:
    def baseDf(self,csvData):
        csvData=csvData.astype(str)
        csvData=csvData.replace(removeStr,'',regex=True)
        csvData=csvData.set_index(keyList)
        csvData=csvData.apply(lambda s:pd.to_numeric(s,errors='coerce'))
        return csvData
    def transDf(self,csvData):
        return self.baseDf(csvData).transpose()
    def dropRows(self,csvData,dropRows):
        return self.transDf(csvData).drop(index=dropRows)
    def baseTrans(self,csvData):
        csvData=csvData.replace(removeStr,'',regex=True)
        csvData=csvData.set_index(keyList)
        return csvData.transpose()
    
def expectEarnTrans(df,filterCondition=""):
    if len(filterCondition)>0:
        df=df[filterCondition].copy()
    df.loc[:,commonDict['expectEarn']]=df[commonDict['priceGoal']]/df[commonDict['price']]-1
    df=df.sort_values(by=cashDict['expectEarn'],ascending=False)
    df.loc[:,cashDict['expectEarn']]=df[commonDict['expectEarn']].apply(lambda x: f'{x*100:.1f}%')
    return df

def transToApi(dfWithIndex):
    df=dfWithIndex.reset_index()
    df_json =df.to_json(orient='records')
    return df_json 