import flask
from flask import request, jsonify
import model

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/go', methods=["POST"])
def go():
    print(request)
    return jsonify(model.process(""))

app.run()