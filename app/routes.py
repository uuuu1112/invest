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
    query={}
    query['descrip']=investDescrip
    return render_template('invest.html', invest_options=InvestDict,query=query)

@bp.route('/dcfModel')
def dcfModel():
    query={}
    query['descrip']=dcfDescrip
    query['maxValue']=str(0.4)
    return render_template('dcfModel.html',cash_option=cashListDict,growth_option=growthDict,query=query)

@bp.route('/form')
def form():
    query={}
    query['selected_option']=request.args.get('selected_option')
    # query['descrip']=integrateInvest(query['selected_option'])['descrip']
    # api_response=integrateInvest(query['selected_option'])['table']
    # query['table_html']=api_response.to_html(classes='table table-bordered', index=False)
    # return render_template('invest.html', invest_options=InvestDict, query=query)
    return query
@bp.route('/dcfForm')
def dcfForm():
    query={}
    query['selectCash']=request.args.get('cash_option')
    query['selectGrowth']=request.args.get('growth_option')
    query['maxValue']=request.args.get('maxValue')
    query['withLiquidation']=request.args.get('checkbox')
    query['descrip']=getPridictValue(query['selectCash'],query['selectGrowth'])['descrip']
    api_response=getPridictValue(query['selectCash'],query['selectGrowth'],float(query['maxValue']),query['withLiquidation'])['table']
    query['table_html']=api_response.to_html(classes='table table-bordered', index=False)
    return render_template('dcfModel.html',cash_option=cashListDict,growth_option=growthDict,query=query)
    # return query
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