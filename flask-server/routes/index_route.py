from . import index
from flask import render_template
from app import connection  # app.py에서 정의한 connection을 가져옵니다.
import oracledb


@index.route('/')
def index():
    try:
        cursor = connection.cursor()

        # PL/SQL 프로시저를 호출하여 팀 목록을 가져옴
        plsql_query = """
        DECLARE
            p_team_cursor SYS_REFCURSOR;
        BEGIN
            teams_pkg.read_team(p_team_id => NULL, p_result => p_team_cursor);
            :result := p_team_cursor;
        END;
        """
        result = cursor.var(oracledb.CURSOR)
        cursor.execute(plsql_query, result=result)
        teams_result = result.getvalue().fetchall()

        cursor.close()

        teams_list = [row[1] for row in teams_result]

        return render_template("index.html", teams=teams_list)
    except Exception as e:
        return "Error: " + str(e)