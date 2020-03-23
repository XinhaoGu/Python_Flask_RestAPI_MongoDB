import json 
from pathlib import Path

class jsonReaderHelper:
    # fields
    file_name = ""

    # constructor
    def __init__(self, file_name):
        self.file_name = file_name

    def GetJsonData(self):
        
        # read file
        data_folder = Path("../database")
        file_full_name = self.file_name + ".json"
        file_to_open = data_folder / file_full_name
        with open(file_to_open, 'r') as json_data_file:
            json_data = json_data_file.read()

        # parse file
        json_obj = json.loads(json_data)

        return json_obj
