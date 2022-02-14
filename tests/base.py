import unittest
# from collections import counter
import json
from utils.catapi_request import GotoApi


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.catapi = GotoApi()
        cls.json_object = json.loads('{ "id": 499958, "user_id": "4", "image_id": "ol", "sub_id": "goodman_votes",'
                                     ' "created_at": "2022-02-11T11:43:00.000Z", "value": 1, "country_code": null }')
        cls.status = range(200, 300)
