from flask import Blueprint,render_template,request,session,redirect,url_for
from app.models import *
import requests

bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        # 假设这里进行了用户身份验证，验证通过后将用户名存储在会话中
        session['email'] = email
        return redirect(url_for('routes.profile'))
    return render_template('login.html')

# 用户个人资料页面
@bp.route('/profile')
def profile():
    # 从会话中获取用户名
    email = session.get('email', None)
    if email is None:
        return redirect(url_for('routes.login'))
    return render_template('profile.html', email=email) 

# 登出
@bp.route('/logout')
def logout():
    # 从会话中移除用户名
    session.pop('email', None)
    return redirect(url_for('login'))

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
    query['descrip']=integrateInvest(query['selected_option'])['descrip']
    api_response=integrateInvest(query['selected_option'])['table']
    query['table_html']=api_response.to_html(classes='table table-bordered', index=False)
    return render_template('invest.html', invest_options=InvestDict, query=query)
    # return query
@bp.route('/dcfForm')
def dcfForm():
    query={}
    query['selectCash']=request.args.get('cash_option')
    query['selectGrowth']=request.args.get('growth_option')
    query['maxValue']=request.args.get('maxValue')
    query['withLiquidation']=request.args.get('checkbox')
    query['loseExtra']=request.args.get('checkbox1')
    predictValue=getPridictValue(query['selectCash'],query['selectGrowth'],float(query['maxValue']),query['withLiquidation'],query['loseExtra'])
    query['descrip']=predictValue['descrip']
    api_response=predictValue['table']
    query['table_html']=api_response.to_html(classes='table table-bordered', index=False)
    return render_template('dcfModel.html',cash_option=cashListDict,growth_option=growthDict,query=query)

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