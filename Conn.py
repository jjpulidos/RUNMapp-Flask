from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from bson.json_util import dumps
from dateutil import parser

from datetime import timedelta

def connection_Mongo(param={}):
    """
    connection_Mongo se encarga de conectar con la base de datos MongoDB y retorna una lista de estructuras JSON
    :return  Lista de Estructuras JSON correspondiente a las busquedas en la base de datos MongoDB:
    """
    client_mongo = MongoClient("mongodb+srv://RUNMapp-developer:POpeMXyP1DY6kaJR@production-cluster-say4a.mongodb.net/test?retryWrites=true")
    db_mongo = client_mongo['RUNMapp_DB']

    return db_mongo


# conn= connection_Mongo()

# print(dumps(conn["Buildings"].find({},{"name":1})))

# conn["EventsServices"].insert_one({
#    "name": "Charla «Diplomacia científica: el contexto integral y global acerca del Agua» (Dra. Angélica Gutiérrez-Magness)",
#    "description": "Conferencista: Dra. Angélica Gutiérrez-Magness, científica de la Administración Nacional Oceánica y Atmosférica (NOAA por sus siglas en inglés) de los Estados Unidos de América y profesora honoraria de la Universidad Nacional de Colombia.",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.now(),
#    "rate":  85.0,
#    "location": ObjectId("5c47ca1e6c0e8251cc5e9ee0"),
#    "finishDate": datetime.now() + timedelta(days=70030),
#    "isEvent": True,
#    "cat": "Sports"
# })

#


# conn["EventsServices"].update_one(
#     {
#         "_id": ObjectId("5c88a48a8ed97e000b964951")
#     },
#     {
#         "name": "Ronald",
#         "description": "Helloss",
#         "initDate": parser.parse("Thu Mar 28 2019 02:02:00 GMT-0500 (Colombia Standard Time)"),
#         "rate": 50,
#         "location": ObjectId("5c549598573ea33fb2afb773"),
#         "finishDate": parser.parse("Thu Mar 28 2019 02:02:00 GMT-0500 (Colombia Standard Time)"),
#         "isEvent": True,
#         "cat": "Sports"
#     })

