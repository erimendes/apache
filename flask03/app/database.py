import mysql.connector
from mysql.connector import Error
import os

# Configuração do banco de dados
db_config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'host': os.getenv('DB_HOST', 'db'),
    'database': os.getenv('DB_NAME', 'testdb'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

# Função para conectar ao banco de dados
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"],
            # charset=db_config["charset"],
            # collation=db_config["collation"]
        )
        if conn.is_connected():
            print("Conexão bem-sucedida ao banco de dados")
            return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para criar a tabela 'users'
def create_users_table():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL
                ) CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """)
            conn.commit()
            print("Tabela 'users' criada com sucesso.")
        except Error as e:
            print(f"Erro ao criar a tabela 'users': {e}")
        finally:
            cursor.close()
            conn.close()
