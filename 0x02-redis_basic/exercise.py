#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
from typing import Union, Callable, Optional

from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    decorator to count number of implementations of Cache methods
    """

    @wraps(method)
    def wrapper(*args, **kwargs):

        result = method(*args, **kwargs)
        key = method.__qualname__
        args[0]._redis.incr(key)
        return result

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    decorator to add input parametersand output parameters to
    different lists in redis
    """
    @wraps(method)
    def wrapper(*args, **kwargs):

        key = method.__qualname__
        args[0]._redis.rpush("{}:inputs".format(key), str(args[1:]))
        result = method(*args, **kwargs)
        args[0]._redis.rpush("{}:outputs".format(key), str(result))

        return result
    return wrapper


class Cache:
    """
    defines Cache class
    """

    def __init__(self) -> None:
        """
        initialize Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method to store input data using generated uuid key

        args:
            data (str | bytes | int | float): data to be stored

        returns:
            key (str): uuid4 g
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes,
                                                    int,
                                                    float,
                                                    None]:
        """
        method to retrieve stored data with optional conversion function

        args:
            key (str):
        """
        if not self._redis.get(key):
            return None

        if fn is None:
            return self._redis.get(key)

        return fn(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """
        method to retrieve stored value in str format
        """
        return str(self.get(key, lambda d: d.decode("utf-8")))

    def get_int(self, key: str) -> int:
        """
        method to retrieve stored value in int format
        """
        return self.get(key, int)
