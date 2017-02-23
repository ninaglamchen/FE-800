from pymongo import MongoClient


def get_db():
    client = MongoClient("localhost", 27017)
    db_name = client.test
    return db_name


def get_collection(db):
    collection = db["robo_advisor"]
    print(collection)


def main():
    pass

if __name__ == "__main__":
    main()