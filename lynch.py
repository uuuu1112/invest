from base import Revenue,SeasonEps,BaseInfo


# 慶龍林區成長股策略
# 近3個月營收年增率都大於30%
# 連續4計的eps都大於0
# 本益比10倍買進(沒設)
# 本益比15倍賣出
# 不要營建股

# 林區巴菲特選股
# 近4季ROE在20%以上
# 近4季EPS本益比在10以下(沒設)
# 近4季皆有獲利

# be true 成長股策略
# 近3個月營收年增率都大於0%
# 連續4計的eps都大於0
# 最小年增率乘以50當成本益比賣出
# 不要營建股

class Lynch:
    def __init__(self,Revenue,SeasonEps,BaseInfo):
        self.todayPrice=Today().todayPrice
    def expectEarn(self):
        self.df=pd.DataFrame({})
        return self.df