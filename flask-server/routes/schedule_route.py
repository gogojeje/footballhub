from . import schedule
from app import connection  # app.py에서 정의한 connection을 가져옵니다.
import oracledb
from flask import jsonify

@schedule.route("/api/schedule", methods=["GET"])
def get_schedule():
    try:
        cursor = connection.cursor()

        result_cursor = cursor.var(oracledb.CURSOR)
        cursor.callproc('matchschedule_pkg.read_all_matchschedule', (result_cursor,))

        result = result_cursor.getvalue()
        cursor.close()

        schedule_data = []
        for row in result:
            schedule_data.append({
                "roundnumber": row[1],
                "Date": row[2],
                "time": row[3],
                "leagueortournament": row[4],
                "hometeam": row[8],
                "awayteam": row[9]
            })

        return jsonify({"data": schedule_data})
    except Exception as e:
        return jsonify({"error": str(e)})