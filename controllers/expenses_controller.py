import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt

gastos = []
limite_mensual = None
moneda_actual = "ARS"
conversion_rates = {"ARS": 1, "USD": 370, "EUR": 395}

def ingresar_gasto(entry_nombre, entry_cantidad, categoria_var, moneda_var, resumen_text):
    nombre_gasto = entry_nombre.get()
    cantidad = entry_cantidad.get()
    categoria = categoria_var.get()
    moneda = moneda_var.get()

    if not nombre_gasto or not cantidad:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    try:
        cantidad = float(cantidad)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")
        return

    # Conversión de moneda
    cantidad_ars = cantidad * conversion_rates[moneda]

    if limite_mensual is not None and (sum(cantidad for _, cantidad, _ in gastos) + cantidad_ars) > limite_mensual:
        messagebox.showwarning("Advertencia", f"Superaste el límite mensual establecido. El gasto se ha agregado igualmente.")
    
    # Agregar el gasto
    gasto = (nombre_gasto, cantidad_ars, categoria, moneda)
    gastos.append(gasto)

    # Limpiar los campos
    entry_nombre.delete(0, 'end')
    entry_cantidad.delete(0, 'end')

    # Mostrar resumen actualizado
    mostrar_resumen(resumen_text)

def mostrar_resumen(resumen_text):
    resumen_categorias = {"Comida": 0, "Transporte": 0, "Entretenimiento": 0, "Otros": 0}
    total_general = 0

    resumen_text.delete(1.0, 'end')

    for gasto in gastos:
        nombre, cantidad, categoria, moneda = gasto
        resumen_categorias[categoria] += cantidad
        total_general += cantidad
        resumen_text.insert(tk.END, f"{nombre} - {cantidad:.2f} ARS ({moneda}) en {categoria}\n")

    resumen_text.insert(tk.END, "\nResumen por categoría:\n")
    for categoria, total in resumen_categorias.items():
        resumen_text.insert(tk.END, f"{categoria}: ${total:.2f} ARS\n")
    
    resumen_text.insert(tk.END, f"\nTotal general: ${total_general:.2f} ARS\n")

def mostrar_grafico():
    categorias = {}
    for _, cantidad, categoria, _ in gastos:
        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += cantidad

    plt.figure(figsize=(10, 7))
    plt.pie(categorias.values(), labels=categorias.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Gastos')
    plt.show()

def establecer_limite():
    global limite_mensual
    limite = simpledialog.askfloat("Establecer Límite", "Ingrese el límite mensual en ARS:")
    if limite is None or limite <= 0:
        messagebox.showerror("Error", "Debe ingresar un límite válido.")
        return
    limite_mensual = limite
    messagebox.showinfo("Éxito", f"Límite mensual establecido en ${limite_mensual:.2f} ARS.")

def limpiar_resumen(resumen_text):
    resumen_text.delete(1.0, 'end')
    messagebox.showinfo("Resumen", "El resumen ha sido limpiado.")
