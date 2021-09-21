# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    try:
        print("Establishing connection with the database".center(100, "-"))
        myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('myUserAdmin', 'abc123'))
        print("Connection established successfully: ", myclient)

        # Printing the databases
        list_of_db = myclient.list_database_names()
        print("Databases available in mongodb: ", list_of_db)

        # create new database in mongodb
        mydb = myclient['test']
        print("Database created...", mydb)

        #one way of inserting records (one record at a time)
        #create collection (like a table)
        # collection = mydb['student']
        # record = {
        #     "_id":0,
        #     "name": "raj",
        #     "roll_number": 101,
        #     "branch": "cse",
        #     "marks": 40
        # }
        # record_1 = collection.insert_one(record)
        # print("records", record_1)

        # list down the databases
        list_of_db = myclient.list_database_names()
        print("Databases available in mongodb after creation: ", list_of_db)

        # Inserting multiple records in a collection (dictionary)
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

        # #create collection (insertion logic)
        # collection = mydb['student']
        # for record in records.values():
        #     collection.insert_one(record)

        #Inserting multiple records in a collection (list)
        # mylist = [
        #     {
        #         "_id": 19,
        #         "name": "john",
        #         "roll_number": 103,
        #         "branch": "cse",
        #         "marks": 45
        #     },
        #     {
        #         "_id": 20,
        #         "name": "jenny",
        #         "roll_number": 108,
        #         "branch": "cse",
        #         "marks": 55
        #     },
        #     {
        #         "_id": 21,
        #         "name": "joe",
        #         "roll_number": 105,
        #         "branch": "cse",
        #         "marks": 55
        #     }
        #
        # ]
        #insertion logic
        collection = mydb['student']
        #collection.insert_many(mylist)

        # 3 find the  document display document (one document in the collection)
        # x = collection.find_one()
        # print("One Record: ", x)

        # Finding all the documents in a collection
        all_document = collection.find()
        for each_record in all_document:
            print("doc", each_record)

        # Printing only custom attributes for all the documents in a collection
        # for x in collection.find({}, {"_id": 0, "name": 1, "branch": 1}):
        #     print("Only fields with 1: ", x)

        # Applying conditions on attributes
        # curson = collection.find({"marks": {"$gt": 45}})
        # print("The records greater than 45: ")
        # for record in curson:
        #   print("records:%s" % record)

        # cursor = collection.find({"marks": {"$lt": 45}})
        # print("The records less than 45: ")
        # for record in cursor:
        #    print("records:%s" % record)

        # search or display records in between
        # print('search or display records in between')
        # ob = collection.find({"$and":[{"marks":{"$gt":40}}, {"marks":{"$lt":50}}]})
        # print("And conditions records: ")
        # for record in ob:
        #    print("records", record)
        #
        # ob = collection.find({"$or":[{"marks":{"$gt":40}}, {"marks":{"$lt":50}}]})
        # print("Or conditions records: ")
        # for record in ob:
        #    print("records", record)

        # sorting
        print("Sorted on name")
        #ascending
        # mydoc = collection.find().sort("name")
        # for x in mydoc:
        #    print("sorting..", x)

        #descending
        # mydoc = collection.find().sort("name", -1)
        # for x in mydoc:
        #     print("sorting..", x)

        # 1. connectivity to mongodb
        # 2. create database in mongodb
        # 3. create collections in mongodb
        # 4. insert - insert_one, insert_many
        # 5. find - find_one, find
        # 6. find- display particular attributes records
        # 7. find -- conditional formating using and or gt, lt
        # home work explore operator in pymongo
        # 8. Sorting how to sort on fields of the documents

        # update one record based on some condition

        # filter = {'roll_number': 104}
        # newvalues = {"$set": {"marks": 35}}
        # collection.update_one(filter, newvalues)
        # all_document = collection.find()
        # for each_record in all_document:
        #    print("doc", each_record)

        # upsert

        collection.update_many(
            {
                "marks": {
                    "$gt": 40
                }
            },
            {
                "$set": {
                    "address": "pune"
                }
            }
        )
        print("Updated records.....")
        cursor = collection.find()
        for record in cursor:
            print(record)

        """ # 2 create student database, employee db

          1. ask the choice to user 
          1. create the records(insert the record)
          2. find the record by using specific field
          3. display all records
          4. update the records

        # class, function """

    except ConnectionFailure as e:
        print("Error: ", e)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


