from loguru import logger
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "Goa_Health"
 
DB_HOST = "localhost"
DB_NAME = "Goa_Works"
DB_USER = "postgres"
DB_PASS = "postgres"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/toure', methods = ['GET'])
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM goa_mf_t1"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)

if __name__ == '__main__':
    app.run(debug=True)