import customtkinter as ctk
import functions as f
import global_vars
import json

def read_config() -> dict:
    """Get config var from json file"""
    with open('config.json', 'r') as f:
        return json.load(f)

def update_config(entries: list[ctk.CTkEntry], entries_order : list[str]) -> None:
    """
    Update config with new parameters \n
    entries -> list of tkinter Entries \n
    entries_order -> list of strings, set in order of entries. String must be exact as in json file
    """
    data = {}
    for entry in range(0, len(entries)):
        data[entries_order[entry]] = entries[entry].get()
    
    with open("config.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_from_config(entries: list[ctk.CTkEntry], entries_order : list[str]) -> None:
    """
    Load config parameters \n
    entries -> list of tkinter Entries \n
    entries_order -> list of strings, set in order of entries. String must be exact as in json file
    """
    cfg = read_config()
    for entry in range(0, len(entries)):
        entries[entry].delete(0, ctk.END)
        entries[entry].insert(0, cfg[entries_order[entry]])

        

def run() -> None:
    global_vars.SETTINGS_OPEN = 1
    app = ctk.CTk()
    app.title("Settings")
    app.geometry(f.center_window(app, 640, 300))
    app.resizable(0, 0)
    

    font_fp = ctk.CTkEntry(app,width=280)
    font_sz = ctk.CTkEntry(app,width=280)
    text_cl = ctk.CTkEntry(app,width=280)
    ph_cl = ctk.CTkEntry(app,width=280)
    file_path = ctk.CTkEntry(app,width=280)

    ffp_l = ctk.CTkLabel(app, text="Font Path")
    fsz_l = ctk.CTkLabel(app, text="Font Size")
    cl_l = ctk.CTkLabel(app, text="Text Color (HEX)")
    phcl_l = ctk.CTkLabel(app, text="Placeholder Color (HEX)")
    fp_l = ctk.CTkLabel(app, text="File Path")
    
    save = ctk.CTkButton(app, text="Save", command=lambda: update_config([font_fp, font_sz, text_cl, ph_cl, file_path], ["font_path", "font_size", "text_color_hex", "ph_color_hex", "save_path"]))
    
    load_from_config([font_fp, font_sz, text_cl, ph_cl, file_path], ["font_path", "font_size", "text_color_hex", "ph_color_hex", "save_path"])

    ffp_l.grid(row=0, column=0, padx=20, pady=5)
    font_fp.grid(row=1, column=0, padx=20, pady=5)
    fsz_l.grid(row=0, column=2, padx=20, pady=5)
    font_sz.grid(row=1, column=2, padx=20, pady=5)

    cl_l.grid(row=2, column=0, padx=20, pady=5)
    text_cl.grid(row=3, column=0, padx=20, pady=5)
    phcl_l.grid(row=2, column=2, padx=20, pady=5)
    ph_cl.grid(row=3, column=2, padx=20, pady=5)
    file_path.grid(row=5, column=0, padx=20, pady=5)
    fp_l.grid(row=4, column=0, padx=20, pady=5)
    
    save.place(rely=.9, relx=.5, anchor="center")

    def on_closing():
        global_vars.SETTINGS_OPEN = 0
        app.destroy()
        
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
