from datetime import datetime,timedelta

today=datetime.today().strftime('%Y-%m-%d')
current_date=datetime.today().date()

# 將日期字符串轉換為 datetime 格式
def datetime_obj(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d')

# n年前的今日
def n_years_ago(n=10,current_date=current_date):
    n_years_ago=current_date-timedelta(days=365*n)
    formatted_date=n_years_ago.strftime('%Y-%m-%d')
    return formatted_date

# n個月前的今日
def get_previous_month_date(date_string, n):
    date_format = '%Y-%m-%d'

    # 將輸入的日期轉換為 datetime 格式
    current_date = datetime.strptime(date_string, date_format)

    # 計算前 n 個月的日期
    previous_month_date = current_date - timedelta(days=current_date.day)
    for _ in range(n-1):
        year = previous_month_date.year
        month = previous_month_date.month
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
        previous_month_date = datetime(year, month, 1)

    return previous_month_date.strftime(date_format)

# 最新月營收日期
def latestRevenueDate(current_date=current_date):
    # 如果當前日期在15日之前，則財報月份為上個月
    if current_date.day <= 15:
        latest_financial_month = datetime(current_date.year, current_date.month - 1, 1)
    else:
        # 如果當前日期在15日之後，則財報月份為當前月份
        latest_financial_month = current_date
    return latest_financial_month.strftime('%Y-%m-01')

# class HandleMonth:
#     def __init__(self,current_date=current_date):
#         self.current_date=current_date