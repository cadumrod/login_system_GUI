import customtkinter as ctk
from database import db
import bcrypt


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
window.iconbitmap('assets\\icons\\python.ico')

# Center the main window
center_window(window, 500, 300)


# Register success function
def show_success_popup():
    popup = ctk.CTkToplevel()
    popup.title("Sucesso")
    popup.after(
        200, lambda: popup.iconbitmap('assets\\icons\\python.ico'))

    # Popup dimensions
    width, height = 300, 150

    # Get screen width and height
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    # Calculates position x and y to center window
    position_x = int((screen_width - width) / 2)
    position_y = int((screen_height - height) / 2)

    # Define window geometry
    popup.geometry(f"{width}x{height}+{position_x}+{position_y}")

    # Get popup on top
    popup.lift()
    popup.grab_set()

    # Success message
    label = ctk.CTkLabel(popup, text="Cadastro efetuado com sucesso!")
    label.pack(pady=20)

    # Function to destroy popup and register windows
    def close_popup():
        popup.destroy()
        registration_window.destroy()

    # Close popup button
    close_button = ctk.CTkButton(popup, text="OK", command=close_popup)
    close_button.pack(pady=10)


# Register error function
def error_popup():
    popup = ctk.CTkToplevel()
    popup.title("Erro")
    popup.after(
        200, lambda: popup.iconbitmap('assets\\icons\\python.ico'))

    # Popup dimensions
    width, height = 300, 150

    # Get screen width and height
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    # Calculates position x and y to center window
    position_x = int((screen_width - width) / 2)
    position_y = int((screen_height - height) / 2)

    # Define window geometry
    popup.geometry(f"{width}x{height}+{position_x}+{position_y}")

    # Get popup on top
    popup.lift()
    popup.grab_set()

    # Error message
    label = ctk.CTkLabel(
        popup, text="As senhas não coincidem. Tente novamente.")
    label.pack(pady=20)

    # Close popup button
    close_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
    close_button.pack(pady=10)


# Fuction for window register
def open_registration_window():
    global registration_window
    # Disable the registration button to prevent opening multiple windows
    btn_register_window.configure(state="disabled")

    # Create a new window
    registration_window = ctk.CTkToplevel(window)
    registration_window.geometry("400x300")
    registration_window.title("Cadastro de Usuário")
    registration_window.after(
        200, lambda: registration_window.iconbitmap('assets\\icons\\python.ico'))
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

    username_entry = ctk.CTkEntry(registration_window,
                                  placeholder_text="Novo Usuário")
    username_entry.pack(padx=10, pady=10)

    password_entry = ctk.CTkEntry(registration_window,
                                  placeholder_text="Nova Senha", show="*")
    password_entry.pack(padx=10, pady=10)

    confirm_password_entry = ctk.CTkEntry(
        registration_window, placeholder_text="Confirme a Senha", show="*")
    confirm_password_entry.pack(padx=10, pady=10)

    # Get user insertions for register
    def save_data():
        conn = db.db_conn('database\\logsys.db')
        db.create_table(conn)
        username = username_entry.get()
        password = password_entry.get()
        salt = bcrypt.gensalt()
        hash_pw = bcrypt.hashpw(password.encode("utf-8"), salt)
        confirm_password = confirm_password_entry.get()

        if password == confirm_password:
            db.insert_user(conn, username, hash_pw)
            show_success_popup()
        else:
            error_popup()

    btn_register = ctk.CTkButton(
        registration_window, text="Efetuar Cadastro", command=save_data)
    btn_register.pack(pady=10, padx=10)


# Main Window
label = ctk.CTkLabel(window, text="Sistema de login", font=("Arial", 20))
label.pack(padx=10, pady=10)

user = ctk.CTkEntry(window, placeholder_text="Usuário")
user.pack(padx=10, pady=10)

password_login = ctk.CTkEntry(window, placeholder_text="Senha", show="*")
password_login.pack(padx=10, pady=10)

checkbox = ctk.CTkCheckBox(window, text="Lembrar de mim")
checkbox.pack(padx=10, pady=10)


btn_login = ctk.CTkButton(window, text="Login")
btn_login.pack(pady=10, padx=10)


btn_register_window = ctk.CTkButton(
    window, text="Cadastrar", command=open_registration_window)
btn_register_window.pack(pady=10, padx=10)


window.mainloop()
