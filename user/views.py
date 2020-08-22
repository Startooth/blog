from flask import Blueprint
from flask import request
from flask import render_template
from flask import session
from flask import redirect

from user.models import User
from libs.orm import db


user_bp = Blueprint('user',__name__,url_prefix='/user')
user_bp.template_folder = './templates'


@user_bp.route('/register',methods=('POST','GET'))
def register():
    '''注册'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        pwd = request.form.get('pwd')
        gender = request.form.get('gender')
        phone = request.form.get('phone')

        if pwd != password:
            return render_template('response.html', msg='两次输入密码不同！')
        if User.query.filter_by(username=username):
            render_template('response.html', msg='用户名已存在！')
    
        new_id = User(username=username,password=password,gender=gender,phone=phone)
        db.session.add(new_id)
        db.session.commit()
        return render_template('response.html', msg='注册成功！')
    else:
        return render_template('register.html')


@user_bp.route('/login',methods=('POST','GET'))
def login():
    '''登陆'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        num = User.query.filter_by(username=username).count()
        if num == 0:
            return render_template('response.html', msg='用户名不存在！')
        user = User.query.filter_by(username=username).one()
        if user.password != password:
            return render_template('response.html', msg='用户名密码错误！')

        # session记录username
        session['username'] = username
        # return render_template('home.html')
        return redirect('/article/index')
            
    else:
        return render_template('login.html')


@user_bp.route('/info')
def info():
    '''用户信息'''
    user = User.query.filter_by(username=session['username']).count()
    if user != 0:
        user = User.query.filter_by(username=session['username']).one()
        return render_template('info.html',user=user)
    else:
        return render_template('response.html',msg='请先登录！')


@user_bp.route('/')
def home():
    return redirect('/user/login')

