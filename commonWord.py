commonDict={
    'latestAvg':'近期平均',
    'conditionCount':'符合個數',
    'dataId':'代號',
    'dataName':'名稱',
    'price':'成交'
}
cashDict={
    'avgDividendRatio':'平均股息發放率',
    'avgDividend':'平均股息',
    'cashCount':'發放股息次數',
    'latestYield':'近一年股息殖利率',
    'avgYield':'平均股息殖利率'
}

removeStr=[',','=','"']
keyList=[commonDict['dataId'],commonDict['dataName']]
todayPriceColumn=[commonDict['price']]
starkList=['latestYield','avgYield']

def dictList(dict,keyList):
    return [dict[key] for key in keyList]

