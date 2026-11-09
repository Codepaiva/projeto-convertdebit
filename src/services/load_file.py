import re
import pandas as pd



# Construir trava para caso o usuário insira um arquivo com mais de 3 colunas ou menos que 3 colunas,
# além disso verificar se existem celulas vaizas ou outro tipo de valor (data | float | texto).
# A função deverá iterar sobre essas informações e checkar se eles estão no formato acima exemplificado.

class LoadFileService:
    def load_excel_file(self, file_selected):
        data_excel_file = pd.read_excel(file_selected, dtype=str, index_col=None, header=None).values
        
        print(data_excel_file)
        return data_excel_file
    
    
    def check_value_data(self, row) -> str:
        date_default = re.fullmatch(r'\d{4}.\d{2}.\d{2}', row)
        print(date_default)
        
        if date_default == True:
            date = row.split()[0]
            replace_data = date.replace('-', '/').split('/')
            new_date = f'{replace_data[2]}/{replace_data[1]}/{replace_data[0]}'
            
            return new_date
        
        return 'O formato deve ser data.'
    
    
    def check_value_amount(self, row) -> str | None:
        print(row)
        amount_default = re.fullmatch(r'\D', row)
        print(amount_default)
        
        if amount_default == True:
            return row
    
    
    def check_value_type_debit_credit(self, row) -> str | None:
        type_debit_credit_default = re.fullmatch(r'[A-Z]', row)
        
        
        if type_debit_credit_default == True:
            if len(row) == 1:
                type_debit_credit = row
                
                return type_debit_credit
            else:
                return 'O tipo deve ter apenas 1 (um) caractere'
        else:
            return 'O tipo deve ser "D" para débito e/ou "C" para crédito'
    
    
    
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
        