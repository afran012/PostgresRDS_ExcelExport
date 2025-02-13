POLYGON_QUERY = """
    SELECT 
        id_reporte,
        nombre_reporte,
        email_interventor,
        fecha_hora_reporte,
        nombre_lkp_categoria_problematica_3,
        nombre_lkp_categoria_problematica_2,
        nombre_lkp_categoria_problematica_1,
        id_localizacion,
        geometry_type,
        direccion,
        latitud,
        longitud
    FROM public.reporte_problematica_polygon_denormalizado
    ORDER BY id_reporte;
"""

POINT_QUERY = """
    SELECT 
        id_reporte,
        nombre_reporte,
        email_interventor,
        fecha_hora_reporte,
        nombre_lkp_categoria_problematica_3,
        nombre_lkp_categoria_problematica_2,
        nombre_lkp_categoria_problematica_1,
        id_localizacion,
        geometry_type,
        direccion,
        latitud,
        longitud
    FROM public.reporte_problematica_punto_direccion_denormalizado
    ORDER BY id_reporte;
"""