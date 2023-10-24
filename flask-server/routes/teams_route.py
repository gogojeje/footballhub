from . import teams
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from app import connection  # app.py에서 정의한 connection을 가져옵니다.
cursor = connection.cursor()

@teams.route('/api/teams/', methods=['GET'])
def get_teams():    
    try:
        query = "SELECT id, name, league FROM teams"
        cursor.execute(query)
        teams = []
        for row in cursor:
            team = {
                'id': row[0],
                'name': row[1],
                'league': row[2]
            }
            teams.append(team)
        return jsonify(teams)
    except Exception as e:
        return jsonify({'error': str(e)})