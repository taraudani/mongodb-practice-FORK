#!/usr/bin/env python3

from pymongo import MongoClient
from bson.json_util import dumps
import os
from db import *
from pymongo.server_api import ServerApi

uri = "mongodb+srv://taraudani@cluster0.nr0mo.mongodb.net/hav7tz?retryWrites=true&w=majority&appName=Cluster0"
password = os.getenv('MONGOPASS')
client = MongoClient(uri, username='taraudani', password= password, connectTimeoutMS=200, retryWrites=True)

db = client["hav7tz"]
collection = db["characters"]

characters_data = [
    {"name": "Jess", "age": 30, "hair color": "brown", "home": "loft"},
    {"name": "Nick", "age": 31, "hair color": "brown", "home": "loft"},
    {"name": "Schmidt", "age": 29, "hair color": "black", "home": "loft"},
    {"name": "Winston", "age": 30, "hair color": "black", "home": "loft"},
    {"name": "Cece", "age": 30, "hair color": "black", "home": "apartment"}
]

collection.insert_many(characters_data)

query = {"hair color": "black"}

characters_cursor = collection.find(query).limit(3)

for character in characters_cursor:
    print(character)

