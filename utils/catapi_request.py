import requests
from utils.configs_reader import DataReader


class GotoApi:

    def __init__(self):
        self.dread = DataReader()
        self.headers = {self.dread.auth_name: self.dread.auth_value}

    def get_votes(self):
        return requests.get(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes",
                            headers=self.headers)

    def post_votes(self):
        return requests.post(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes",
                             headers=self.headers,
                             data={'key': 'value'})

    def get_votes_id(self):
        return requests.post(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes/{vote_id}",
                             headers=self.headers)

    def del_votes(self):
        return requests.post(url=f"{self.dread.protocol}://{self.dread.host}/{self.dread.version}/votes/{vote_id}",
                             headers=self.headers)