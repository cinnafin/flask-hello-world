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
    conn = psycopg2.connect('postgres://database_lom7_user:TTJFJYzStJQEE0FaHwisqNn7FUDEWUzC@dpg-co1mhpq0si5c73cov4n0-a.oregon-postgres.render.com/database_lom7')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit
    conn.close()
    return 'Basketball Table Successfully Created'

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect('postgres://database_lom7_user:TTJFJYzStJQEE0FaHwisqNn7FUDEWUzC@dpg-co1mhpq0si5c73cov4n0-a.oregon-postgres.render.com/database_lom7')
    cur = conn.cursor()
    cur.execute(''' 
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Populated'

@app.route('/db_select')
def select():
    conn = psycopg2.connect('postgres://database_lom7_user:TTJFJYzStJQEE0FaHwisqNn7FUDEWUzC@dpg-co1mhpq0si5c73cov4n0-a.oregon-postgres.render.com/database_lom7')
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string
