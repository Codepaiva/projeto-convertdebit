from tkinter import filedialog

from pathlib import Path


class SearchFileService:
    def select_file(self) -> dict[str , str ] | None:
        file = filedialog.askopenfilename(title="Selecione a planilha", filetypes=(("xlsx files", "*.xlsx"), ("", "")))
        
        if file:
            file = Path(file)
                
            data_file = {
                'path': file,
                'name': file.name,
            }

            
            return data_file
        
        return None

    
    def file_selected(self, file_name) -> str:
        self._file_name = file_name
        
        return self._file_name
    
    
    def get_file_selected(self) -> str:
        return self._file_name