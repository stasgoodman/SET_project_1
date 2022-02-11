import unittest
from utils.catapi_request import GotoApi


class TestCatApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.catapi = GotoApi()

    def test_step_1_status_200(self):
        """
        1. status = 200
        """
        self.assertEqual(200, self.catapi.get_votes().status_code, "FU")

    def test_step_3(self):
        pass

    def test_step_2_len_not_0(self):
        """
        1. content is not 0
        """
        self.assertGreater(len(self.catapi.get_votes().content), 0, "FU2")
