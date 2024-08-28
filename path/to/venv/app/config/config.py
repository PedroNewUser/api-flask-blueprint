import mysql.connector
import os

def get_db_connection():
    """
    Estabelece uma conexão com o banco de dados MySQL.

    Retorna:
    - Uma conexão com o banco de dados MySQL, configurada com os parâmetros especificados.
    """
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'mysql'),  # Nome do serviço MySQL no Docker Compose
        user=os.getenv('MYSQL_USER', 'user'),  # Nome do usuário para autenticação
        password=os.getenv('MYSQL_PASSWORD', 'secret'),  # Senha do usuário
        database=os.getenv('MYSQL_DATABASE', 'lp_trainer'),  # Nome do banco de dados
        port=int(os.getenv('MYSQL_PORT', 3306)) 
    )
