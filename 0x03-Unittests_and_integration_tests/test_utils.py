#!/usr/bin/env python3

""" Class that inherits from unnittest.TestCase
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the map."),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the map."),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            expected_exception_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        exception_message = str(context.exception)
        self.assertEqual(exception_message, expected_exception_message)


if __name__ == '__main__':
    unittest.main()
