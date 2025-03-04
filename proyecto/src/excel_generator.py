import pandas as pd
from datetime import datetime

def generate_excel(df, tipo):
    """
    Genera un archivo Excel a partir de un DataFrame
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reportes_{tipo}_{timestamp}.xlsx"
    
    # Crear un writer de Excel
    writer = pd.ExcelWriter(filename, engine='openpyxl')
    
    # Convertir las columnas de fecha a datetime si existen
    if 'fecha_hora_reporte' in df.columns:
        df['fecha_hora_reporte'] = pd.to_datetime(df['fecha_hora_reporte'])
    
    # Escribir el DataFrame al archivo Excel
    df.to_excel(writer, sheet_name=f'Reportes_{tipo}', index=False)
    
    # Ajustar el ancho de las columnas
    worksheet = writer.sheets[f'Reportes_{tipo}']
    for idx, col in enumerate(df.columns):
        max_length = max(
            df[col].astype(str).apply(len).max(),
            len(str(col))
        ) + 2
        worksheet.column_dimensions[chr(65 + idx)].width = min(max_length, 50)
    
    writer.close()
    return filename

def generate_combined_excel(df_polygons, df_points):
    """
    Genera un archivo Excel combinado a partir de dos DataFrames
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reportes_combined_{timestamp}.xlsx"
    
    # Añadir columna 'tipo' a cada DataFrame
    df_polygons['tipo'] = 'poligono'
    df_points['tipo'] = 'punto'
    
    # Combinar los DataFrames
    df_combined = pd.concat([df_polygons, df_points], ignore_index=True)
    
    # Crear un writer de Excel
    writer = pd.ExcelWriter(filename, engine='openpyxl')
    
    # Convertir las columnas de fecha a datetime si existen
    if 'fecha_hora_reporte' in df_combined.columns:
        df_combined['fecha_hora_reporte'] = pd.to_datetime(df_combined['fecha_hora_reporte'])
    
    # Escribir el DataFrame combinado al archivo Excel
    df_combined.to_excel(writer, sheet_name='Reportes_Combined', index=False)
    
    # Ajustar el ancho de las columnas
    worksheet = writer.sheets['Reportes_Combined']
    for idx, col in enumerate(df_combined.columns):
        max_length = max(
            df_combined[col].astype(str).apply(len).max(),
            len(str(col))
        ) + 2
        worksheet.column_dimensions[chr(65 + idx)].width = min(max_length, 50)
    
    writer.close()
    return filename