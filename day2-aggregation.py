from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

print("Establishing connection with the database".center(100, "-"))
myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ("myUserAdmin", "abc123"))
print("Connection established successfully: ", myclient)

mydatabase = myclient['database']

mycollection = mydatabase['myTable']

# profiles = [
#     {"user": "Ram", "title": "Python"},
#     {"user": "Raj", "title": "Javascript"},
#     {"user": "Ram", "title": "c++"},
#     {"user": "John", "title": "MongoDB"},
#     {"user": "Rohan", "title": "Perl"},
# ]
# mycollection.insert_many(profiles)

records = mycollection.find()
for record in records:
    print(record)

# perform aggregation

# agg_result = mycollection.aggregate(
#     [
#         {
#             "$group":
#                 {
#                     "_id": "$user",
#                     "num_lang": {"$sum": 1}
#                 }
#         }
#     ]
# )
agg_result = mycollection.aggregate(
    [
        {
            "$group":
                {
                    "_id": "$title",
                    "occurences": {"$sum": 1}
                }
        }
    ]
)

print("Aggregation Result".center(100, "="))
for doc in agg_result:
    print(doc)