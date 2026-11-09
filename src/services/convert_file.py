from services.create_dir import CreateDirService
from services.load_file import LoadFileService



class ConvertService:
    """
        Converte o conteúdo do arquivo excel para o arquivo txt
    """
    
    def __init__(self) -> None:
        self.create_dir_service = CreateDirService()
        self.get_data_file_service = LoadFileService()
    
        
    def convert_file_xlsx_to_txt(self, file: str):
        data_xlsx = self.get_data_file_service.get_data_excel_file(file)
        
        if data_xlsx is not None:
            # Coleta a data e hora atualizadas a cada iteração
            self.create_dir_service.update_today() 
            path = self.create_dir_service.create_path()
            date_now = self.create_dir_service.extract_complete_date_with_hour()
        
            file_path = path / f'Débitos - {date_now}.txt'
            
            with open(file_path, 'w', encoding="utf-8") as txt:
                txt.write("[DEBITO]\nSeMaFe=true\n")
                    
                for enum, info in enumerate(data_xlsx, start=1):
                    txt.write(f'Data{enum}={info["data"]}\n')
                    txt.write(f'Valor{enum}={info["valor"]}\n')
                    txt.write(f'Tipo{enum}={info['tipo']}\n')
                    