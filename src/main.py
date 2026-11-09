from views.form import Form

import tkinter as tk


class App:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Converte débito")
        self.app["bg"] = 'gray37'
        self.app.geometry("450x100+100+100")
        self.app.resizable(False, False)
        
        self.form = Form()
        self.form.window(self.app)
        
        self.app.mainloop()
        
            

if "__main__" == __name__:
    app = App()