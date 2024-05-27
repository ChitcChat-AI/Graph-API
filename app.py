import re
from datetime import datetime

from flask import Flask
from flask import request
from flask_cors import CORS


from graph import Graph

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/graph", methods=["POST"])
def create_graph():
    return Graph(request.get_json()).create_graph()
