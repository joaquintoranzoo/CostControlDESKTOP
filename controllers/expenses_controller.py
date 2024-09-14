import matplotlib.pyplot as plt
from tkinter import messagebox, simpledialog

gastos = []
subcategorias_otros = {}
limite_mensual = None

def ingresar_gasto(entry_nombre, entry_cantidad, categoria_var, resumen_label):
    nombre_gasto = entry_nombre.get()
    cantidad = entry_cantidad.get()
    categoria = categoria_var.get()

    if not nombre_gasto or not cantidad:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    try:
        cantidad = float(cantidad)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")
        return

    if categoria == "Otros":
        subcategoria = simpledialog.askstring("Subcategoría", "Ingrese la subcategoría para 'Otros':")
        if not subcategoria:
            messagebox.showerror("Error", "Debe ingresar un nombre para la subcategoría.")
            return
        categoria = f"Otros - {subcategoria}"

        if subcategoria not in subcategorias_otros:
            subcategorias_otros[subcategoria] = 0

    gasto = (nombre_gasto, cantidad, categoria)
    gastos.append(gasto)

    if limite_mensual and total_gastos() > limite_mensual:
        messagebox.showwarning("Advertencia", "Superaste el límite establecido para el mes.")

    entry_nombre.delete(0, 'end')
    entry_cantidad.delete(0, 'end')

    mostrar_resumen_label(resumen_label)

def mostrar_resumen_label(resumen_label):
    resumen_categorias = {"Comida": 0, "Transporte": 0, "Entretenimiento": 0, "Otros": 0}

    for gasto in gastos:
        nombre, cantidad, categoria = gasto
        if categoria.startswith("Otros - "):
            subcategoria = categoria.split(" - ")[1]
            subcategorias_otros[subcategoria] += cantidad
        else:
            resumen_categorias[categoria] += cantidad

    resumen = "Resumen de Gastos:\n"
    for categoria, total in resumen_categorias.items():
        resumen += f"{categoria}: ${total:.2f}\n"
    if subcategorias_otros:
        resumen += "\nDetalle de 'Otros':\n"
        for subcategoria, total in subcategorias_otros.items():
            resumen += f"  - {subcategoria}: ${total:.2f}\n"

    resumen_label.config(text=resumen)

def total_gastos():
    return sum(cantidad for _, cantidad, _ in gastos)

def mostrar_grafico():
    categorias = {}
    for gasto in gastos:
        nombre, cantidad, categoria = gasto
        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += cantidad

    labels = categorias.keys()
    valores = categorias.values()

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Gastos')
    plt.show()

def establecer_limite():
    global limite_mensual
    limite_mensual = simpledialog.askfloat("Límite de Gastos", "Ingrese el límite de gastos para este mes:")
    if limite_mensual is None:
        messagebox.showerror("Error", "Debe ingresar un límite válido.")
