import pandas as pd
from src.database import get_connection
from src.queries import POLYGON_QUERY, POINT_QUERY
from src.excel_generator import generate_excel, generate_combined_excel

def main():
    try:
        # Preguntar al usuario si desea generar archivos por separado o combinados
        option = input("¿Desea generar los archivos por separado (1) o combinados (2)? Ingrese 1 o 2: ")
        
        # Establecer conexión con la base de datos
        conn = get_connection()
        
        # Procesar datos de polígonos
        print("Procesando datos de polígonos...")
        df_polygons = pd.read_sql_query(POLYGON_QUERY, conn)
        
        # Procesar datos de puntos
        print("Procesando datos de puntos...")
        df_points = pd.read_sql_query(POINT_QUERY, conn)
        
        if option == '1':
            # Generar archivos por separado
            polygon_file = generate_excel(df_polygons, "poligonos")
            print(f"Archivo de polígonos generado: {polygon_file}")
            
            point_file = generate_excel(df_points, "puntos")
            print(f"Archivo de puntos generado: {point_file}")
        elif option == '2':
            # Generar archivo combinado
            combined_file = generate_combined_excel(df_polygons, df_points)
            print(f"Archivo combinado generado: {combined_file}")
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")
        
    except Exception as e:
        print(f"Error durante la ejecución: {str(e)}")
    finally:
        if conn:
            conn.close()
            print("Conexión a la base de datos cerrada")

if __name__ == "__main__":
    main()