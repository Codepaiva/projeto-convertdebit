from views.form import Form

import tkinter as tk


class App:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Converte débito")
        self.app["bg"] = "#3a3838"
        self.app.geometry("400x232+100+100")
        self.app.resizable(False, False)
        
        self.form = Form()
        self.form.window(self.app)
        
        
        self.app.mainloop()