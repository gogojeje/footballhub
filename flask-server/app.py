from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_cors import CORS
import oracledb
from routes import index, schedule, signup, login, logout, teams, schedule_and_teams

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})
app.secret_key = "your_secret_key_here"

# Oracle DB 연결 설정
dsn = oracledb.makedsn(host='localhost', port=1521, service_name='xepdb1')
connection = oracledb.connect(user='ace01', password='me', dsn=dsn)
cursor = connection.cursor()

app.register_blueprint(index)
app.register_blueprint(schedule)
app.register_blueprint(signup)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(teams)
app.register_blueprint(schedule_and_teams)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)