from . import signup
from flask import render_template
from flask import request  # request 모듈을 가져옵니다.
from app import connection  # app.py에서 정의한 connection을 가져옵니다.

@signup.route("/api/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        userid = request.json.get("userid")
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        gender = request.json.get("gender")
        age = int(request.json.get("age"))
        location = request.json.get("location")

        try:
            cursor = connection.cursor()
            # PL/SQL 프로시저를 호출하여 새 회원 생성
            cursor.callproc("members_pkg.create_member", [userid, username, email, password, gender, age, location])
            connection.commit()
            cursor.close()

            return "Signup successful!"
        except Exception as e:
            return "Signup failed. Error: " + str(e)

    return render_template("signup.html")
