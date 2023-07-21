import tkinter as tk
from administrador.gui_app import Frame, barra_menu
def main():
    root = tk.Tk()
    root.title('Sistema de egresados')
    root.iconbitmap('img/logo.ico')
     # Obtener el ancho y alto de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Establecer el tamaño de la ventana al tamaño de la pantalla
    root.geometry(f"{screen_width}x{screen_height}")
    
    barra_menu(root)

    app = Frame(root = root)
    
    app.mainloop()

if __name__ == '__main__':
    main()
