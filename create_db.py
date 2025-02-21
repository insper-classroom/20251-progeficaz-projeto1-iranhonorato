import sqlite3 as sql

# Essa linha cria uma conexão com um banco de dados SQLite chamado db_web.db. 
# Se o arquivo não existir, o SQLite cria um novo banco de dados automaticamente.
conexao = sql.connect('db_web.db')
# Pense nisso como abrir um canal de comunicação com o banco de dados.




# Aqui, criamos um cursor, que é um objeto responsável por executar comandos SQL no banco de dados.
cursor = conexao.cursor()
# Pense no cursor como uma "mão" que pode manipular os dados dentro do banco.




# Deleta a tabela "users" se ela existir.
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS posts")




# Cria uma tabela posts" em db_web database 
sql ='''CREATE TABLE "posts" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"TITLE"	TEXT,
	"CONTENT"	TEXT
)'''
cursor.execute(sql)


# A linha abaixo tem uma função muito importante no contexto de bancos de dados, 
# especialmente em operações que envolvem modificação de dados 
# (como INSERT, UPDATE, DELETE ou até mesmo criação de tabelas como no seu código).
conexao.commit()



# A linha con.close() tem a função de fechar a conexão com o banco de dados SQLite quando 
# você já terminou de realizar as operações desejadas.
conexao.close()

