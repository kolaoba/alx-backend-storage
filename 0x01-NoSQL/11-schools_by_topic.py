#!/usr/bin/env python3
"""
Find schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic

    Args:
        mongo_collection (pymongo): collection object
        topic (str): topic to be searched
    """
    if mongo_collection is not None:
        search = {'topics': topic}
        return mongo_collection.find(search)
    return None
