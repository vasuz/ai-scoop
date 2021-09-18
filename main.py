import flask
from flask import request, jsonify

import model
from validators import url as valid_url

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/go', methods=["POST"])
def go():
    url = request.args.get('url')

    if valid_url(url):
        return jsonify(model.process(url))
    else:
        return jsonify("Please provide a valid URL.")

app.run()