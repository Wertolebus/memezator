# 02.08.2024  
# memetizator  
# zboxjpg    

import customtkinter as ctk
import functions as f
import global_vars
from windows import settings, demotivator_win, cloud_win, impact_win

def start(gv, app):
    """
    Run window \n
    gv -> global variable from global_vars.py \n
    app -> application var from `windows` folder
    """
    if gv == 0:
        app.run()

def run():
    app = ctk.CTk()
    app.title("Menu")
    app.geometry(f.center_window(app, 360, 200))
    app.resizable(0, 0)

    dem_button = ctk.CTkButton(app, text="Demotivator", command=lambda: start(global_vars.DEMOTIVATOR_OPEN, demotivator_win))
    dem_button.grid(row=0, column=0, padx=20, pady=20)

    cld_button = ctk.CTkButton(app, text="Cloud", command=lambda: start(global_vars.CLOUD_OPEN, cloud_win))
    cld_button.grid(row=1, column=0, padx=20, pady=20)

    imp_button = ctk.CTkButton(app, text="Impact", command=lambda: start(global_vars.IMPACT_OPEN, impact_win))
    imp_button.grid(row=2, column=0, padx=20, pady=20)

    stg_button = ctk.CTkButton(app, text="Settings", command=lambda: start(global_vars.SETTINGS_OPEN, settings))
    stg_button.grid(row=0, column=1, padx=20, pady=20)


    app.mainloop()

run()