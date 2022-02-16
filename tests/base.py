import json
import unittest
import random
import string
# from collections import counter
from utils.catapi_request import GotoApi


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.catapi = GotoApi()
        cls.json_object = json.loads('{ "id": 499958, "user_id": "4", "image_id": "ol", "sub_id": "goodman_votes",'
                                     ' "created_at": "2022-02-11T11:43:00.000Z", "value": 1, "country_code": null }')
        cls.status = range(200, 300)
        cls.s_success = 'SUCCESS'
        cls.not_found = 'NOT_FOUND'

    def setUp(self):
        self.sub_post_sub_id = "goodman_votes_1"
        self.sub_id_rand = str(''.join(random.choice(string.ascii_letters) for _ in range(9)))
        self.posts_rand_id = self.catapi.post_votes(sub_id=self.sub_id_rand)
        self.posted_rand_id = self.catapi.post_votes(sub_id=self.sub_id_rand).json()['id']
