import mysql.connector
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['MYSQL_DATABASE_HOST'],
            user=current_app.config['MYSQL_DATABASE_USER'],
            password=current_app.config['MYSQL_DATABASE_PASSWORD'],
            database=current_app.config['MYSQL_DATABASE_DB']
        )
    return g.db

def close_db(e=None):
    
    
    db = g.pop('db', None)

    if db is not None:
        db.close()