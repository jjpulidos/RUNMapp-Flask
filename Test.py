from flask import Flask, request, render_template
from Conn import connection_Mongo
from bson import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

def db_getEvents(building):

    conn = connection_Mongo()
    db_locationID = conn['Buildings'].find({"name": building}, {"_id": 1})

    return conn['EventsServices'].find({
        "location": ObjectId(db_locationID.next()["_id"])
    })

@app.route('/')
def index():
    return render_template('Button.html')

@app.route('/getEvents', methods=['POST', 'GET'])
def getEvents():
    error = None
    building = request.form['edificio']
    if request.method == 'POST':
        db_response = db_getEvents(building)
        if db_response != None:
            return dumps(db_response)
        else:
            error = 'Invalid username/password'
    return render_template('Button.html', error=error)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
