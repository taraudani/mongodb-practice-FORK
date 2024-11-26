#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *
from pymongo.server_api import ServerApi

uri = "mongodb+srv://taraudani:<db_password>@cluster0.nr0mo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

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

print("Displaying 3 documents where hair color is black:")
for character in characters_cursor:
    print(character)

client.close()
