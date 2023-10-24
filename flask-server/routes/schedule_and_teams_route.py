from . import schedule_and_teams
from flask import jsonify
from app import connection  # app.py에서 정의한 connection을 가져옵니다.
cursor = connection.cursor()

@schedule_and_teams.route('/api/get_schedule_and_teams', methods=['GET'])
def get_schedule_and_teams():
    cursor.execute("SELECT * FROM matchschedule")
    matches = cursor.fetchall()

    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()

    return jsonify({"matches": matches, "teams": teams})