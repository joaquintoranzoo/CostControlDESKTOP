
gastos = []

def ingresar_gasto(nombre_gasto, cantidad, categoria):
    gasto = (nombre_gasto, cantidad, categoria)
    gastos.append(gasto)

def obtener_resumen():
    resumen_categorias = {"Comida": 0, "Transporte": 0, "Entretenimiento": 0, "Otros": 0}
    total = 0
    
    for gasto in gastos:
        nombre, cantidad, categoria = gasto
        resumen_categorias[categoria] += cantidad
        total += cantidad

    return resumen_categorias, total
