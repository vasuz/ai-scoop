import requests
import json

def get_word_search(words):
    endpoint = "https://thewordsearch.com/api/pri/testapikey/save_word_search/"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "json": json.dumps({
            "title": "Vocab words",
            "desc": "Generated by The AI Scoop!",
            "wordlist": words
        })
    }

    response = requests.post(endpoint, data, headers=headers)
    response_id = json.loads(response.content).get('result', {}).get('id')
    
    image_url = f"https://thewordsearch.com/static/puzzle/word-search-{response_id}.png"
    return image_url