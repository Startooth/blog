from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import redirect


from libs.orm import db
from user.views import user_bp
from article.views import article_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wizard:123@localhost:3306/Blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


app.register_blueprint(user_bp)
app.register_blueprint(article_bp)
app.secret_key = r'dsaf^%*E^%d84%#%*(&^)(*goERXr9&*T)(UGH9-ua'


@app.route('/')
def home():
    return redirect('/user/login')

if __name__ == "__main__":
    manager.run()
