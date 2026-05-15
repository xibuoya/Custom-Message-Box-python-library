import customtkinter as ctk

def ctk_msg_entry(title, message, placeholder):
    # Fenêtre
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("400x180")
    win.resizable(False, False)
    win.attributes("-topmost", True)

    entry_var = ctk.StringVar()

    # On définit la fonction AVANT de l'appeler dans le bouton
    def réponse():
        entry_var.set(entry.get())
        win.destroy()

    label = ctk.CTkLabel(win, text=message)
    label.pack(pady=15)

    # On crée un cadre pour utiliser grid sans casser le pack du label
    frame = ctk.CTkFrame(win, fg_color="transparent")
    frame.pack(pady=10, padx=20, fill="x")

    entry = ctk.CTkEntry(frame, placeholder_text=placeholder)
    entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")

    ok = ctk.CTkButton(frame, text="ok", width=60, command=réponse)
    ok.grid(row=0, column=1)

    frame.columnconfigure(0, weight=1)

    win.grab_set()
    win.wait_window() # Attend la fermeture
    return entry_var.get()

def ctk_msg_yesno(title, message):
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("400x150")
    win.resizable(False, False)
    win.attributes("-topmost", True)

    yesno_var = ctk.IntVar(value=-1)

    def yes():
        yesno_var.set(1)
        win.destroy()

    def no():
        yesno_var.set(0)
        win.destroy()

    label = ctk.CTkLabel(win, text=message)
    label.pack(pady=20)

    # Cadre pour les boutons
    btn_frame = ctk.CTkFrame(win, fg_color="transparent")
    btn_frame.pack(fill="x", padx=50)

    yes_btn = ctk.CTkButton(btn_frame, text="Oui", command=yes, width=100)
    yes_btn.grid(row=0, column=0, padx=10)

    no_btn = ctk.CTkButton(btn_frame, text="Non", command=no, width=100)
    no_btn.grid(row=0, column=1, padx=10)

    win.grab_set()
    win.wait_window()
    return yesno_var.get()

def ctk_msg_custom(title, message, number, txtone, txttwo, txtthree=None):
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("500x180")
    win.resizable(False, False)
    win.attributes("-topmost", True)

    custom_btns_var = ctk.StringVar(value="")

    label = ctk.CTkLabel(win, text=message)
    label.pack(pady=15)

    btn_frame = ctk.CTkFrame(win, fg_color="transparent")
    btn_frame.pack(pady=20)

    # On gère les 2 ou 3 boutons
    def click(val):
        custom_btns_var.set(val)
        win.destroy()

    # Bouton 1 et 2 (toujours présents)
    ctk.CTkButton(btn_frame, text=txtone, command=lambda: click(txtone)).grid(row=0, column=0, padx=5)
    ctk.CTkButton(btn_frame, text=txttwo, command=lambda: click(txttwo)).grid(row=0, column=1, padx=5)
    
    # Bouton 3 (optionnel)
    if number == 3:
        ctk.CTkButton(btn_frame, text=txtthree, command=lambda: click(txtthree)).grid(row=0, column=2, padx=5)

    win.grab_set()
    win.wait_window()
    return custom_btns_var.get()

def ctkinfo(title, message):
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("400x150")
    win.attributes("-topmost", True)

    ctk.CTkLabel(win, text=f"{message}").pack(pady=20)
    ctk.CTkButton(win, text="OK", command=win.destroy).pack(pady=10)

def ctkerror(title, message):
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("400x150")
    win.attributes("-topmost", True)

    # Texte en rouge pour l'erreur
    ctk.CTkLabel(win, text=f"{message}", text_color="red").pack(pady=20)
    ctk.CTkButton(win, text="Fermer", command=win.destroy).pack(pady=10)