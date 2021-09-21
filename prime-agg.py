from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

print("Establishing connection with the database".center(100, "="))
myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ("myUserAdmin", "abc123"))
print("Connection established successfully: ", myclient)

mydatabase = myclient['database']

mycollection = mydatabase['test3']

mycollection.delete_many({})

sample_data = [{"x": 1, "tags": ["dog", "cat"]},
               {"x": 2, "tags": ["cat"]},
               {"x": 2, "tags": ["mouse", "cat", "dog"]},
               {"x": 3, "tags": []}]

result = mycollection.insert_many(sample_data)

from bson.son import SON

pipeline = [
    { "$unwind": "$tags" }, #1. Make a flat hierarchy
    { "$group": { "_id": "$tags", "count": { "$sum": 1 } } }, #2. Actual Aggregation
    { "$sort": SON( [("count", -1) , ("_id", -1) ] ) } #3. Display
]

import pprint
print("Aggregation Pipeline".center(100, "="))
pprint.pprint(list(mycollection.aggregate(pipeline)))
print("".center(100, "="))


