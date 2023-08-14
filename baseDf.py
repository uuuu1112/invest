import pandas as pd
import numpy as np
from commonWord import *

def baseDfTrans(df):
    df=df.replace(removeStr,'',regex=True)
    df=df.set_index(keyList)
    return df

# 定義一個函數來處理欄位名稱的轉換
def replace_column_names(column_name,transList=transList,transWord='M'):
    columnName=column_name
    for word in transList:
        columnName=columnName.replace(word,transWord)
    return columnName

def revenueDfTrans(df):
    df=baseDfTrans(df)
    df.columns = df.columns.map(replace_column_names)
    return df.apply(pd.to_numeric, errors='coerce')

def concatDf(dfList):
    return pd.concat(dfList,axis=1)

def shareTable(shareData,columns,filterFunction,sortValue):
    filterCondition=filterFunction(shareData)
    filterDf=shareData[filterCondition]
    filterDf=filterDf[columns]
    filterDf=filterDf.sort_values(by=sortValue,ascending=False)
    return filterDf

def dictList(dict,keyList):
    return [dict[key] for key in keyList]

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