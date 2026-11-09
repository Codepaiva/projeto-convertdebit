from datetime import datetime

import pathlib
import os.path


class CreateDirService:
    """
    Cria o diretório para armazenar os arquivos .txt
    """
    
    def __init__(self):
        self.today = datetime.now()
    
    
    def update_today(self):
        self.today = datetime.now()
    
    
    def extract_complete_date(self):
        date_extract = self.today.strftime("%d-%m-%Y")
        
        return date_extract
    
    
    def extract_complete_date_with_hour(self):
        
        date_extract = self.today.strftime("%d-%m-%Y__%H-%M-%S")
        
        return date_extract
    
    def extract_year_date(self):
        year = str(self.today.year)

        return year


    def extract_month_date(self):
        month = self.today.strftime('%m')

        return month


    def extract_day_date(self):
        day = self.today.strftime('%d')

        return day
    
    
    def create_path(self):
        path_root = pathlib.Path.cwd()

        path_records = path_root / 'data' / self.extract_year_date() / self.extract_month_date() / self.extract_day_date()

        if os.path.isdir(path_records):
            pass
        else:
            path_records.mkdir(parents=True, exist_ok=True)

        return path_records
            
    