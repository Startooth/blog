from libs.orm import db

class Article(db.Model):
    '''初始化article表'''
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
