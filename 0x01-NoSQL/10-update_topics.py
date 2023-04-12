#!/usr/bin/env python3
"""
Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """updates all topics of a school document based on the name

    Args:
        mongo_collection (pymongo): collection object
        name (str): school name to be updated
        topics (List[str]): list of topics approached in the school
    """
    if mongo_collection is not None:
        search = {'name': name}
        newtopics = {'$set': {'topics': topics}}
        return mongo_collection.update_many(search, newtopics)
    return None
