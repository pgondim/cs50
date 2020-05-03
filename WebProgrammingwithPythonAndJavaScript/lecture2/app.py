from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/",  methods= ["GET","POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html",notes=session["notes"])


# @app.route("/outro", methods= ["GET","POST"] )
# def outro():
#    name = request.form.get("name")
#    if request.method == "GET":
#        return "Envie seu nome"
#
#    return render_template("outro.html", name=name)



# @app.route("/<string:name>")
# def hello(name):
#    return f"Hello, {name}!!"


