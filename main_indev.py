import json

from utils.configs_reader import DataReader
# from utils.configs_reader import ResponseDataReader
from utils.catapi_request import GotoApi


data_reader = DataReader()
# resp_data_reader = ResponseDataReader()
print(data_reader.host, data_reader.auth_value)
# print(resp_data_reader.ids)


go_cat_api = GotoApi()

resp = go_cat_api.get_votes()
list_js = resp.json()
dict_js = list_js[0]
resp_status_code = resp.status_code
body_resp = resp.headers

vote_id = list_js[0]['id']
resp_id = go_cat_api.get_votes_id(vote_id)
resp_content = resp_id.content
ids_resp = resp_id.json()


print(resp.url, resp.status_code, resp.reason, resp.headers['Pagination-Count'], resp.headers['Pagination-Limit'],
      resp.headers['Pagination-Page'], '\n')

# print(resp_content)
# print(resp.json())
# print(dict_js['id'])


def step_1_length_is_not_0():
    ids = []
    for p_id in list_js:
        ids.append((p_id['id']))
    ids_len = len(ids)
    if resp_status_code == 200 and ids_len > 0:
        print('Step_1 is Passed > 200, Length of response result is:', ids_len)
    else:
        print('Step_1 is Failed > 200, Length of response result is:', ids_len)
    pass


def step_2_by_vote_id():                                                               #TODO
    l1 = 200
    l2 = []
    l3 = ids_resp['id']
    json_string = '{ "id": 31098, "user_id": "4", "image_id": "43u", "sub_id": null,' \
                  ' "created_at": "2018-10-24T08:36:13.000Z", "value": 1, "country_code": null }'
    json_object = json.loads(json_string)
    if resp_status_code == l1 and resp_content != l2 and ids_resp == json_object and vote_id == l3:
        print("Step_2 is Passed > 200, Json content is not empty, request id = response id")
    else:
        print("Step_2 is Failed")


def post_vote():
    if resp_status_code != 200:
        print("Step_3 is Passed")
    else:
        print("Step_3 is Failed")


def show_info():
    ids = []
    for p_id in list_js:
        ids.append((p_id['id'], p_id['image_id'], p_id['sub_id'],
                    p_id['created_at'], p_id['value'], p_id['country_code']))
    print(ids)
    list1 = list((p_id.get('id') for p_id in list_js if p_id.get('sub_id') is None))
    print(list1)


def filter_all_by_sub_id_is_not_none():                      # filtering with the 'sub_id'
    ids = []
    for all_items in list_js:
        if all_items['sub_id'] is not None:
            ids.append((all_items['id'], all_items['sub_id']))
    print("Filtered by 'sub_id'>>", ids)


def try_f():
    json_response = resp.json()
    votez = json_response[99]
    print(f'ID >: {votez["id"]}')
    print(f'Image_id >: {votez["image_id"]}')
    print(f'Created_at > : {votez["created_at"]}')


step_1_length_is_not_0()
step_2_by_vote_id()
post_vote()
# show_info()
# filter_all_by_sub_id_is_not_none()
# try_f()


#
# print(resp.url, resp.status_code, resp.reason, resp.content)           # Just INFO
# print('>>>>>>INFO START>>>\n>>>>>>')
# print(list_js)
# print(type(list_js))
#
# print(dict_js)
# print(type(dict_js))
#
# print(cat_ids)
# print(type(cat_ids))
# print('>>>>>>\n>>>>>>INFO END>>>')
