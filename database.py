import os
import pymongo
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
class Database():
    @staticmethod
    def connect ():
        load_dotenv()
        # Obtém as variáveis de ambiente
        host = os.getenv("MONGO_HOST")
        port = int(os.getenv("MONGO_PORT"))
        database = os.getenv("MONGO_DATABASE")

        # Constrói o URI de conexão
        mongo_uri = f"mongodb://{host}:{port}/{database}"

        # Criação do cliente MongoDB
        client = pymongo.MongoClient(mongo_uri)
        db = client["development"]

        return db, client
    
    @staticmethod
    def desconect(client):
        client.close()

    @staticmethod
    def insert_document(document, query, collection):
        db, client = Database.connect()
        collection = db[collection]

        collection.insert_one(document)

        Database.desconect(client)

    @staticmethod
    def find_document(query, collection):
        db, client = Database.connect()
        collection = db[collection]

        result = collection.find_one(query)

        Database.desconect(client)

        return result

    @staticmethod
    def update_document(query, collection, document):
        db, client = Database.connect()
        collection = db[collection]

        result = collection.update_one(query, document)

        Database.desconect(client)

        return result
    
    @staticmethod
    def delete_document(query, collection):
        db, client = Database.connect()
        collection = db[collection]

        result = collection.delete_one(query)

        Database.desconect(client)

        return result
# Restante do código continua como antes...
