import logging

import azure.functions as func
from ProcessURL.processing import processor
from json import dumps as jsonify

# need to separate __init__.py so this only runs once?
import nltk
nltk.data.path.append('./nltk_data')

def main(req: func.HttpRequest) -> func.HttpResponse:
    url = req.params.get('url')

    if not url:
        return func.HttpResponse("Please provide a valid URL.", status_code=400)
    else:
        proc = processor.Processor(url)

        result = {
            "authors": proc.authors(),
            "title": proc.heading(),
            "summary": proc.summarize(),
            "image_url": proc.image(),
            "ws_puzzle_url": "imageurlhere",
            "cw_puzzle_url": "imageurlhere",
            "dictionary": proc.keyword_defs()
        }

        return func.HttpResponse(jsonify(result), mimetype="application/json")