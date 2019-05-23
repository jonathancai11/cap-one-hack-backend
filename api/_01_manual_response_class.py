import json
from flask import Flask, Response, abort
from .utils import JSON_MIME_TYPE, search_book
from insight import make_insight_json
count = 0

app = Flask(__name__)

img_resp = {
    "words": "LOL"
}

@app.route('/api/img')
def img_upload():
    with open('api/data/demo.json') as json_file_demo:
        demo_json = json.load(json_file_demo)

    with open('api/data/history.json') as json_file_hist:
        history_json = json.load(json_file_hist)

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
    with open('api/data/history.json') as json_file_hist:
        history_json = json.load(json_file_hist)
    
    response = Response(
        json.dumps(history_json), status=200, mimetype=JSON_MIME_TYPE)
    return response

@app.route('/api/insights')
def insights():
    with open('api/data/insights.json', 'w') as json_file:  
        insights_resp = make_insight_json('api/data/history.json')
        json.dump(make_insight_json('api/data/history.json'), json_file, indent= 4)
         
    response = Response(
        json.dumps(insights_resp), status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.errorhandler(404)
def not_found(e):
    return '', 404
