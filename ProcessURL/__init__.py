import azure.functions as func
from ProcessURL.processing.article_processor import ArticleProcessor
from json import dumps as jsonify

import nltk
nltk.data.path.append('./nltk_data')

def main(req: func.HttpRequest) -> func.HttpResponse:
    url = req.params.get('url')

    if not url:
        return func.HttpResponse("Please provide a valid URL.", status_code=400)
    else:
        proc = ArticleProcessor(url)

        result = {
            "authors": proc.authors(),
            "title": proc.heading(),
            "summary": proc.summarize(),
            "image_url": proc.image(),
            "ws_puzzle_url": proc.word_search(),
            "dictionary": proc.keyword_defs()
        }

        return func.HttpResponse(jsonify(result), mimetype="application/json")