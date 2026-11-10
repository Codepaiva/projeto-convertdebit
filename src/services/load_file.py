import pandas as pd
import re


class LoadFileService:
    def load_excel_file(self, file_selected):
        excel_file = pd.read_excel(file_selected, dtype=str, index_col=None, header=None).values
        
        return excel_file


    def check_date(self, row) -> str:
        
        # Seleciona o 1ª index da string
        row = row.split()[0]
        date_value = re.fullmatch(r'\d{4}.\d{2}.\d{2}', row, flags=re.ASCII)
        
        if date_value:
        
            # Seleciona o valor exato encontrado no fullmatch
            date_value = date_value.group(0)
            
            # Retorna uma lista com a data separada ['2019','11','12']
            replace_date = date_value.split('-')
            
            new_date = f'{replace_date[2]}/{replace_date[1]}/{replace_date[0]}'
            print(f'Data: {new_date}')
            
            return new_date
        
        return 'O campo "data" não é válido.'
    
    
    def check_value(self, row) -> str | None:
        # \D = qualquer caractere que não seja um dígito numérico
        # \d = qualquer caractere que seja um dígito numérico de 0 a 9
        amount = re.fullmatch(r'\d+|\d+[\.]\d+', row, flags=re.ASCII)
        
        
        
        if amount:
            print(f'Valor: {amount.group(0)}')
            return amount.group(0)
        else:
            print('O valor não e válido.')
    
 
    def check_type_value(self, row) -> str | None:
        type_value = re.fullmatch(r'[A-Z]', row)
        
        if type_value:
            if len(type_value.group(0)) == 1:
                if type_value.group(0) == "C" or type_value.group(0) == "D":
                    print(f'Tipo: {type_value.group(0)}')
                
                    return type_value.group(0)
                else:
                    return 'A coluna "tipo" deve conter "D" para débito e/ou "C" para crédito.'
            else:
                return 'O a coluna "tipo" deve ter apenas 1 (um) caractere.'
        else:
            return 'A coluna "Tipo" não é válida.'
    
    
    def get_data_verify(self, data) -> list[dict[str, str]] | None:
        self.laod_file_service = LoadFileService() 
        content = []
        
        print(f'{data}')
        for row in self.laod_file_service.load_excel_file(data):
            data = {
                'data': self.check_date(row[0]),
                'valor': self.check_value(row[1]),
                'tipo': self.check_type_value(row[2]),
            }
            
            content.append(data)
        
        return content