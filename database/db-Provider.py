import json 

class DBHelper:
    # fields
    db_type = ""

    # constructor
    def __int__(self, db_type):
        self.db_type = db_type

    def GetConfigData: 
        # read file
        with open('dbConfig.json', 'r') as json_data_file:
            json_data = json_data_file.read()

        # parse file
        json_obj = json.loads(json_data)

        return json_obj
    
    def GetDBConfig: 
        db_obj = None
        db_config_obj = GetConfigData()
        for key in db_config_obj:
            if self.db_type == key 
                db_obj = db_config_obj[key]
        pass
        return db_obj

    def GetURI:
        db_config = GetDBConfig()
        # "mongodb://localhost:27017/myRetail"
        uri = "mongodb://" + db_config["host"] + 
            ":" + db_config["port"] + "/" + db_config["db"]
        return uri