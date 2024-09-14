import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from controllers.expenses_controller import ingresar_gasto, mostrar_resumen, mostrar_grafico, establecer_limite
from PIL import Image, ImageTk

def iniciar_interfaz():
    root = tk.Tk()
    root.title("Control de Gastos")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 400
    window_height = 500
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    logo_image = Image.open("assets/logo.png")
    logo_image = logo_image.resize((100, 100), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = ttk.Label(root, image=logo_photo)
    logo_label.image = logo_photo
    logo_label.grid(row=0, column=0, columnspan=2, pady=10)

    categoria_var = tk.StringVar(value="Comida")

    ttk.Label(root, text="Nombre del gasto:").grid(row=1, column=0, padx=10, pady=10, sticky="W")
    entry_nombre = ttk.Entry(root)
    entry_nombre.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(root, text="Cantidad:").grid(row=2, column=0, padx=10, pady=10, sticky="W")
    entry_cantidad = ttk.Entry(root)
    entry_cantidad.grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(root, text="Categoría:").grid(row=3, column=0, padx=10, pady=10, sticky="W")
    categoria_menu = ttk.OptionMenu(root, categoria_var, "Comida", "Comida", "Transporte", "Entretenimiento", "Otros")
    categoria_menu.grid(row=3, column=1, padx=10, pady=10)

    ttk.Button(root, text="Ingresar Gasto", command=lambda: ingresar_gasto(entry_nombre, entry_cantidad, categoria_var, resumen_label)).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    ttk.Button(root, text="Mostrar Resumen", command=lambda: mostrar_resumen(root)).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    ttk.Button(root, text="Mostrar Gráfico de Gastos", command=mostrar_grafico).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    ttk.Button(root, text="Establecer Límite", command=establecer_limite).grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    ttk.Button(root, text="Salir", command=root.quit).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    resumen_label = ttk.Label(root, text="", font=("Arial", 10))
    resumen_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()
