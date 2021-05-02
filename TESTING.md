# Testing The API

On the parent directory file `test_autocomplete.py` contain the following:

- Test Case class to house all API tests.
- setUp() methods to initialize our app and it's test client and create our test database within the app's context.
- tearDown() method to tear down test variables and delete our test database after testing is done.
- tests to test whether our API can get suggestions.

## Running the Tests
To run the tests run the following command `python test_autocomplete.py`