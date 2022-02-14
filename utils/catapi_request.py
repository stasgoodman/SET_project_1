import requests
from utils.configs_reader import DataReader


class GotoApi:

    def __init__(self):
        self.dread = DataReader()
        self.headers = {self.dread.auth_name: self.dread.auth_value}

    def get_votes(self):
        return requests.get(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes",
                            headers=self.headers)

    def post_votes(self, sub_id):
        return requests.post(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes",
                             headers=self.headers,
                             json={"image_id": "ol", "sub_id": sub_id, "value": 1})

    def get_votes_id(self, vote_id=None):
        return requests.get(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes/{vote_id}",
                            headers=self.headers)

    def get_sub_id(self, vote_id=None, sub_id=None):
        return requests.get(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes/{vote_id}",
                            headers=self.headers,
                            json={"sub_id": sub_id})

    def del_votes_id(self, vote_id):
        return requests.delete(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes/{vote_id}",
                               headers=self.headers)
