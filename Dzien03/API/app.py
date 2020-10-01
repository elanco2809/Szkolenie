
from flask import Flask, request, jsonify, make_response, render_template, flash, send_file
import uuid
from werkzeug.utils import secure_filename
import secrets
import os
import re
import glob

app = Flask("app")

def create_response(message, code):
    resp = make_response(jsonify(message), code)
    resp.mimetype = "application/json"
    return resp

@app.route("/")
def hello():
    return "<h1>Hello world!</h1>"

@app.route("/echo/<ping>", methods=['POST','GET'])
def resp_ping(ping):
    return f"<h1>{ping}<h1>"


@app.route("/login", methods=['POST'])
def login():
    try:
        username = request.args.get("user","")
        password = request.args.get("pass","")
        if username=="admin" and password=="qwerty123":
            token = uuid.uuid5(uuid.NAMESPACE_X500, str(uuid.uuid4()) )
            resp = {"status":"OK", "token": token}
            return create_response(resp, 200)
        else:
            resp = {"status":"ERROR", "msg":"Not valid username/password"}
            return create_response(resp, 403)
    except Exception as exc:
        resp = {"status": "ERROR", "msg": str(exc)}
        return create_response(resp, 500)

# WmWsp34eTo_LR1S0LyeGg

@app.route("/get/<string:token>")
def get_file(token):
    mask = f"uploads/{token}-*.*"
    files = glob.glob(mask)
    if len(files)==0:
        return create_response({ "status":"ERROR", "msg":"Not found" }, 404)
    return send_file(files[0], as_attachment=True)

@app.route("/upload", methods=['POST','GET'])
def upload_file():
    if request.method == "POST":
        if "picture" not in request.files:
            #brak pliku
            return render_template("upload.html", message="Wybierz plik" )
        file = request.files["picture"]
        file_name = file.filename
        token = re.sub("\W", "", secrets.token_urlsafe(16))
        new_file = os.path.join("uploads", f"{token}-{secure_filename(file_name)}")
        file.save(new_file)
        return render_template("upload.html", message=token)

    return render_template("upload.html")

@app.after_request
def add_headers(response):
    response.headers["Server"] = "My Own Server"
    response.headers["App-Id"] = "API Server"
    return response

@app.after_request
def add_headers1(response):
    response.headers["Expires"] = 0
    return response

app.run(debug=True)
