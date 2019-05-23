import json
from flask import Flask, Response, abort
from .utils import JSON_MIME_TYPE, search_book

count = 0

app = Flask(__name__)


img_resp = {
    "Received image": "Goood stuff man",
}

with open('api/data/insights.json') as json_file:  
    insights_json = json.load(json_file)

with open('api/data/history.json') as json_file_hist:
    history_json = json.load(json_file_hist)

with open('api/data/demo.json') as json_file_demo:
    demo_json = json.load(json_file_demo)

insights_resp = insights_json
history_resp = history_json


@app.route('/api/img')
def img_upload():
    global count
    history_json.insert(0, demo_json[count])
    with open('history.json', 'w') as fb:
        json.dump(history_json, fb, indent= 4)
    response = Response(
        json.dumps(img_resp), status=200, mimetype=JSON_MIME_TYPE)
    count += 1
    return response


@app.route('/api/history')
def history():
    '''
    response = json.dumps(hist_resp)
    return response, 200, {'Content-Type': JSON_MIME_TYPE}
    '''
    response = Response(
        json.dumps(history_resp), status=200, mimetype=JSON_MIME_TYPE)
    return response

@app.route('/api/insights')
def insights():
    response = Response(
        json.dumps(insights_resp), status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.errorhandler(404)
def not_found(e):
    return '', 404
