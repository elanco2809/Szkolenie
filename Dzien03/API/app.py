
from flask import Flask, request, jsonify

app = Flask("app")

@app.route("/")
def hello():
    return "<h1>Hello world!</h1>"

@app.route("/echo/<ping>", methods=['POST','GET'])
def resp_ping(ping):
    return f"<h1>{ping}<h1>"

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
