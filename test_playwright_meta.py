import unittest
import playwright_meta

class TestPlaywrightMeta(unittest.TestCase):

    def test_get_cookie_playwright(self):
        # Pass variables to run test
        url='https://www.asos.com/asos-design/'
        cookie_location=3
        accept_cookies_name="That's ok"
        # Get cookie_key and cookie_value so you can run asserts on them
        cookie_key, cookie_value = playwright_meta.get_cookie_playwright()
        # Tests
        self.assertIsNotNone(cookie_key)
        self.assertIsNotNone(cookie_value)
        self.assertNotEqual(cookie_key, '')
        self.assertNotEqual(cookie_value, '')

if __name__ == '__main__':
    unittest.main()
