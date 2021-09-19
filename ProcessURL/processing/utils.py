import json

CONFIG_FILE = "appconfig.json"

def get_config(option):
    with open(CONFIG_FILE) as json_file:
        data = json.load(json_file)
        return(data[option])