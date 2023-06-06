import os
from time import sleep
from datetime import datetime
from flask import Flask, request, Response
import pymysql

# connect to db
connection = None
conn_attempts = 10
for i in range(conn_attempts):
    try:
        connection = pymysql.connect(host='mariadb',
                                    user=os.environ['MARIADB_USER'],
                                    password=os.environ['MARIADB_PASSWORD'],
                                    database=os.environ['MARIADB_DATABASE'],)
    except pymysql.err.OperationalError:
        print(f'Failed to connect to MariaDB (Attempt {i+1}/{conn_attempts})')
        sleep(2)
        continue
    print('Connected to MariaDB!')
    break
else:
    raise pymysql.err.OperationalError()

# create app
app = Flask(__name__)
app_name = 'app1'

@app.route('/')
def index():
    # insert log
    date_formatted = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    with connection.cursor() as cursor:
        sql = 'INSERT INTO `logs` (`description`) VALUES (%s)'
        cursor.execute(sql, (f'{app_name}: GET / {date_formatted}'))
    connection.commit()
    
    # read logs
    with connection.cursor() as cursor:
        sql = f'SELECT * FROM `logs` WHERE `description` like "{app_name}%" ORDER BY id DESC'
        cursor.execute(sql)
        logs = cursor.fetchmany(20)
    logs = '<br>'.join([str(log) for log in logs])
    
    return Response(f'hi this is {app_name}<br>'+logs)