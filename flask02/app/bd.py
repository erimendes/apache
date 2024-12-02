import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexão com MySQL bem-sucedida")
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    return connection

# Função para executar uma consulta SQL
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Consulta executada com sucesso")
    except Error as e:
        print(f"Erro ao executar a consulta: {e}")

# Dados de configuração do banco de dados
host_name = "localhost"
user_name = "root"
user_password = "sua_senha"
db_name = "nome_do_banco"

# Conecte-se ao banco de dados
connection = create_connection(host_name, user_name, user_password, db_name)

# Consulta para criar a tabela 'users'
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    gender VARCHAR(10)
);
"""

# Execute a consulta para criar a tabela
execute_query(connection, create_users_table)

# Consulta para inserir dados na tabela 'users'
insert_user = """
INSERT INTO users (name, age, gender)
VALUES
    ('Alice', 30, 'Female'),
    ('Bob', 25, 'Male'),
    ('Charlie', 35, 'Male');
"""

# Execute a consulta para inserir dados
execute_query(connection, insert_user)
