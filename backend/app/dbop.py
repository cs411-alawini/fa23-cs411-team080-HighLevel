from .db import get_db

def insert_user(userid,username, password):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (userid, username, password) VALUES (%s,%s,%s)", (userid,username, password))
    db.commit()
    cursor.close()

def get_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user
def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    db.commit()
    cursor.close()
def update_user(userid,username, password):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET username = %s, password = %s WHERE user_id = %s", (username, password, userid))
    db.commit()
    cursor.close()
