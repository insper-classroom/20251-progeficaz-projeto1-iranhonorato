from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__) 
app.static_folder = 'static' 





@app.route("/")
@app.route("/index")
def index():
    conexao=sql.connect("db_web.db")
    
    # O row_factory define como cada linha do resultado da consulta será representada.
    conexao.row_factory=sql.Row
    # Quando você define row_factory = sql.Row, cada linha retornada pela consulta será representada como um dicionário. 
    # Isso significa que você pode acessar as colunas usando o nome delas como chave


    cursor=conexao.cursor()
    cursor.execute("select * from posts")



    # Essa linha recupera todas as linhas do resultado de uma consulta SQL e as armazena na variável data
    data=cursor.fetchall()
    # cursor.fetchall() retorna uma lista contendo todas as linhas que foram recuperadas pela consulta.
    # Cada item dessa lista será um objeto Row (como configurado pela linha anterior), então você pode acessar os dados por nome da coluna.


    return render_template("index.html",datas=data)


@app.route("/add_post",methods=['POST','GET'])
def add_post():
    if request.method=='POST':
        # Quando o formulário é enviado (via POST), os dados dos campos do formulário são enviados dentro de request.form.
        title=request.form['title']
        # request.form['uname'] pega o valor do campo uname (que provavelmente é um campo de nome do usuário no formulário HTML) armazenando na variável uname.
        
        content=request.form['content']
        # Similar à linha anterior, aqui você está pegando o valor do campo contact enviado no formulário e armazenando na variável contact.
        
        conexao=sql.connect("db_web.db")
        cursor=conexao.cursor()

        # Os "?"" são placeholders para os valores que você quer inserir (isto é uma prática comum para evitar SQL Injection).
        cursor.execute("insert into posts(TITLE,CONTENT) values (?,?)",(title,content))
        conexao.commit()

        # A função flash() é usada para mostrar uma mensagem ao usuário após a operação (inserir o usuário).
        flash('Post Added','success')
        return redirect(url_for("index"))
    return render_template("add_post.html")

@app.route("/edit_post/<string:uid>",methods=['POST','GET'])
def edit_post(uid):
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content']

        conexao=sql.connect("db_web.db")
        cursor=conexao.cursor()
        cursor.execute("update posts set TITLE=?,CONTENT=? where UID=?",(title,content,uid))
        conexao.commit()
        flash('Post Updated','success')
        return redirect(url_for("index"))
    conexao=sql.connect("db_web.db")
    conexao.row_factory=sql.Row
    cursor=conexao.cursor()
    cursor.execute("select * from posts where UID=?",(uid,))
    data=cursor.fetchone()
    return render_template("edit_post.html",datas=data)
    
@app.route("/delete_post/<string:uid>",methods=['GET'])
def delete_post(uid):
    conexao=sql.connect("db_web.db")
    cursor=conexao.cursor()
    cursor.execute("delete from posts where UID=?",(uid,))
    conexao.commit()
    flash('Post Deleted','warning')
    return redirect(url_for("index"))



if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)