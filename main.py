import json

from utils.configs_reader import DataReader
from utils.catapi_request import GotoApi

data_reader = DataReader()
print(data_reader.host, data_reader.auth_value)

go_cat_api = GotoApi()
resp = go_cat_api.get_votes()
list_js = resp.json()
dict_js = list_js[0]
cat_ids = list_js[0]['id']

print(resp.url, resp.status_code, resp.reason)


def filter_all_by_sub_id_is_none():                                                          # filtering with the 'sub_id'
    for all_items in list_js:
        if all_items['sub_id'] is None:
            print(all_items['id'])
    print("Filtered by 'sub_id'\n >>>\n")


# Pagination
#
#
print('>>>>>>INFO START>>>\n>>>>>>')
print(list_js)
print(type(list_js))

print(dict_js)
print(type(dict_js))

print(cat_ids)
print(type(cat_ids))
print('>>>>>>\n>>>>>>INFO END>>>')

filter_all_by_sub_id_is_none()
