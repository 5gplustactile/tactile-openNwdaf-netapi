from pymongo import MongoClient
import os

class MongoDatabase():
    def __init__(self):
        self.db = self.__connect()

    def __connect(self):
        uri = os.getenv("ME_CONFIG_MONGODB_URL")
        client = MongoClient(uri)

        try:
            mydb = client[os.getenv('MONGO_DB_NWDAF')]
            return mydb
        except Exception as e:
            print("An exception occurred ::", e)
            return None
    
    def get_coll(self, name):
        return self.db[name]