#!/usr/bin/python3
# save this as app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return ('Hello, {escape(name)}!')
