from flask import Flask, json, request, render_template, Response
from Conn import connection_Mongo
from filters import db_filter, db_add
from bson import ObjectId
from bson.json_util import dumps


from flask_cors import *

app = Flask(__name__)
cors = CORS(app)


def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/getEvents', methods=['POST', 'GET'])
@cross_origin()
def getEvents():
    error = None
    print(request)
    data = json.loads(request.data)

    print(data)
    if request.method == 'POST':
        db_response = db_filter(data["categories"], data["distance"], data["coordPoint"], data["nameEventService"],
                             data["isEvent"], data["initDate"], data["finishDate"], data["minRate"], data["maxRate"])
        if db_response != None:
            print(dumps(db_response))
            resp = Response(dumps(db_response), status=200, mimetype='application/json')
            # resp.headers['Link'] = 'http://192.168.1.118:5000'
            return resp
        else:
            error = 'Invalid username/password'
    return render_template('Button.html', error=error)


@app.route('/addEvents', methods=['POST', 'GET'])
@cross_origin()
def addEvents():

    data = json.loads(request.data)
    # print(data)

    return db_add(data["name"], data["isEvent"], data["cat"], data["description"], data["location"], data["initDate"],
           data["finishDate"])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
