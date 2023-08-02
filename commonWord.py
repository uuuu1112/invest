commonDict={
    'latestAvg':'近期平均',
    'conditionCount':'符合個數',
    'dataId':'代號',
    'dataName':'名稱',
    'price':'成交',
    'priceGoal':'目標價',
    'expectEarn':'預期報酬率',
    'cagr':'年CAGR'
}
cashDict={
    'avgDividendRatio':'平均股息發放率',
    'avgDividend':'平均股息',
    'cashCount':'發放股息次數',
    'latestYield':'近一年股息殖利率',
    'avgYield':'5年平均股息殖利率',
    'expectEarn':commonDict['expectEarn'],
    'cagr10':'10年CAGR',
    'cagr5':'5年CAGR',
    'cagr3':'3年CAGR',
    'dcfexpectEarn':'DCF預期報酬率',
    'cagrMin':'股息年成長率'
}
lynchDict={
    'revenueGrowthOver30':'營收年增率超過30%',
    'epsOver0':'eps大於0次數',
    'expectEarn':commonDict['expectEarn'],
    'per':'PER',
    'price':commonDict['price']
}

removeStr=[',','=','"']
keyList=['代號','名稱']
todayPriceColumn=['成交']
todayPricePerColumn=['成交','PER']
transList=['21M','22M','23M']

starkList=['latestYield','avgYield']
longLIst=['latestYield','avgYield','expectEarn']
beTrueCashList=['avgYield','latestYield','cagr10','cagr5','cagr3','expectEarn','dcfexpectEarn']

lynchList=['expectEarn']



