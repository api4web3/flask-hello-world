from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from getkey import getKey

def connectDb():
    uri = "mongodb+srv://api4web3:" + getKey() + "@cluster0.fpk98fo.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        return "Pinged your deployment. You successfully connected to MongoDB!"
    except Exception as e:
        print(e)
        return "Error"

if __name__ == '__main__':
    connectDb()
