import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/go')
def go():
    return jsonify({
        "hello": "world"
    })

app.run()