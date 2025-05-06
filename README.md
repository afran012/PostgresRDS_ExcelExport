# PostgresRDS_ExcelExport

## Descripción
Esta aplicación extrae reportes de una base de datos PostgreSQL en AWS RDS y los exporta a archivos Excel. Permite generar reportes de polígonos y puntos tanto por separado como en un archivo combinado.

## Requisitos
- Python 3.6+
- Credenciales de AWS con acceso a RDS
- Base de datos PostgreSQL en AWS RDS

## Instalación

1. Clone el repositorio
2. Cree un entorno virtual y actívelo:
   ```bash
   python -m venv venv
   venv\Scripts\activate.bat  # En Windows
   source venv/bin/activate   # En Linux/macOS
   ```

3. Instale las dependencias:
   ```bash
   pip install -r proyecto/requirements.txt
   ```

## Configuración del archivo .env

Cree un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
# Configuración PostgreSQL
PROD_POSTGRES_HOST=su-instancia.region.rds.amazonaws.com
PROD_POSTGRES_DB=nombre_base_datos
PROD_POSTGRES_USER=usuario_aws_iam
PROD_POSTGRES_PORT=5432

# Configuración AWS
AWS_ACCESS_KEY_ID=su_access_key_id
AWS_SECRET_ACCESS_KEY=su_secret_access_key
AWS_DEFAULT_REGION=us-east-1
```

### Notas importantes sobre la configuración:
- El `PROD_POSTGRES_USER` debe ser un usuario IAM con permisos para autenticación RDS
- Las credenciales AWS (`AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY`) deben tener permisos para generar tokens de autenticación RDS
- Asegúrese de que la instancia RDS tenga habilitada la autenticación IAM

## Uso

1. Active el entorno virtual:
   ```bash
   venv\Scripts\activate.bat
   ```

2. Navegue a la carpeta del proyecto:
   ```bash
   cd proyecto
   ```

3. Ejecute la aplicación:
   ```bash
   python main.py
   ```

4. Siga las instrucciones en pantalla:
   - Seleccione `1` para generar archivos separados para polígonos y puntos
   - Seleccione `2` para generar un archivo combinado con ambos tipos de datos

5. Los archivos Excel generados se guardarán en la carpeta `proyecto` con el formato:
   - `reportes_poligonos_YYYYMMDD_HHMMSS.xlsx` (para polígonos)
   - `reportes_puntos_YYYYMMDD_HHMMSS.xlsx` (para puntos)
   - `reportes_combined_YYYYMMDD_HHMMSS.xlsx` (para datos combinados)

## Estructura del Proyecto

- `proyecto/main.py`: Punto de entrada principal
- `proyecto/src/database.py`: Gestión de conexiones a la base de datos usando autenticación IAM de AWS RDS
- `proyecto/src/excel_generator.py`: Funciones para generar los archivos Excel
- `proyecto/src/queries.py`: Consultas SQL para extraer los datos de polígonos y puntos
- `sql/`: Carpeta con las consultas SQL originales utilizadas para obtener los datos

## Dependencias Principales

- psycopg2-binary: Conector para PostgreSQL
- pandas: Manipulación de datos y análisis
- openpyxl: Generación de archivos Excel
- python-dotenv: Manejo de variables de entorno
- boto3: SDK de AWS para Python
- sqlalchemy: ORM y herramientas SQL

## Solución de Problemas

- Si experimenta problemas de conexión, verifique:
  - Las credenciales en el archivo `.env`
  - Los permisos IAM del usuario
  - Que la instancia RDS tenga habilitada la autenticación IAM
  - Que la instancia RDS sea accesible desde su red

- Para problemas con la generación de Excel:
  - Verifique que tiene suficiente espacio en disco
  - Asegúrese de que no tiene el archivo abierto en otra aplicación

## Seguridad

- Nunca almacene el archivo `.env` en el control de versiones
- Considere usar AWS Secrets Manager para una gestión más segura de credenciales
- Utilice credenciales IAM con los permisos mínimos necesarios