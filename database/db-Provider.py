import json 
from pathlib import Path

class DBHelper:
    # fields
    db_type = ""

    # constructor
    def __init__(self, db_type):
        self.db_type = db_type

    def GetConfigData(self): 
        # read file
        data_folder = Path("../database")
        file_to_open = data_folder / "dbConfig.json"
        with open(file_to_open, 'r') as json_data_file:
            json_data = json_data_file.read()

        # parse file
        json_obj = json.loads(json_data)

        return json_obj
    
    def GetDBConfig(self): 
        db_obj = None
        db_config_obj = self.GetConfigData()
        for key in db_config_obj:
            if self.db_type == key 
                db_obj = db_config_obj[key]
        pass
        return db_obj

    def GetURI(self):
        db_config = self.GetDBConfig()
        # "mongodb://localhost:27017/myRetail"
        uri = "mongodb://" + db_config["host"] + ":" + db_config["port"] + "/" + db_config["db"]
        return uri