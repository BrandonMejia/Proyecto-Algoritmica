from flask import Flask , render_template, request, redirect, url_for, 

flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#MySqlConnection
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='flaskcontacts'
mysql = MySQL(app)