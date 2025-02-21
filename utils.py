import sqlite3 as sql 


def connect_db():
    conexao = sql.connect('db_web.db')
    conexao.row_factory=sql.Row
    return conexao 


def get_all_post():
    conexao = sql.connect('db_web.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM posts")
    data = cursor.fetchall()
    conexao.close()
    return data 


def get_post_uid(uid):
    conexao = sql.connetc("db_web.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM posts WHERE UID=?", (uid,))
    data = cursor.fetchone()
    conexao.close() 
    return data


def add_post(title, content):
    conexao = sql.connect('db_web.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO posts (TITLE, CONTENT) VALUES (?, ?)", (title, content))
    conexao.commit()
    conexao.close() 


def edit_post(title, content, uid):
    conexao = sql.connect('db_web.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE posts SET TITLE=?, CONTENT=? WHERE UID = ?", (title, content, uid))
    conexao.commit()
    conexao.close()


def delete_post(uid):
    conexao = sql.connect('db_web.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM posts WHERE UID = ?", (uid,))
    conexao.commit()
    conexao.close()



