#It will read the data from the './src'
# specially the 'Products'

import json

class FileAccess:
    def __init__(self,filename):
        self.filename = filename
    
    def read(self):
        #read_file_data:dict = ""
        file_path = self.filename
        try:
            with open(file_path,'r') as file:
                read_file_data = json.load(file)
                return read_file_data
        except (FileNotFoundError ,json.JSONDecodeError):
            print(f"ErrorType[FR001] : {file_path}. Return an empty list")
            return []
    def CreateFile(self,fileName):
        try:
            with open(fileName, 'x') as file:
                file.write("[]") # Set a array in .json file. Cuz it return as array/list.
                print(f"A new file had created name as : '{fileName}'")
        except json.JSONDecodeError:
                with open(fileName, 'w') as file:
                    file.write("[]")
                print("ErrorType[FW001] : I think file aleady exist :",fileName)
