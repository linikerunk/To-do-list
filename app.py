import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/todolist.sqlite3'

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, completed):
        self.title = title
        self.completed = completed


@app.route("/")
def home():
    return "Hello, Flask!"
    

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)