from flask import Blueprint,render_template
from app.models import *

seasonEpsList=SeasonEpsList()
dividendRatio=DividendRatio()

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return 'This is the about page'

@bp.route('/liquidation')
def liquidation():
    seasonBalance=SeasonBalance()
    liquidationInvest=LiquidationInvest(seasonBalance)
    return liquidationInvest.expectEarnApi()

@bp.route('/cashInvest')
def cashInvest():
    cashList=CashList()
    cashInvest=CashInvest(cashList,dividendRatio)
    return cashInvest.expectEarnApi()

@bp.route('/lynchInvest')
def lynchInvest():
    revenue=Revenue()
    shortRevenueGrowth=ShortRevenueGrowth(revenue)
    baseInfo=BaseInfo()
    lynchInvest=LynchInvest(seasonEpsList,baseInfo,shortRevenueGrowth)
    return lynchInvest.expectEarnApi()

@bp.route('/buffettInvest')
def buffettInvest():
    seasonRoe=SeasonRoe()
    buffettInvest=BuffettInvest(seasonRoe,seasonEpsList,dividendRatio)
    return buffettInvest.expectEarnApi()