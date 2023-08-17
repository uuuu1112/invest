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
    'industry':'產業別'
}
cashDict={
    'avgDividendRatio':'平均股息發放率',
    'avgDividend':'平均股息',
    'latestYield':'近一年股息殖利率',
    'avgYield':'5年平均股息殖利率',
    'minCash':'5年最低股息',
    'expectEarn':commonDict['expectEarn'],
}
lynchDict={
    'expectEarn':commonDict['expectEarn'],
    'per':'PER',
    'price':commonDict['price'],
    'industry':commonDict['industry'],
    'minGrowth':'最小年增率',
    'minEps':'最小EPS',
    'dividendRatio':'盈餘配發率',
    'priceGoal':commonDict['priceGoal'],
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

baseDropRows=['成交','排名','漲跌價','漲跌幅']
monthDrop=['\xa0平均\xa0營收(億)','\xa0合計\xa0營收(億)']

removeStr=[',','=','"']
keyList=['代號','名稱']
roeEpsList=['ROE(%)','EPS(元)']




