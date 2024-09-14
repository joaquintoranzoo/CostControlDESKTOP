from tkinter import messagebox, simpledialog

# Lista global para almacenar los gastos
gastos = []
subcategorias_otros = {}

def ingresar_gasto(entry_nombre, entry_cantidad, categoria_var):
    nombre_gasto = entry_nombre.get()
    cantidad = entry_cantidad.get()
    categoria = categoria_var.get()

    if not nombre_gasto or not cantidad:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    try:
        # Validar que la cantidad sea un número
        cantidad = float(cantidad)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")
        return

    if categoria == "Otros":
        # Solicitar el nombre de la subcategoría si se selecciona "Otros"
        subcategoria = simpledialog.askstring("Subcategoría", "Ingrese la subcategoría para 'Otros':")
        if not subcategoria:
            messagebox.showerror("Error", "Debe ingresar un nombre para la subcategoría.")
            return
        categoria = f"Otros - {subcategoria}"

        # Guardar subcategoría en el diccionario
        if subcategoria not in subcategorias_otros:
            subcategorias_otros[subcategoria] = 0

    gasto = (nombre_gasto, cantidad, categoria)
    gastos.append(gasto)

    # Limpiar los campos de entrada
    entry_nombre.delete(0, 'end')
    entry_cantidad.delete(0, 'end')
    messagebox.showinfo("Éxito", "Gasto registrado con éxito.")

def mostrar_resumen(root):
    resumen_categorias = {"Comida": 0, "Transporte": 0, "Entretenimiento": 0, "Otros": 0}
    total_general = 0

    # Sumarizar los gastos
    for gasto in gastos:
        nombre, cantidad, categoria = gasto
        if categoria.startswith("Otros - "):
            subcategoria = categoria.split(" - ")[1]
            subcategorias_otros[subcategoria] += cantidad
        else:
            resumen_categorias[categoria] += cantidad
        total_general += cantidad

    # Crear el resumen de los gastos
    resumen = "Resumen de Gastos:\n"
    for categoria, total in resumen_categorias.items():
        resumen += f"{categoria}: ${total:.2f}\n"
    
    # Agregar las subcategorías de "Otros"
    if subcategorias_otros:
        resumen += "\nDetalle de 'Otros':\n"
        for subcategoria, total in subcategorias_otros.items():
            resumen += f"  - {subcategoria}: ${total:.2f}\n"
    
    resumen += f"\nTotal general: ${total_general:.2f}"

    # Mostrar el resumen en un MessageBox
    messagebox.showinfo("Resumen de Gastos", resumen)
