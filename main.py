from utils.configs_reader import DataReader
from utils.catapi_request import GotoApi

data_reader = DataReader()
print(data_reader.host, data_reader.auth_value)

go_cat_api = GotoApi()
resp = go_cat_api.get_votes()
print(resp.status_code, resp.url, resp.reason)
