import pandas as pd
from src.database import get_connection
from src.queries import POLYGON_QUERY, POINT_QUERY
from src.excel_generator import generate_excel

def main():
    try:
        # Establecer conexión con la base de datos
        conn = get_connection()
        
        # Procesar datos de polígonos
        print("Procesando datos de polígonos...")
        df_polygons = pd.read_sql_query(POLYGON_QUERY, conn)
        polygon_file = generate_excel(df_polygons, "poligonos")
        print(f"Archivo de polígonos generado: {polygon_file}")
        
        # Procesar datos de puntos
        print("Procesando datos de puntos...")
        df_points = pd.read_sql_query(POINT_QUERY, conn)
        point_file = generate_excel(df_points, "puntos")
        print(f"Archivo de puntos generado: {point_file}")
        
    except Exception as e:
        print(f"Error durante la ejecución: {str(e)}")
    finally:
        if conn:
            conn.close()
            print("Conexión a la base de datos cerrada")

if __name__ == "__main__":
    main()