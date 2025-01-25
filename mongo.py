from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime


uri = "mongodb://username:password@localhost:27017/main"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client["university"]
collection = database["information"]
documents = collection.find()

def ping():
    try:
        client.admin.command('ping')
        print("Connected to MongoDB")
    except Exception as e:
        print(e)

def get_documents():
    try:
        d = []
        for document in documents:
            d.append(document)
        return d
    except Exception as e:
        print(e)

def insert(user, route, ip, args):
    try:
        document = {
            "name": user,
            "route": route,
            "IP": ip,
            "args": args,
            "date": datetime.now()
        }
        collection.insert_one(document)
    except Exception as e:
        print(e)

def delete():
    try:
        collection.delete_many({})
    except Exception as e:
        print(e)

if __name__ == '__main__':
    delete()