from pymongo import MongoClient

def connection_Mongo(param={}):
    """
    connection_Mongo se encarga de conectar con la base de datos MongoDB y retorna una lista de estructuras JSON
    :return  Lista de Estructuras JSON correspondiente a las busquedas en la base de datos MongoDB:
    """
    client_mongo = MongoClient("mongodb+srv://RUNMapp-developer:POpeMXyP1DY6kaJR@production-cluster-say4a.mongodb.net/test?retryWrites=true")
    db_mongo = client_mongo['RUNMapp_DB']

    return db_mongo

# conn= connection_Mongo()