# test_autocomplete.py
import unittest
import os
import json
from app import create_app, db


class AutocompleteTestCase(unittest.TestCase):
    """This class represents the Auto Suggest test case"""

    def setUp(self):
        """Define test variables and initialize app."""


    def test_api_can_get_all_suggestions(self):
        """Test API can get suggestions (GET request)."""


    def test_api_can_get_suggestions_by_species(self):
        """Test API can get suggestions by using it's species."""


    def test_api_can_get_suggestions_by_label(self):
        """Test API can get suggestions by using it's display label."""

    def test_api_can_get_suggestions_by_limit(self):
        """Test API can get suggestions by using limit."""

    def tearDown(self):
        """teardown all initialized variables."""


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()