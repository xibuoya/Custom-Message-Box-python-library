import customtkinter as ctk

def ctk_msg_entry(title="Message", message="Please enter a value:", placeholder="Type here...", default_value=""):

    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("400x180")
    win.resizable(False, False)
    win.attributes("-topmost", True)

    entry_var = ctk.StringVar(value=default_value)

    def response():
        entry_var.set(entry.get())
        win.destroy()

    label = ctk.CTkLabel(win, text=message)
    label.pack(pady=15)

    frame = ctk.CTkFrame(win, fg_color="transparent")
    frame.pack(pady=10, padx=20, fill="x")

    entry = ctk.CTkEntry(frame, placeholder_text=placeholder, textvariable=entry_var)
    entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")

    ok_btn = ctk.CTkButton(frame, text="OK", width=60, command=response)
    ok_btn.grid(row=0, column=1)

    frame.columnconfigure(0, weight=1)

    win.grab_set()
    win.wait_window()
    return entry_var.get()

def ctk_msg_yesno(title="Confirmation", message="Are you sure?"):
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("300x150")
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

    btn_frame = ctk.CTkFrame(win, fg_color="transparent")
    btn_frame.pack(pady=10)

    yes_btn = ctk.CTkButton(btn_frame, text="Yes", command=yes, width=100)
    yes_btn.grid(row=0, column=0, padx=10)

    no_btn = ctk.CTkButton(btn_frame, text="No", command=no, width=100)
    no_btn.grid(row=0, column=1, padx=10)

    btn_frame.columnconfigure(0, weight=1)
    btn_frame.columnconfigure(1, weight=1)

    win.grab_set()
    win.wait_window()
    return yesno_var.get()

def ctk_msg_custom(title="Choice", message="Select an option:", txtone="Option 1", txttwo="Option 2"):
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("300x150")
    win.resizable(False, False)
    win.attributes("-topmost", True)

    custom_btns_var = ctk.StringVar(value="")

    label = ctk.CTkLabel(win, text=message)
    label.pack(pady=15)

    btn_frame = ctk.CTkFrame(win, fg_color="transparent")
    btn_frame.pack(pady=10)

    def click(val):
        custom_btns_var.set(val)
        win.destroy()

    ctk.CTkButton(btn_frame, text=txtone, command=lambda: click(txtone), width=100).grid(row=0, column=0, padx=5)
    ctk.CTkButton(btn_frame, text=txttwo, command=lambda: click(txttwo), width=100).grid(row=0, column=1, padx=5)

    btn_frame.columnconfigure(0, weight=1)
    btn_frame.columnconfigure(1, weight=1)

    win.grab_set()
    win.wait_window()
    return custom_btns_var.get()

def ctkinfo(title="Information", message="Operation completed successfully."):
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("400x180")
    win.resizable(False, False)
    win.attributes("-topmost", True)

    ctk.CTkLabel(win, text=f"{message}").pack(pady=20)
    ctk.CTkButton(win, text="OK", width=100, command=win.destroy).pack(pady=10)

def ctkerror(title="Error", message="An unexpected error occurred."):
    win = ctk.CTkToplevel()
    win.title(title)
    win.geometry("400x180")
    win.resizable(False, False)
    win.attributes("-topmost", True)

    ctk.CTkLabel(win, text=f"{message}", text_color="red").pack(pady=20)
    ctk.CTkButton(win, text="Close", width=100, command=win.destroy).pack(pady=10)
