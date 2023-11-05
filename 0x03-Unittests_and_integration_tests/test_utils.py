#!/usr/bin/env python3

""" Class that inherits from unnittest.TestCase
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    A test class for the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with various inputs

        Parameters:
            nested_map (dict): The nested map to access.
            path (tuple): The path to access in the map.
            expected_result (any): Expected result
        """
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
        """
        Test that the access_nested_map function raises a KeyError

        Parameters:
            nested_map (dict): The nested map to access.
            path (tuple): The path to access in the map.
            expected_exception_message (str): The expected error.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        exception_message = str(context.exception)
        self.assertEqual(exception_message, expected_exception_message)


class TestGetJson(unittest.TestCase):
    @patch('requests.get')
    def test_get_json(self, mock_requests_get):
        # Define the test data
        test_data = [
            {"test_url": "http://example.com",
                "test_payload": {"payload": True}},
            {"test_url": "http://holberton.io",
                "test_payload": {"payload": False}},
        ]

        for data in test_data:
            test_url = data["test_url"]
            test_payload = data["test_payload"]

            # Create a Mock object for requests.get
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_requests_get.return_value = mock_response

            # Call the get_json function
            result = get_json(test_url)

            # Assert that the requests.get method was called once
            mock_requests_get.assert_called_once_with(test_url)

            # Assert that the result of get_json is equal to the test_payload
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
