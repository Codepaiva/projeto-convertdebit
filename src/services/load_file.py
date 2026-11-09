import re
import pandas as pd



# Construir trava para caso o usuário insira um arquivo com mais de 3 colunas ou menos que 3 colunas,
# além disso verificar se existem celulas vaizas ou outro tipo de valor (data | float | texto).
# A função deverá iterar sobre essas informações e checkar se eles estão no formato acima exemplificado.

class LoadFileService:
    def load_excel_file(self, file_selected):
        data_excel_file = pd.read_excel(file_selected, dtype=str, index_col=None, header=None).values
        
        print(f'{data_excel_file}')
        return data_excel_file
    
    
    def check_value_data(self, row) -> str:
        
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
    
    
    def check_value_amount(self, row) -> str | None:
        # \D = qualquer caractere que não seja um dígito numérico
        # \d = qualquer caractere que seja um dígito numérico de 0 a 9
        amount = re.fullmatch(r'\d+|\d+[\.]\d+', row, flags=re.ASCII)
        
        
        
        if amount:
            print(f'Valor: {amount.group(0)}')
            return amount.group(0)
        else:
            print('O valor não e válido.')
    
 
    def check_value_type_debit_credit(self, row) -> str | None:
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
    
    
    def get_data_excel_file(self, data) -> list[dict[str, str]] | None:
        content = []
        
        for row in self.load_excel_file(data):
            date = self.check_value_data(row[0])
            value = self.check_value_amount(row[1])
            type_debit_credit = self.check_value_type_debit_credit(row[2])
        
            data_debits = {
                'data': date,
                'valor': value,
                'tipo': type_debit_credit,
            }
            
            content.append(data_debits)
        
        return content
        