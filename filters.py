from Conn import connection_Mongo
from datetime import datetime
from bson import ObjectId
from datetime import timedelta
from dateutil import parser

def db_filter(categories, distance, coordPoint, nameEventService, isEvent, initDate, finishDate, minRate, maxRate):

    pipeline = []
    listNearBuildings = None
    initDate=  datetime.datetime.fromtimestamp(initDate / 1e3)
    finishDate=  datetime.datetime.fromtimestamp(finishDate / 1e3)
    # print(categories, distance, coordPoint, nameEventService, isEvent, initDate, finishDate, minRate, maxRate)
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

        # print(list(conn['EventsServices'].aggregate(pipeline)))
    if (nameEventService != ""):
        pipeline.append(
            {
                "$match": {
                    "name": nameEventService,
                    "isEvent": isEvent,
                    "cat": {"$in": categories},
                    "initDate": {"$lte": initDate},
                    #"finishDate": {"$lt": finishDate},
                    "rate": {"$gte": minRate, "$lte": maxRate},
                }})
    else:
        pipeline.append(
            {
                "$match": {
                    "isEvent": isEvent,
                    "cat": {"$in": categories},
                    #"initDate": {"$lte": initDate},
                    #"finishDate": {"$lt": finishDate},
                    "rate": {"$gte": minRate, "$lte": maxRate},
                }})

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



    for event in result:
        event["_id"] = str(event["_id"])
        event["location"] = str(event["location"])
        event["initDate"] = str(event["initDate"])
        event["finishDate"] = str(event["finishDate"])



    return result



def db_add(name, isEvent, cat, description, location, initDate, finishDate):

    conn = connection_Mongo()

    conn["EventsServices"].insert_one({
       "name": name,
       "description": description,
       "photo": "link to Google/Drive/Path/Image",
       "initDate": parser.parse(initDate),
       "rate":  0,
       "location": ObjectId(location),
       "finishDate": parser.parse(finishDate),
       "isEvent": isEvent,
       "cat": cat
    })
    return