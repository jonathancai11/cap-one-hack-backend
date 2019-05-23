import json
from flask import Flask, Response, abort
from .utils import JSON_MIME_TYPE, search_book

app = Flask(__name__)

img_resp = {
    "Received image": "Goood stuff man",
}

hist_resp = {
    "Here are all of the history": "Goood stuff man",
}


insights_resp = {
    "Here are all of the insights": "Goood stuff man",
}



@app.route('/api/img')
def img_upload():
    response = Response(
        json.dumps(img_resp), status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.route('/api/history')
def book_detail():
    response = json.dumps(hist_resp)
    return response, 200, {'Content-Type': JSON_MIME_TYPE}


@app.route('/api/insights')
def insights():
    response = Response(
        json.dumps(insights_resp), status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.errorhandler(404)
def not_found(e):
    return '', 404
