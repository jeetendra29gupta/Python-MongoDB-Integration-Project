import pymongo

# MongoDB Connection Setup
mongodb_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongodb_database = mongodb_client["my_first_database"]  # Select/Create a database
mongodb_collection = mongodb_database["my_first_collection"]  # Select/Create a collection
