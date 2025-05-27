import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from schemas import Mentee, Mentor


URI = "mongodb+srv://be11-mini-project3:Ugi4z9QlPhECmBP2@be11-mini-project3.6fhgijo.mongodb.net/?retryWrites=true&w=majority&appName=be11-mini-project3"


def save_mentee(mentee: dict):
    try:
        client = MongoClient(URI, server_api=ServerApi('1'))
        db = client["mentor_matching"]
        collection = db["mentees"]
        mentee["owner_id"] = os.environ["OWNER_ID"]
        collection.insert_one(mentee)
    except Exception as e:
        raise RuntimeError(e)


def get_mentee_list() -> list[Mentee]:
    try:
        client = MongoClient(URI, server_api=ServerApi('1'))
        db = client["mentor_matching"]
        collection = db["mentees"]
        documents = list(collection.find({"owner_id": os.environ["OWNER_ID"]}))
        return [Mentee.from_dict(doc) for doc in documents]
    except Exception as e:
        raise RuntimeError(e)


def get_mentor_list() -> list[Mentor]:
    try:
        client = MongoClient(URI, server_api=ServerApi('1'))
        db = client["mentor_matching"]
        collection = db["mentors"]
        documents = collection.find()
        return [Mentor.from_dict(doc) for doc in documents]
    except Exception as e:
        raise RuntimeError(e)
