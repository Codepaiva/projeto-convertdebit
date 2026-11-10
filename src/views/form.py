from tkinter import (
    Frame, Label, Button, StringVar, messagebox, ttk, NO
    )

from services.search_file import SearchFileService
from services.load_file import LoadFileService
from services.convert_file import ConvertService


class Form:
    def __init__(self):
        self.file_selected = None


    def window(self, app):
        self.app = app
        
        fr_div_title = Frame(self.app, width=100, height=100, background="red", highlightthickness=0.5, highlightbackground="#FFFFFF")
        fr_div_title.pack(fill='x', expand=1, padx=10)
        
        lb_name_file = Label(
            fr_div_title,
            text="Converte Débito",
            background='#3a3838',
            foreground='#FFFFFF',
            font=("Poppins", 14, "bold")
        )
        lb_name_file.pack(fill='x')

        
        
        fr_div_infos = Frame(self.app, width=100, height=100, background="#3a3838")
        fr_div_infos.pack(fill='x', expand=1, padx=10)

        self.name_file = StringVar()
        self.name_file.set('Selecione um arquivo .xlsx para converter')
        self.lb_name_file = Label(fr_div_infos, textvariable= self.name_file, font=("Poppins", 10, "bold"))
        self.lb_name_file.pack(fill='x', side='left', expand=1, pady=3)
        
        
        bt_select_file = Button(
            fr_div_infos,
            text="Selecionar",
            bd=0,
            background='gray80',
            font=("Poppins", 9, "bold"),
            command= self.action_select_file
        )
        bt_select_file.pack(fill='x', side='left', expand=1)
        

        fr_div_tree = Frame(self.app, width=100, height=100, background="gray37")
        fr_div_tree.pack(fill='x', expand=1, padx=10)
        
        self.ver_lista = ttk.Treeview(fr_div_tree, height=5, columns=('col1', 'col2', 'col3'))
        self.ver_lista.heading("#0", text='')
        self.ver_lista.heading("#1", text='Data')
        self.ver_lista.heading("#2", text='Valor')
        self.ver_lista.heading("#3", text='Tipo')
        
        self.ver_lista.column('#0', width=0, stretch=NO)
        self.ver_lista.column('#1', width=100, anchor="center") #n, ne, e, se, s, sw, w, nw, or center
        self.ver_lista.column('#2', width=100, anchor="center")
        self.ver_lista.column('#3', width=100, anchor="center")
        
        
        scroll = ttk.Scrollbar(fr_div_tree, orient="vertical", command=self.ver_lista.yview)
        self.ver_lista.configure(yscrollcommand=scroll.set)
        
        self.ver_lista.pack(fill='both', side='left', expand=1)
        scroll.pack(fill='y', side='left')
        
        
        fr_div_buttons = Frame(self.app, width=100, height=100, background="#3a3838")
        fr_div_buttons.pack(fill='x', expand=1, padx=10, pady=5)

        bt_write_file_txt = Button(
            fr_div_buttons, text="Converter",
            height=1,
            bd=0,
            background='gray80',
            font=("Poppins", 9, "bold"),
            command=self.action_convert_file
        )
        bt_write_file_txt.pack(side='bottom', expand=1)
        
        
    def action_select_file(self):
        self.file_service = SearchFileService()
        self.file = self.file_service.select_file()
        
        self.load_service = LoadFileService()
        
        if self.file is not None:
            self.name_file.set(self.file['name'])
            self.data = self.load_service.get_data_verify(self.file['path'])
            self.population_tree(self.data)
            
        else:
            messagebox.showwarning(
                title='Atenção',
                message='Arquivo não encontrado ou selecionado.'
            )
        
        
    def action_convert_file(self):
        self.conversion_service = ConvertService()
        
        
        if self.file is not None:
            if self.data is not None:
                self.conversion_service.convert_file_to_txt(self.data)
                messagebox.showinfo(
                    title='Sucesso',
                    message='Arquivo convertido com sucesso!'
                )
                
        else:
            messagebox.showwarning(
                title='Atenção',
                message='Por favor, selecione o arquivo .xlsx para converter.'
            )


    def population_tree(self, data):
        for item in self.ver_lista.get_children():
            self.ver_lista.delete(item)

        for row in data:
            self.ver_lista.insert(
                '',
                'end',
                values=(
                    row['data'],
                    row['valor'],
                    row['tipo']
                )
            )