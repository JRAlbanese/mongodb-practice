#!/bin/bash  python3

from pymongo import MongoClient, errors
import os
import json
from bson.json_util import dumps

MONGOPASSn = os.getenv('MONGOPASSn')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/pwg2gq"
client =  MongoClient(uri, username='nmagee', password=MONGOPASSn, connectTimeoutMS=200, retryWrites=True)


db = client["pwg2gq"]

lab_collection = db["bands"] #band's name, year created, famous song

db.bands.insertOne({"band_name":"Eagles", "founded": "1971", "2_popular_songs": ["Take it easy", "Hotel California"]})
db.bands.insertOne({"band_name":"The Beatles", "founded": "1960", "2_popular_songs": ["Hey Jude", "Let It Be"]})
db.bands.insertOne({"band_name":"Led Zeppelin", "founded": "1968", "2_popular_songs": ["Stairway to Heaven", "Whole Lotta Love"]})
db.bands.insertOne({"band_name":"Queen", "founded": "1970", "2_popular_songs": ["Bohemian Rhapsody", "Another One Bites the Dust"]})
db.bands.insertOne({"band_name":"Pink Floyd", "founded": "1965", "2_popular_songs": ["Wish You Were Here", "Comfortably Numb"]})

first_3_lines = lab_collection.find().limit(3)

#for loop to show each doc by itself among the 3
x = 0

for each in first_3_lines:
    print(each)