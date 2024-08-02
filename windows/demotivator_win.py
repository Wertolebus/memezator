import customtkinter as ctk
import functions as f
import global_vars
from generators import demotivator

def selectImageFunc() -> str:
    return ctk.filedialog.askopenfilename(filetypes=[("Images", ".png .jpg .jpeg")])

def run() -> None:
    global selected_img
    
    global_vars.DEMOTIVATOR_OPEN = 1
    app = ctk.CTk()
    app.title("Create Demotivator")
    app.geometry(f.center_window(app, 360, 140))
    app.resizable(0, 0)
    
    selected_img = ''

    def selectImage():
        global selected_img
        selected_img = selectImageFunc()
        if selected_img != '':
            create_button.grid(row=1, column=1, padx=20, pady=20)
    


    top_text = ctk.CTkEntry(app, placeholder_text="Top Text")
    top_text.grid(row=0, column=0, padx=20, pady=20)
    bottom_text = ctk.CTkEntry(app, placeholder_text="Bottom Text")
    bottom_text.grid(row=0, column=1, padx=20, pady=20)
    
    ctk.CTkButton(app, text="Select File...", command=selectImage).grid(row=1, column=0, padx=20, pady=20)
    create_button = ctk.CTkButton(app, text="Start!", command=lambda: demotivator.run(selected_img, top_text.get(), bottom_text.get()))
    create_button.grid(row=1, column=1, padx=20, pady=20)
    create_button.grid_forget()
    
        
    def on_closing():
        global_vars.DEMOTIVATOR_OPEN = 0
        print(selected_img)
        app.destroy()
        
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
