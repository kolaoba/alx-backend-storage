#!/usr/bin/env python3
"""
List all documents in Python
"""


def list_all(mongo_collection):
    """
    List all documents in a collection
    """
    if mongo_collection is not None:
        return mongo_collection.find()
    return []
