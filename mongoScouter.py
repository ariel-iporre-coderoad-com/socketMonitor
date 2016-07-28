from pymongo import MongoClient
print "Connecting to mongod... "

uri = "mongodb://admin:control123!@localhost:27017"
client = MongoClient(uri)
print "Client Host                 : " + str(client.HOST)
print "Client Port                 : " + str(client.PORT)

db = client.riot_main

print "Primer database            : " + str(db)
collection = db.things
print "Primer database collections: " + str(collection)
cursor = collection.find({"serialNumber":"ITEMA2"})
print "Primer database cursor     : " + str(cursor)
cnt = 0
for thing in cursor:
    cnt += 1;
    print ":):):):):) thing (" + str(cnt) + ") : " + str(thing)



