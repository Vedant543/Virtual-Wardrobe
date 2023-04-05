import os
import random
import pymongo
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

client = pymongo.MongoClient("mongodb+srv://vedantbhagat99:D9UiaCqouXF1uFSy@cluster0.qtleoda.mongodb.net/?retryWrites=true&w=majority")
db = client["wardrobe"]
top1 = db["Top"]
bottom1 = db["Bottom"]

with open("tops\images.jpg", "rb") as f:
    image_data = f.read()                                                                                           
document = {"imagedata": image_data}
top1.insert_one(document)

with open("tops\hmgoepprod.jpg", "rb") as f:
    image_data = f.read()                                                                                           
document = {"imagedata": image_data}
top1.insert_one(document)

with open("tops\hello.jpg", "rb") as f:
    image_data = f.read()                                                                                           
document = {"imagedata": image_data}
top1.insert_one(document)





with open("bottoms\images.jpg", "rb") as f:
    image_data = f.read()                                                                                           
document = {"imagedata": image_data}
bottom1.insert_one(document)

with open("bottoms\download.jpg", "rb") as f:
    image_data = f.read()                                                                                           
document = {"imagedata": image_data}
bottom1.insert_one(document)

with open("bottoms\world.jpg", "rb") as f:
    image_data = f.read()                                                                                           
document = {"imagedata": image_data}
bottom1.insert_one(document)