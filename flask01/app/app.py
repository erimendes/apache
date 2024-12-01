# funciona

# from flask import Flask, request, jsonify
# from flasgger import Swagger
# import mysql.connector
# from mysql.connector import Error
# import os

# app = Flask(__name__)
# swagger = Swagger(app, 
#                   template={
#                       'info': {
#                           'title': 'API Title',
#                           'version': '1.0.0',
#                       },
#                       'schemes': ['http']  # ou ['https'] se estiver usando HTTPS
#                   })

# db_config = {
#     'user': os.getenv('DB_USER', 'root'),
#     'password': os.getenv('DB_PASSWORD', 'password'),
#     'host': os.getenv('DB_HOST', 'db'),  # 'db' é o nome do serviço no docker-compose.yml
#     'database': os.getenv('DB_NAME', 'testdb'),
#     'charset': 'utf8mb4',
#     'collation': 'utf8mb4_unicode_ci'
# }

# # Função para conectar ao banco de dados
# def get_db_connection():
#     try:
#         conn = mysql.connector.connect(
#             host=db_config["host"],
#             user=db_config["user"],
#             password=db_config["password"],
#             database=db_config["database"],
#             charset=db_config["charset"],
#             collation=db_config["collation"]
#         )
#         if conn.is_connected():
#             print("Conexão bem-sucedida ao banco de dados")
#             return conn
#     except Error as e:
#         print(f"Erro ao conectar ao banco de dados: {e}")
#         return None

# # Criação da tabela 'users' ao inicializar a aplicação
# def create_users_table():
#     conn = get_db_connection()
#     if conn:
#         cursor = conn.cursor()
#         try:
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS users (
#                     id INT AUTO_INCREMENT PRIMARY KEY,
#                     name VARCHAR(255) NOT NULL
#                 ) CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
#             """)
#             conn.commit()
#             print("Tabela 'users' criada com sucesso.")
#         except Error as e:
#             print(f"Erro ao criar a tabela 'users': {e}")
#         finally:
#             cursor.close()
#             conn.close()

# # # Criar a tabela ao iniciar o aplicativo
# # create_users_table()

# @app.route('/')
# def index():
#     return jsonify({"mensagem": "Welcome to the Flask APP!"})

# @app.route('/initialize-db', methods=['GET'])
# def initialize_db():
#     create_users_table()
#     return jsonify({'message': 'Tabela users criada com sucesso ou já existia!'})

# @app.route('/insert-user', methods=['GET'])
# def add_user_from_query():
#     """
#     Adiciona um usuário ao banco de dados com valor enviado na URL.
#     URL exemplo: /insert-user?name=Catarina
#     """
#     name = request.args.get('name')  # Obtém o valor do parâmetro "name"

#     if not name:
#         return jsonify({'message': 'Nome é obrigatório na URL'}), 400

#     conn = get_db_connection()
#     if conn:
#         cursor = conn.cursor()
#         try:
#             cursor.execute('INSERT INTO users (name) VALUES (%s)', (name,))
#             conn.commit()
#             return jsonify({'message': f'Usuário {name} adicionado com sucesso!'}), 201
#         except Error as e:
#             print(f"Erro ao inserir usuário: {e}")
#             return jsonify({'message': 'Erro ao inserir usuário'}), 500
#         finally:
#             cursor.close()
#             conn.close()
#     else:
#         return jsonify({'message': 'Erro ao conectar ao banco de dados'}), 500

# @app.route('/users', methods=['GET'])
# def get_users():
#     """
#     Lista todos os usuários do banco de dados.
#     ---
#     responses:
#       200:
#         description: Lista de usuários.
#         schema:
#           type: array
#           items:
#             properties:
#               id:
#                 type: integer
#                 description: ID do usuário.
#               name:
#                 type: string
#                 description: Nome do usuário.
#     """
#     conn = get_db_connection()
#     if conn:
#         cursor = conn.cursor()
        
#         try:
#             cursor.execute('SELECT id, name FROM users')
#             users = cursor.fetchall()
#             return jsonify(users)
#         except Error as e:
#             print(f"Erro ao buscar usuários: {e}")
#             return jsonify({'message': 'Erro ao buscar usuários'}), 500
#         finally:
#             cursor.close()
#             conn.close()
#     else:
#         return jsonify({'message': 'Erro ao conectar ao banco de dados'}), 500

# @app.route('/teste-conexao', methods=['GET'])
# def teste():
#     """
#     Testa a conexão com o banco de dados.
#     """
#     connection = get_db_connection() 
#     if connection:
#         return jsonify({"mensagem": "Conexão bem-sucedida!"}) 
#     else: 
#         return jsonify({"mensagem": "Erro ao conectar ao banco de dados"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify
from flasgger import Swagger
import mysql.connector
from mysql.connector import Error
import os
from database import get_db_connection, create_users_table

app = Flask(__name__)
swagger = Swagger(app, 
                  template={
                      'info': {
                          'title': 'API Title',
                          'version': '1.0.0',
                      },
                      'schemes': ['http']  # ou ['https'] se estiver usando HTTPS
                  })

@app.route('/')
def index():
    return jsonify({"mensagem": "Welcome to the Flask APP!"})

@app.route('/initialize-db', methods=['GET'])
def initialize_db():
    create_users_table()
    return jsonify({'message': 'Tabela users criada com sucesso ou já existia!'})

@app.route('/insert-user', methods=['GET'])
def add_user_from_query():
    """
    Adiciona um usuário ao banco de dados com valor enviado na URL.
    URL exemplo: /insert-user?name=Catarina
    """
    name = request.args.get('name')  # Obtém o valor do parâmetro "name"

    if not name:
        return jsonify({'message': 'Nome é obrigatório na URL'}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (name) VALUES (%s)', (name,))
            conn.commit()
            return jsonify({'message': f'Usuário {name} adicionado com sucesso!'}), 201
        except Error as e:
            print(f"Erro ao inserir usuário: {e}")
            return jsonify({'message': 'Erro ao inserir usuário'}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'message': 'Erro ao conectar ao banco de dados'}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """
    Lista todos os usuários do banco de dados.
    ---
    responses:
      200:
        description: Lista de usuários.
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
                description: ID do usuário.
              name:
                type: string
                description: Nome do usuário.
    """
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT id, name FROM users')
            users = cursor.fetchall()
            return jsonify(users)
        except Error as e:
            print(f"Erro ao buscar usuários: {e}")
            return jsonify({'message': 'Erro ao buscar usuários'}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'message': 'Erro ao conectar ao banco de dados'}), 500

@app.route('/teste-conexao', methods=['GET'])
def teste():
    """
    Testa a conexão com o banco de dados.
    """
    connection = get_db_connection() 
    if connection:
        return jsonify({"mensagem": "Conexão bem-sucedida!"}) 
    else: 
        return jsonify({"mensagem": "Erro ao conectar ao banco de dados"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)