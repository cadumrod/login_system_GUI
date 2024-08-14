import customtkinter as ctk


# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


# Setting colors
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

# Set window
window = ctk.CTk()

# Window settings
window.geometry("500x300")
window.title("Sistema de login")
window.resizable(False, False)
window.iconbitmap("python.ico")

# Center the main window
center_window(window, 500, 300)


# Fuction for window register
def open_registration_window():
    # Disable the registration button to prevent opening multiple windows
    btn_register_window.configure(state="disabled")

    # Create a new window
    registration_window = ctk.CTkToplevel(window)
    registration_window.geometry("400x300")
    registration_window.title("Cadastro de Usuário")
    registration_window.after(
        200, lambda: registration_window.iconbitmap('python.ico'))
    center_window(registration_window, 400, 300)

    # Ensure the window is on top
    registration_window.attributes("-topmost", True)
    registration_window.after(
        10, lambda: registration_window.attributes("-topmost", False))
    registration_window.focus_force()

    # Function to re-enable the button when the registration window is closed
    def on_close():
        btn_register_window.configure(state="normal")
        registration_window.destroy()

    registration_window.protocol("WM_DELETE_WINDOW", on_close)

    # Widgets of register window
    label = ctk.CTkLabel(registration_window,
                         text="Cadastro de Usuário", font=("Arial", 20))
    label.pack(padx=10, pady=10)

    username = ctk.CTkEntry(registration_window,
                            placeholder_text="Novo Usuário")
    username.pack(padx=10, pady=10)

    password = ctk.CTkEntry(registration_window,
                            placeholder_text="Nova Senha", show="*")
    password.pack(padx=10, pady=10)

    confirm_password = ctk.CTkEntry(
        registration_window, placeholder_text="Confirme a Senha", show="*")
    confirm_password.pack(padx=10, pady=10)

    btn_register = ctk.CTkButton(registration_window, text="Cadastrar")
    btn_register.pack(pady=10, padx=10)


# Main Window
label = ctk.CTkLabel(window, text="Sistema de login", font=("Arial", 20))
label.pack(padx=10, pady=10)

user = ctk.CTkEntry(window, placeholder_text="Usuário")
user.pack(padx=10, pady=10)

password = ctk.CTkEntry(window, placeholder_text="Senha", show="*")
password.pack(padx=10, pady=10)

checkbox = ctk.CTkCheckBox(window, text="Lembrar de mim")
checkbox.pack(padx=10, pady=10)


btn_login = ctk.CTkButton(window, text="Login")
btn_login.pack(pady=10, padx=10)


btn_register_window = ctk.CTkButton(
    window, text="Cadastrar", command=open_registration_window)
btn_register_window.pack(pady=10, padx=10)


window.mainloop()
