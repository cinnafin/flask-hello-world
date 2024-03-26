import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Steven Delaney in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect(postgres://hello_world_sql_user:ACR2qSqGQ68g5SkMzrPQhMIr2kfA9ccy@dpg-co1luc6v3ddc7385e9t0-a/hello_world_sql)
    conn.close()
    return "Database Connection Successful"
