from flask import Flask
from database import db
from api import api

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///salaries.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
