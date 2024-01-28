import pymongo
clint = pymongo.MongoClient("mongodb://localhost:27017/")
print(clint)
db = clint.trial
collection = db.python_mongodb

# document={'name':'Ritik','branch':'cs','number':77}
# collection.insert_one(document)

# documents = [
#     {'id': 0, 'item': "large box", 'qty': 20},
#     {'id': 1, 'item': "small box", 'qty': 55},
#     {'id': 1, 'item': "medium box", 'qty': 30},
#     {'id': 2, 'item': "envelope", 'qty': 100},
#     {'id': 3, 'item': "stamps", 'qty': 125},
#     {'id': 3, 'item': "tape", 'qty': 20},
#     {'id': 4, 'item': "bubble wrap", 'qty': 30}
# ]
# collection.insert_many(documents)

# all_docs=collection.find({},{'_id':0})
# for i in all_docs:
#     print(i)

# all_databases=clint.list_database_names()
# print(all_databases)

# for i in clint.list_database_names():
#     print(i)

# docs=collection.find_one({},{'id':0})
# print(docs.count())
# print(docs)

# prev={"item":"large box"}
# nextt={"$set":{"qty":99}}
# collection.update_one(prev,nextt)