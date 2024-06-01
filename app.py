from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify

from graph import Graph

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/graph/", methods=["POST", "OPTIONS"])
@cross_origin()
def create_graph():
    if request.method == "OPTIONS":
        response = jsonify({})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response
    else:
        return Graph(request.get_json()).create_graph()
