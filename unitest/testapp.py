import unittest
from app import app
import json


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client =app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        resp = self.client.post("/")
        print("+++")
        resp_str = resp.data.decode("utf-8")
        resp_json = eval(resp_str)
        print(resp_json)
        resp_dict = []
        for item in resp.data:
            pass

        print(resp_dict)
        #self.assertIn("code", resp_dict)


if __name__ == '__main__':
    unittest.main()