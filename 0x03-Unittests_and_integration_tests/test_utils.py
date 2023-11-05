#!/usr/bin/env python3

"""Generic utilities
"""


import requests
from functools import wraps
from typing import (
        Mapping,
        Sequence,
        Any,
        Dict,
        Callable,
)

__all__ = [
        "access_nested_map",
        "get_json",
        "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.

    Parameters:
        nested_map (Mapping): A nested map.
        path (Sequence): A sequence of keys

    Example:
        >>> nested_map = {"a": {"b": {"c": 1}}}
        >>> access_nested_map(nested_map, ["a", "b", "c"])
        1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """Get JSON from a remote URL.

    Parameters:
        url (str): The URL to fetch JSON from

    Return:
        Dict: The JSON data obtained from URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method.
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
