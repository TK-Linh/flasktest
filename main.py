from flask import Flask, render_template, request, jsonify
import pypyodbc as odbc

app = Flask(__name__)

driver_name = 'SQL SERVER'
server_name = 'DESKTOP-9TFKPMA\SQLEXPRESS'
database_name = 'PROJECT'

connection_string = f"""
    driver={{{driver_name}}};
    server={server_name};
    database={database_name};
    Trust_Connection=yes;
"""
conn = odbc.connect(connection_string)
cursor = conn.cursor()

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.post("/signin")
def signin():
    exist_account = request.get_json()
    query = f"select pass from accounts where email = '{exist_account['username']}'"
    cursor.execute(query)

    result = cursor.fetchone()[0]

    if exist_account['password'] == result:
        print('success')
        print('success')
        return {'mess': "success"}

    else:
        return{'mess': "Try again"}
    

    