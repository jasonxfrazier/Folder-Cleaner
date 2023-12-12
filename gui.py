import customtkinter as ctk
from tkinter import filedialog
import main

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x70")
        self.title("Folder Cleaner")
        self.resizable(False, False)
        self.iconbitmap("favicon.ico")

        self.folder_button = ctk.CTkButton(master=self, text="Open File Path", command=self.open_explorer)
        self.folder_button.grid(row=0, column=0, padx=5, pady=15)

        self.clean_button = ctk.CTkButton(master=self, text="Clean Folder", fg_color="green",hover_color="darkgreen", command=self.clean_folder)
        self.clean_button.grid(row=0, column=1, padx=5, pady=15)
        
    def open_explorer(self):
        self.folder_path = filedialog.askdirectory()
        main.directory = self.folder_path
    
    def clean_folder(self):
        main.main()


app = App()
app.mainloop()