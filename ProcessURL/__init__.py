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
            "authors": proc.get_authors(),
            "title": proc.get_heading(),
            "summary": proc.get_summary(),
            "image_url": proc.get_image(),
            "ws_puzzle_url": proc.get_word_search(),
            "vocabulary": proc.get_keyword_definitions()
        }

        return func.HttpResponse(jsonify(result), mimetype="application/json")