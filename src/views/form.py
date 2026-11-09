from tkinter import Frame, Label, Button, StringVar, messagebox
from services.search_file import SearchFileService
from services.convert_file import ConvertService


class Form:
    def __init__(self):
        self.conversion_service = ConvertService()
        self.file_service = SearchFileService()
        self.file_selected = None


    def window(self, app):
        self.app = app
        
        lb_name_file = Label(self.app, text="Converte Débito", background='gray87', font=("Poppins", 14, "bold"))
        lb_name_file.pack(fill='x')

        fr_div_infos = Frame(self.app, width=100, height=100, background="red")
        fr_div_infos.pack(fill='x', expand=1, padx=10)

        self.name_file = StringVar()
        self.name_file.set('Selecione um arquivo .xlsx para converter')
        self.lb_name_file = Label(fr_div_infos, textvariable= self.name_file, font=("Poppins", 9, "bold"))
        self.lb_name_file.pack(fill='x', expand=1)


        fr_div_buttons = Frame(self.app, width=100, height=100, background="gray37")
        fr_div_buttons.pack(fill='x', expand=1, padx=10)

        bt_select_file = Button(
            fr_div_buttons,
            text="Selecionar",
            height=1,
            bd=0,
            background='gray80',
            font=("Poppins", 9, "bold"),
            command= self.action_select_file
        )
        bt_select_file.pack(side='left', expand=1, padx=25)

        bt_write_file_txt = Button(
            fr_div_buttons, text="Converter",
            height=1,
            bd=0,
            background='gray80',
            font=("Poppins", 9, "bold"),
            command=self.action_convert_file
        )
        bt_write_file_txt.pack(side='left', expand=1)
        
        
    def action_select_file(self):
        data_file = self.file_service.select_file()
        
        if data_file is not None:
            self.file_selected = self.file_service.file_selected(data_file['path'])
            self.name_file.set(data_file['name'])
        else:
            messagebox.showwarning(title='Atenção', message='Arquivo não encontrado ou selecionado.')
        
        
    def action_convert_file(self):
        if self.file_selected is None:
            messagebox.showwarning(
                title='Atenção',
                message='Por favor, selecione o arquivo .xlsx para converter.'
            )
            return
            
        self.conversion_service.convert_file_xlsx_to_txt(self.file_selected)
        messagebox.showinfo(title='Sucesso', message='Arquivo convertido com sucesso!')
        