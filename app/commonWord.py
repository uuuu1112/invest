dataPath='../data'
commonDict={
    'latestAvg':'近期平均',
    'conditionCount':'符合個數',
    'dataId':'代號',
    'dataName':'名稱',
    'price':'成交',
    'priceGoal':'目標價',
    'expectEarn':'預期報酬率',
    'cagr':'年CAGR',
    'industry':'產業別',
    'eps':'EPS(元)'
}
cashDict={
    'avgDividendRatio':'平均股息發放率(%)',
    'avgDividend':'平均股息',
    'latestYield':'近一年股息殖利率',
    'avgYield':'5年平均股息殖利率',
    'minCash':'5年最低股息',
    'expectEarn':commonDict['expectEarn'],
    'avgCash':'5年平均股息'
}
lynchDict={
    'expectEarn':commonDict['expectEarn'],
    'per':'PER',
    'price':commonDict['price'],
    'industry':commonDict['industry'],
    'minGrowth':'最小營收年增率',
    'minEps':'最小EPS',
    'dividendRatio':'盈餘配發率',
    'priceGoal':commonDict['priceGoal'],
    'innerGrowth':'內部成長率(%)',
}
balaceDict={
    'debt':'負債總額(%)',
    'stock':'存貨(%)',
    'receive':'應收帳款(%)',
    'invest':'投資(%)',
    'liquidationValue':'清算價值',
    'expectEarn':commonDict['expectEarn'],
    'price':commonDict['price'],
}
roeDict={
    'avgRoe':'平均ROE(%)',
    'roe':'ROE(%)',
}
shortGrowthDict={
    'mom':'營收MoM',
    'yoy':'營收YoY',
    'revenue3Growth':'3個月營收MoM',
    'revenue3YoY':'3個月營收YoY',
    'stockQoQ':'存貨QoQ',
    'stockYoY':'存貨YoY'
}
cagrDict={
    'year10Cagr':'CAGR(10年)',
    'year5Cagr':'CAGR(5年)',
    'year3Cagr':'CAGR(3年)',
    'minCagr':'CAGR(保守)'
}
cashDistDict={
    'cashDiscount':'股息折現',
    'avgInnerGrowth':'平均內部成長率',
    'beginCash':'起初EPS或股利',
    'expectGrowth':'預估成長率',
    'discount':'折現價值',
    'priceGoal':commonDict['priceGoal']
}
InvestDict={
    'LiquidationInvest':"1",
    'CashInvest':"2",
    'LynchInvest':"3",
    'BuffettInvest':"4"
}
cashListDict={
    "latest4SeasonEPS":"1",
    "avg5YearsEPS":"2",
    "latestCash":"3",
    "avg5YearsCash":"4"
}
growthDict={
    "innerGrowth":"1",
    "avg5InnerGrowth":"2",
    "year5CAGR":"3",
    "min3n5CAGR":"4",
    "revenue3MinYOY":"5"
}
investDescrip='''
策略簡述（點選後送出有詳細說明） ： <br>
清算價值投資法 ： 市價小於清算價值３０％買進，市價大於清算價值３０％賣出<br>
凡人說&慶龍存股策略 ： 當現金殖利率來到７％時買進 ，當現金殖利率來到５％時賣出<br>
慶龍林區成長股策略 ： 本益比10倍買進 本益比15倍賣出<br>
林區巴菲特選股 ： 市價到 ( 內部成長率(%)*EPS )賣出<br>
'''

dcfDescrip='''
<h3>現金流折現模型</h3>
第一個變數說明(起初的每股現金流) : 
近4季的EPS、近5年平均的EPS、最近的現金股息、近五年的現金股息<br>
第二個變數說明(未來5年的複合成長率預估) : 
最新的內部成長率、近5年平均的內部成長率、過去5年的複合成長率、過去3年5年的複合成長率取小的、過去3個月的年增率取小的<br>
模型說明 : 
假設未來5年的每股現金流是照第二個變數成長，後來是2%的成長，每年的每股現金流用10%折現到今天，把他們相加當成我的目標價
''' 

baseDropRows=['成交','排名','漲跌價','漲跌幅']
monthDrop=['\xa0平均\xa0營收(億)','\xa0合計\xa0營收(億)']

removeStr=[',','=','"']
keyList=['代號','名稱']




