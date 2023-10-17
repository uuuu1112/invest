import pandas as pd
import numpy as np

# import re
from app.commonWord import *
pd.set_option('display.float_format', '{:.2f}'.format)

class BaseTrans:
    def baseDf(self,csvData,removeColumns=removeColumns):
        csvData=csvData.astype(str)
        csvData.columns = csvData.columns.str.replace(removeColumns, '', regex=True)
        csvData=csvData.replace(removeStr,'',regex=True)
        csvData=csvData.set_index(keyList)
        csvData=csvData.apply(lambda s:pd.to_numeric(s,errors='coerce'))
        return csvData
    def transDf(self,csvData,removeColumns=removeColumns):
        return self.baseDf(csvData,removeColumns).transpose()
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
    df.loc[:,cashDict['expectEarn']]=df[commonDict['expectEarn']].apply(lambda x: f'{x*100:.2f}%')
    return df

def transToApi(dfWithIndex):
    df=dfWithIndex.reset_index()
    df_json =df.to_json(orient='records')
    return df_json 

def safe_loc(df, rows_to_select):
    # 检查 rows_to_select 中哪些行标签在 DataFrame 的索引中存在
    valid_rows = [label for label in rows_to_select if label in df.index]

    # 使用 .loc 选择存在于索引中的行
    selected_data = df.loc[valid_rows, :]

    return selected_data