from pymongo import MongoClient
import os

class MongoDatabase():
    def __init__(self):
        self.client = None
        self.db = self.__connect()

    def __connect(self):
        uri = "mongodb://" + os.getenv('MONGO_USER_WEBHOOK') + ":" + os.getenv('MONGO_PASS_WEBHOOK') + "@" + os.getenv('MONGO_HOST_WEBHOOK') + ":" + os.getenv('MONGO_PORT_WEBHOOK')
        client = MongoClient(uri)

        try:
            mydb = client[os.getenv('MONGO_DB_WEBHOOK')]
            return mydb
        except Exception as e:
            print("An exception occurred ::", e)
            return None
    
    def get_coll(self, name):
        return self.db[name]
