import flask
from flask import request, jsonify
import model

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/go', methods=["POST"])
def go():
    url = request.args.get('url')
    if url:
        return jsonify(model.process(url))
    else:
        return jsonify("Please provide a valid URL.")

app.run()