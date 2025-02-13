import os
import boto3
from botocore.exceptions import ClientError
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración AWS
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')

# Configuración Base de datos
db_config = {
    'dbname': os.getenv('PROD_POSTGRES_DB'),
    'user': os.getenv('PROD_POSTGRES_USER'),
    'host': os.getenv('PROD_POSTGRES_HOST'),
    'port': os.getenv('PROD_POSTGRES_PORT')
}

def get_rds_password():
    """Obtiene el token de autenticación de AWS RDS"""
    client = boto3.client('rds',
                          region_name=aws_region,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
    try:
        token = client.generate_db_auth_token(
            DBHostname=db_config['host'],
            Port=db_config['port'],
            DBUsername=db_config['user'],
            Region=aws_region
        )
        return token
    except ClientError as e:
        print(f"Error generando token de autenticación: {e}")
        return None

def get_connection():
    """
    Crea y retorna una conexión a la base de datos PostgreSQL usando autenticación AWS
    """
    try:
        password = get_rds_password()
        if not password:
            raise Exception("No se pudo obtener el token de autenticación")

        connection_string = f"postgresql://{db_config['user']}:{password}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
        engine = create_engine(connection_string)
        return engine.connect()

    except Exception as e:
        print(f"Error creando conexión PostgreSQL: {str(e)}")
        raise Exception(f"Error de conexión a la base de datos: {str(e)}")