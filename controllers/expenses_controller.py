import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt

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

    if limite_mensual is not None and (sum(cantidad for _, cantidad, _ in gastos) + cantidad) > limite_mensual:
        messagebox.showwarning("Advertencia", f"Superaste el límite establecido para el mes de {simpledialog.askstring('Mes', 'Ingrese el mes')}")
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

    entry_nombre.delete(0, 'end')
    entry_cantidad.delete(0, 'end')
    mostrar_resumen(resumen_label)

def mostrar_resumen(resumen_label):
    resumen_categorias = {"Comida": 0, "Transporte": 0, "Entretenimiento": 0, "Otros": 0}
    total_general = 0

    for gasto in gastos:
        nombre, cantidad, categoria = gasto
        if categoria.startswith("Otros - "):
            subcategoria = categoria.split(" - ")[1]
            subcategorias_otros[subcategoria] += cantidad
        else:
            resumen_categorias[categoria] += cantidad
        total_general += cantidad

    resumen = "Resumen de Gastos:\n"
    for categoria, total in resumen_categorias.items():
        resumen += f"{categoria}: ${total:.2f}\n"

    if subcategorias_otros:
        resumen += "\nDetalle de 'Otros':\n"
        for subcategoria, total in subcategorias_otros.items():
            resumen += f"  - {subcategoria}: ${total:.2f}\n"

    resumen += f"\nTotal general: ${total_general:.2f}"
    resumen_label.config(text=resumen)

def mostrar_grafico():
    categorias = {}
    for _, cantidad, categoria in gastos:
        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += cantidad

    plt.figure(figsize=(10, 7))
    plt.pie(categorias.values(), labels=categorias.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Gastos')
    plt.show()

def establecer_limite():
    global limite_mensual
    limite = simpledialog.askfloat("Establecer Límite", "Ingrese el límite mensual:")
    if limite is None or limite <= 0:
        messagebox.showerror("Error", "Debe ingresar un límite válido.")
        return
    limite_mensual = limite
    messagebox.showinfo("Éxito", f"Límite mensual establecido en ${limite_mensual:.2f}.")
