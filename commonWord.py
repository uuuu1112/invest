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
    'cagrMin':'股息年成長率'
}
lynchDict={
    # 'revenueGrowthOver30':'營收年增率超過30%',
    # 'epsOver0':'eps大於0次數',
    'expectEarn':commonDict['expectEarn'],
    'per':'PER',
    'price':commonDict['price'],
    'industry':commonDict['industry'],
    'minGrowth':'最小年增率',
    'minEps':'最小EPS',
    'expectGrowthEarn':'預期成長估值報酬率',
    'innerGrowthEarn':'內部成長估值報酬率',
    'dividendRatio':'盈餘配發率',
    'priceGoal':commonDict['priceGoal'],
}
balaceDict={
    'debt':'負債總額(%)',
    'stock':'存貨(%)',
    'receive':'應收帳款(%)',
    'invest':'投資(%)',
    'liquidationValue':'清算價值',
    'liquidEarn':'清算價值報酬率'
}
baseDropRows=['成交','排名','漲跌價','漲跌幅']
monthDrop=['\xa0平均\xa0營收(億)','\xa0合計\xa0營收(億)']

removeStr=[',','=','"']
keyList=['代號','名稱']
todayPricePerColumn=['成交','PER']
todayPricePbrColumn=['成交','PBR','PER']
roeEpsList=['ROE(%)','EPS(元)']
transList=['21M','22M','23M']

starkList=['latestYield','avgYield']
longLIst=['latestYield','avgYield','expectEarn']
beTrueCashList=['avgYield','latestYield','expectEarn']

lynchList=['expectEarn']
beTrueGrowthList=['expectGrowthEarn']
buffettList=['innerGrowthEarn']

deductList=['debt','stock','receive','invest']
liquidationModelList=['liquidEarn']



