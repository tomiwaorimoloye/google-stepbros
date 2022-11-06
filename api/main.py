import flask
from flask import request, jsonify
from flask_cors import CORS
from schedule_match import get_n_matches
from db import FirebaseDB

app = flask.Flask(__name__)
CORS(app)
fb = FirebaseDB()


@app.route("/", methods=["GET"])
def home():
    return "Hello World!"


@app.route("/api/v1/add", methods=["POST"])
def new_student():
    if request.method == "POST":
        username = request.form.get("username", "username")
        pwd = request.form.get("password", "pwd")
        faculty = request.form.get("faculty", "Faculty of Unknown")

        returnBody = {
            "username": username,
            "password": pwd,
            "faculty": faculty
        }

        if "file" in request.files:
            icsFile = request.files["file"]

            if icsFile.filename != "":
                try:
                    fb.add_student(username, pwd, icsFile.read(), faculty)

                    returnBody["data"] = "Success"
                except:
                    returnBody["data"] = "Couldn't access DB"

        return returnBody

    return "Stop trying to GET!"


@app.route("/api/v1/matches", methods=["GET"])
def match_by_username():
    if "username" in request.args:
        username = request.args["username"]
    else:
        return "Error: No username provided"

    n = int(request.args.get("max", "5"))

    matches = get_n_matches(fb.get_student(username), fb.get_students(), n)
    return jsonify([m.toDict() for m in matches])


if __name__ == "__main__":
    app.run(debug=True)
