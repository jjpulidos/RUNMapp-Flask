from Conn import connection_Mongo
from datetime import datetime
from bson import ObjectId
from datetime import timedelta
from dateutil import parser
from bson.json_util import dumps

def db_filter(categories, distance, coordPoint, nameEventService, isEvent, initDate, finishDate, minRate, maxRate):
    # print(categories, distance, coordPoint, nameEventService, isEvent, initDate, finishDate, minRate, maxRate)
    pipeline = []
    listNearBuildings = None
    initDate=  datetime.fromtimestamp(initDate / 1e3)
    # print(initDate)
    finishDate=  datetime.fromtimestamp(finishDate / 1e3)

    coordPoint[0] = float(coordPoint[0])
    coordPoint[1] = float(coordPoint[1])
    # print(coordPoint[0], coordPoint[1], type(coordPoint[0]), type(coordPoint[1]))
    #initDate = datetime.now() - timedelta(days=7)
    #finishDate = datetime.now() + timedelta(days=7030)
    #minRate = 0.0
    #maxRate = 100.0

    conn = connection_Mongo()

    if(distance!=0):

        cursor = conn['Buildings'].find({
        'latlng.coordinates': {
            "$geoWithin": {
                "$centerSphere": [coordPoint, (distance / 1000) / 6378.1]}
        }
            }, {"_id": 1})

        print("La distancia es de: ", (distance/1000) / 6378.1)


        listNearBuildings = []
        listNameBuildings = []

        for record in cursor:
        # print(record)
            listNearBuildings.append(record["_id"])
        # print(record["_id"])
        print("Lista de Edificios Cercanos: ", listNearBuildings)

        pipeline.append(
            {
                "$project": {
                    "isNear": {"$in": ["$location", listNearBuildings]},
                    "name": "$name",
                    "description": "$description",
                    "photo": "$photo",
                    "initDate": "$initDate",
                    "finishDate": "$finishDate",
                    "rate": "$rate",
                    "isEvent": "$isEvent",
                    "cat": "$cat",
                    "location": "$location"
                }
            })

        pipeline.append({
            "$match": {
                "isNear": True
            }
        })

        # for record in conn["EventsServices"].find({}):
        #     print(record)

        print(len(list(conn['EventsServices'].aggregate(pipeline))))


    if (nameEventService != ""):
        pipeline.append(
            {
                "$match": {
                    "name": nameEventService,
            }})
    print(len(list(conn['EventsServices'].aggregate(pipeline))))
    if(categories!=""):
        pipeline.append(
            {
                "$match": {
                    "cat": {"$in": categories},
                }})

    print(len(list(conn['EventsServices'].aggregate(pipeline))))
    pipeline.append(
        {
            "$match": {
                "isEvent": isEvent,
               # "initDate": {"$lt": initDate},
               # "finishDate": {"$lte": finishDate},
                "rate": {"$gte": minRate, "$lte": maxRate},
            }})
    print(len(list(conn['EventsServices'].aggregate(pipeline))))
    pipeline.append(
        {
            "$project": {
                "name": "$name",
                "description": "$description",
                "photo": "$photo",
                "initDate": "$initDate",
                "finishDate": "$finishDate",
                "rate": "$rate",
                "isEvent": "$isEvent",
                "cat": "$cat",
                "location": "$location"
            }
        })

    result = list(conn['EventsServices'].aggregate(pipeline))

    buildings = []
    buildingsIDs= []

    for event in result:

        if not event["location"] in buildingsIDs:
            datos = list(conn["Buildings"].find({"_id": event["location"]}))

            buildings.append({
                "name": datos[0]["name"],
                "latlng": datos[0]["latlng"],
                "_id": str(datos[0]["_id"])
            })

            buildingsIDs.append( event["location"])

        event["_id"] = str(event["_id"])
        event["location"] = str(event["location"])
        event["initDate"] = str(event["initDate"])
        event["finishDate"] = str(event["finishDate"])

    return {
        "events": result,
        "buildings": buildings
    }



def db_add(name, isEvent, cat, description, location, initDate, finishDate):

    conn = connection_Mongo()

    response = conn["EventsServices"].insert_one({
        "name": name,
        "description": description,
        "initDate": parser.parse(initDate),
        "rate": 0.0,
        "location": ObjectId(location),
        "finishDate": parser.parse(finishDate),
        "isEvent": isEvent,
        "cat": cat
    })

    try:

        vari1= str(response)
        vari2 = str(response["insertedId"])
        vari3 = str(str(response["insertedId"]))


        return str(vari1 +vari2 +vari3)

    except:
        vari1 = str(response)
        vari2 = str(response["insertedId"])
        vari3 = str(str(response["insertedId"]))
        return "Hubo un Error :c " +str( vari1+ vari2 + vari3)


def db_update(name, isEvent, cat, description, location, initDate, finishDate):

    conn = connection_Mongo()

    try:

        conn["EventsServices"].update_one(
            {
                "name": name
            },
            {
                "description": description,
                "initDate": parser.parse(initDate),
                "rate":  "$rate",
                "location": ObjectId(location),
                "finishDate": parser.parse(finishDate),
                "isEvent": isEvent,
                "cat": cat
            })

        return "Se cambio la informacion con Exito"
    except:
        return "Hubo un Error"
