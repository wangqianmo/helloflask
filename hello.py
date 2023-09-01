#!/usr/bin python
#encoding:utf-8

from flask import Flask,url_for,request

app=Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name="Him"):

    return f"<h1>Hello {name}!!!!</h1>"

@app.route("/hello")
def hello():
    name=request.args.get("name","XiaoMei")
    return f"<h1>Hello {name}!!!!</h1>"

if __name__ == '__main__':

    with app.test_request_context():
        print(url_for('index',name="Jime"))