from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

print("Establishing connection with the database".center(100, "-"))
myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ("myUserAdmin", "abc123"))
print("Connection established successfully: ", myclient)
mydb = myclient['test']
collection = mydb['student']

# cursor = collection.find()
#
# for record in cursor:
#     print(record)
#
# # delete one
# print("After Deletion")
# myquery = {'roll_number': 103}
# collection.delete_one(myquery)
# cursor = collection.find()
# for record in cursor:
#     print(record)

# delete many
# myquery = {'name': 'ram', 'roll_number': 104}
# collection.delete_many(myquery)
# cursor = collection.find()
# for record in cursor:
#     print('Deleting many records', record)

# deleting all the records
# myquery = {}
# collection.delete_many(myquery)
# cursor = collection.find()
# for record in cursor:
#     print('Deleting many records', record)

#inserting elements by list
# mylist = [
#             {
#                 "_id": 19,
#                 "name": "john",
#                 "roll_number": 103,
#                 "branch": "cse",
#                 "marks": 45
#             },
#             {
#                 "_id": 20,
#                 "name": "jenny",
#                 "roll_number": 108,
#                 "branch": "cse",
#                 "marks": 55
#             },
#             {
#                 "_id": 21,
#                 "name": "joe",
#                 "roll_number": 105,
#                 "branch": "cse",
#                 "marks": 55
#             }]
#
# collection.insert_many(mylist)
# cursor = collection.find()

#inserting records by dict
# records = {
#     "record1": {
#         "_id": 17,
#         "name": "rohan",
#         "roll_number": 103,
#         "branch": "cse",
#         "marks": 45
#     },
#     "record2": {
#         "_id": 18,
#         "name": "ram",
#         "roll_number": 104,
#         "branch": "cse",
#         "marks": 55
#     }
# }
# cursor = collection.find()
#
# for record in records.values():
#             collection.insert_one(record)
#
# for record in cursor:
#     print('Deleting many records', record)