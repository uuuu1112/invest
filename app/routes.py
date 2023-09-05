from flask import Blueprint,render_template,request
from app.models import *
import requests


bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')
@bp.route('/contact')
def contact():
    return render_template('contact.html')
@bp.route('/invest')
def invest():
    return render_template('invest.html', invest_options=InvestDict)

@bp.route('/form')
def form():
    selected_option=request.args.get('selected_option')
    descrip=integrateInvest(selected_option)['descrip']
    api_response=integrateInvest(selected_option)['table']
    table_html=api_response.to_html(classes='table table-bordered', index=False)

    return render_template('invest.html', invest_options=InvestDict, table_html=table_html,descrip=descrip)


# @bp.route('/allInvest/<selectValue>')
# def allInvest(selectValue):
#     return integrateInvest(selectValue)

# @bp.route('/liquidation')
# def liquidation():
#     seasonBalance=SeasonBalance()
#     liquidationInvest=LiquidationInvest(seasonBalance)
#     return liquidationInvest.expectEarnApi()

# @bp.route('/cashInvest')
# def cashInvest():
#     cashList=CashList()
#     cashInvest=CashInvest(cashList,dividendRatio)
#     return cashInvest.expectEarnApi()

# @bp.route('/lynchInvest')
# def lynchInvest():
#     revenue=Revenue()
#     shortRevenueGrowth=ShortRevenueGrowth(revenue)
#     baseInfo=BaseInfo()
#     lynchInvest=LynchInvest(seasonEpsList,baseInfo,shortRevenueGrowth)
#     return lynchInvest.expectEarnApi()

# @bp.route('/buffettInvest')
# def buffettInvest():
#     seasonRoe=SeasonRoe()
#     buffettInvest=BuffettInvest(seasonRoe,seasonEpsList,dividendRatio)
#     return buffettInvest.expectEarnApi()