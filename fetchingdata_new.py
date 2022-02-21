#from crypt import methods
from flask import Flask, render_template
import psycopg2
import psycopg2.extras
from loguru import logger
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify





app = Flask(__name__)
 
connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="localhost",
                                    port="5432",
                                    database="Goa_Works_1")

cursor = connection.cursor()



@app.route('/teir_two', methods = ['GET'])
def teir_one_isoch():
    try:
     
      postgreSQL_select_Query = "select * from t2_isochrones"
      cursor.execute(postgreSQL_select_Query)
      print("Selecting rows from t2_isochrones table using cursor.fetchall")

      isochrone = cursor.fetchall()
      print("Print each row and it's columns values")
      for row in isochrone:
      
          print("hospital_id = ", row[0], )
          print("geom = ", row[1])
          
      return jsonify(isochrone)
    except (Exception, psycopg2.Error) as error:
          print("Error while fetching data from PostgreSQL", error)
        

   
    # finally:
    #   # closing database connection.
    #   if connection:
    #       cursor.close()
    #       connection.close()
    #       print("PostgreSQL connection is closed")

if __name__ == '__main__':
    app.run(debug=True)
