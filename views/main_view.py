import tkinter as tk
from tkinter import ttk, messagebox
from controllers.expenses_controller import ingresar_gasto, obtener_resumen
from PIL import Image, ImageTk

def centrar_ventana(ventana, ancho, alto):
    
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

   
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def iniciar_interfaz():
  
    root = tk.Tk()
    root.title("Control de Gastos")
    
   
    ancho_ventana = 400
    alto_ventana = 400
   
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12))
    style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")

   
    try:
        logo_image = Image.open("assets/logo.png")
        logo_image = logo_image.resize((100, 100), Image.LANCZOS)  # Redimensionar el logo
        logo = ImageTk.PhotoImage(logo_image)
    except FileNotFoundError:
        logo = None

    
    root.configure(bg="#f0f0f0")

    
    if logo:
        logo_label = tk.Label(root, image=logo, bg="#f0f0f0")
        logo_label.grid(row=0, column=0, columnspan=2, pady=10)

  
    categoria_var = tk.StringVar(value="Comida")


    ttk.Label(root, text="Nombre del gasto:").grid(row=1, column=0, padx=10, pady=10, sticky="W")
    entry_nombre = ttk.Entry(root)
    entry_nombre.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(root, text="Cantidad:").grid(row=2, column=0, padx=10, pady=10, sticky="W")
    entry_cantidad = ttk.Entry(root)
    entry_cantidad.grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(root, text="Categoría:").grid(row=3, column=0, padx=10, pady=10, sticky="W")
    ttk.OptionMenu(root, categoria_var, "Comida", "Comida", "Transporte", "Entretenimiento", "Otros").grid(row=3, column=1, padx=10, pady=10)

    def registrar_gasto():
        nombre_gasto = entry_nombre.get()
        cantidad = entry_cantidad.get()
        categoria = categoria_var.get()

        try:
            cantidad = float(cantidad)
            ingresar_gasto(nombre_gasto, cantidad, categoria)
            entry_nombre.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            categoria_var.set("Comida")
            messagebox.showinfo("Éxito", "Gasto registrado con éxito.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")

    def mostrar_resumen():
        resumen_categorias, total = obtener_resumen()
        resumen = "\nResumen de Gastos:\n"
        for categoria, total_categoria in resumen_categorias.items():
            resumen += f"{categoria}: ${total_categoria:.2f}\n"
        resumen += f"\nTotal general: ${total:.2f}"
        messagebox.showinfo("Resumen de Gastos", resumen)

    ttk.Button(root, text="Ingresar Gasto", command=registrar_gasto).grid(row=4, column=0, columnspan=2, pady=10)
    ttk.Button(root, text="Mostrar Resumen", command=mostrar_resumen).grid(row=5, column=0, columnspan=2, pady=10)
    ttk.Button(root, text="Salir", command=root.quit).grid(row=6, column=0, columnspan=2, pady=10)
    
    root.update_idletasks() 
    centrar_ventana(root, ancho_ventana, alto_ventana)

    root.mainloop()
