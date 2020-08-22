from libs.orm import db


class User(db.Model):
    ''' 初始化用户信息表 '''
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Enum('男','女','保密'), default='保密')
    phone = db.Column(db.String(16), unique=True, nullable=False)
    photo = db.Column(db.Boolean,default=False)
