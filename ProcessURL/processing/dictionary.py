import requests
import json
from utils import get_config

MERRIAM_WEBSTER_KEY = "merriam-webster-api-key";

def get_definition_merriam(word):
    # This should be fetched from some appsettings file
    key = get_config(MERRIAM_WEBSTER_KEY);
    url = "https://dictionaryapi.com/api/v3/references/sd2/json/" + word + "?key=" + key;

    response = requests.get(url);

    # We hardcode this to get the top response. It's possible another definition is necessary?
    data = json.loads(response.content)[0];

    definition = "\n".join(data["shortdef"]);
    return definition;