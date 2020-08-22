import datetime

from flask import Blueprint
from flask import request
from flask import redirect
from flask import render_template
from flask import session

from article.models import Article
from user.models import User
from libs.orm import db


article_bp = Blueprint('article', __name__, url_prefix='/article')
article_bp.template_folder = './templates'

@article_bp.route('/index')
def index():
    '''blog主页'''
    user = User.query.filter_by(username=session['username']).count()
    if user != 0:
        articles = Article.query.order_by(Article.date.desc()).all()
        return render_template('home.html',articles=articles)
    else:
        return render_template('response.html', msg='请先登录！')

@article_bp.route('/post',methods=('POST','GET'))
def post():
    '''写文章'''
    user = User.query.filter_by(username=session['username']).count()
    if user != 0:
        username = session['username']

        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            now = datetime.datetime.now()
            date = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')

            article = Article(username=username,title=title,content=content,date=date)
            db.session.add(article)
            db.session.commit()
            return redirect('/article/index')
        else:
            return render_template('post.html')
    else:
        return render_template('response.html', msg='请先登录！')

@article_bp.route('/read')
def read():
    '''查看文章'''
    user = User.query.filter_by(username=session['username']).count()
    if user != 0:
        aid = request.args.get('aid')
        article = Article.query.get(aid)
        return render_template('read.html',article=article)
    else:
        return render_template('response.html', msg='请先登录！')

@article_bp.route('/delete')
def delete():
    '''删除文章'''
    aid = request.args.get('aid')
    Article.query.filter_by(id=aid).delete()
    db.session.commit()
    return redirect('/article/index')
