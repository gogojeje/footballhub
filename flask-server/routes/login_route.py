from . import login
from flask import render_template, session, request
from app import connection  # app.py에서 정의한 connection을 가져옵니다.
import oracledb

@login.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.json
        userid = data.get("userid")
        password = data.get("password")

        cursor = connection.cursor()

        plsql_query = """
        DECLARE
            v_result NUMBER;
        BEGIN
            v_result := members_pkg.validate_login(p_userid => :userid, p_password => :password);
            :result := v_result;
        END;
        """
        result = cursor.var(int)
        cursor.execute(plsql_query, userid=userid, password=password, result=result)

        if result.getvalue() == 1:
            session["userid"] = userid
            return "Login successful"
        else:
            return "Login failed. Invalid userid or password."
    except Exception as e:
        return "Login failed. Error: " + str(e)
    finally:
        cursor.close()
