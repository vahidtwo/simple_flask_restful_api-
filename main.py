from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)


@app.route('/test')
def hello():
    return 'hello im running'


from post import post_blueprint

app.register_blueprint(post_blueprint)
if __name__ == '__main__':
    app.run('127.0.0.1', 3000)
