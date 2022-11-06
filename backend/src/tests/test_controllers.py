import unittest
import sys
sys.path.append("..")
from view.tournament_use_cases import create_tournament, find_tournament_by_id
from werkzeug.test import Client
from werkzeug.testapp import test_app




class Test_controllers(unittest.TestCase):

    c = Client(test_app)

    def test_new_tournament(self):
        response = self.c.post("/tournament/new")
        self.assertEqual(200,response.status_code)

    def test_search_tournament(self):
        response = self.c.get("/tournament/1")
        self.assertEqual(200,response.status_code)

if __name__ == '__main__':
    unittest.main()