import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Steven Delaney in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect('postgres://database_lom7_user:TTJFJYzStJQEE0FaHwisqNn7FUDEWUzC@dpg-co1mhpq0si5c73cov4n0-a.oregon-postgres.render.com/database_lom7')
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def create():
    cconn = psycopg2.connect('postgres://database_lom7_user:TTJFJYzStJQEE0FaHwisqNn7FUDEWUzC@dpg-co1mhpq0si5c73cov4n0-a.oregon-postgres.render.com/database_lom7')
    conn.close()
    return 'db_create connection successful'
