import json 
import os
from pathlib import Path

class jsonWriterHelper:
    # fields
    file_name = ""
    json_data = []

    # constructor
    def __init__(self, file_name, json_data):
        self.file_name = file_name
        self.json_data = json_data

    def PostJsonData(self):
        # read file
        data_folder = Path("../database")
        file_full_name = self.file_name + ".json"
        file_to_open = data_folder / file_full_name
        exists = os.path.isfile(file_to_open)
        try: 
            if exists:
                with open(file_to_open, 'w') as json_data_file:
                    json.dump(self.json_data, json_data_file)

                    return self.json_data
                pass
        except FileNotFoundError: 
            return {"Posting product failed - on writting to product.json"}, 500
            pass


