import flask
from flask import request, jsonify
from schedule_match import get_n_matches
from db import get_student, get_students

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return "Hello World!"


@app.route("/api/v1/matches", methods=["GET"])
def match_by_username():
    if "username" in request.args:
        username = request.args["username"]
    else:
        return "Error: No username provided"

    n = int(request.args.get("max", "5"))

    matches = get_n_matches(get_student(username), get_students(), n)
    return jsonify([m.toDict() for m in matches])


app.run()
