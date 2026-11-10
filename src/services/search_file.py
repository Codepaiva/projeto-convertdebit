from tkinter import filedialog

from pathlib import Path


class SearchFileService:
    def select_file(self) -> dict[str , str] | None:
        file = filedialog.askopenfilename(title="Selecione uma planilha", filetypes=(("xlsx files", "*.xlsx"), ("", "")))
        
        if file:
            file = Path(file)
                
            data_file = {
                'path': file,
                'name': file.name,
            }

            
            return data_file
        
        return None