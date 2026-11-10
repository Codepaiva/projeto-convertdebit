from services.create_dir import CreateDirService


class ConvertService:
    def convert_file_to_txt(self, file) -> None:
        self.create_dir_service = CreateDirService()
        
        
        if file is not None:
            # Coleta a data e hora atualizadas a cada iteração
            self.create_dir_service.update_today() 
            path = self.create_dir_service.create_path()
            date_now = self.create_dir_service.extract_complete_date_with_hour()
            
            file_path = path / f'Débitos - {date_now}.txt'
                
                
            with open(file_path, 'w', encoding="utf-8") as txt:
                txt.write("[DEBITO]\nSeMaFe=true\n")
                        
                for enum, info in enumerate(file, start=1):
                    txt.write(f'Data{enum}={info['data']}\n')
                    txt.write(f'Valor{enum}={info['valor']}\n')
                    txt.write(f'Tipo{enum}={info['tipo']}\n')
        
        else:
            return None   