from pymongo import MongoClient
import os

class MongoDatabase():
    def __init__(self):
        self.db = self.__connect()
        self.data = self.__connect_data()

    def __connect(self):
        uri = os.getenv("ME_CONFIG_MONGODB_URL")
        client = MongoClient(uri)

        try:
            mydb = client[os.getenv('MONGO_DB_NWDAF')]
            return mydb
        except Exception as e:
            print("An exception occurred ::", e)
            return None
        
    def __connect_data(self):
        uri = "mongodb://" + os.getenv('MONGO_USER_WEBHOOK') + ":" + os.getenv('MONGO_PASS_WEBHOOK') + "@" + os.getenv('MONGO_HOST_WEBHOOK') + ":" + os.getenv('MONGO_PORT_WEBHOOK')
        client = MongoClient(uri)

        try:
            db = client[os.getenv('MONGO_DB_WEBHOOK')]
            return db
        except Exception as e:
            print("An exception occurred ::", e)
            return None
    
    def get_coll(self, name):
        return self.db[name]
    
    def get_coll_data(self, name):
        return self.data[name]
