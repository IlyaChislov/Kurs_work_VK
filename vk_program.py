import requests
from urllib.parse import urlencode
import pprint
from yadisk import YaDisk
# app_id = '51792587'
# base_url = 'https://oauth.vk.com/authorize'
# params={
#     'client_id': app_id,
#     'redirect_uri': 'https://oauth.vk.com/blank.html',
#     'display': 'page',
#     'scope': 'photos,offline',
#     'response_type': 'token'
# }
# response=requests.get(base_url, params=params)
# print(response.url)
# app_id='4d319bb29e474d4b894df2b993c6f3cf'
# base_url='https://oauth.yandex.ru/authorize'
# params_yandex={
#     'response_type': 'token',
#     'client_id': app_id
# }
# response=requests.get(base_url, params=params_yandex)
# print(response.url)
token_vk='vk1.a.77EDsiAquiSMVsIdCdTqIoEFqx3-J9euk160rX_yolfCOaG_bojE3oG7r-4nIwsEYJNqWRkqLNFlymD0oHoiyxXi3oNnf1ks7eQUI5GDJBmXVCHmQTh9r0f5ZyBzKmshaNavn1L2B8eOuqJwuwELoV2I87dPrkcV1OnIooEwmIBdNnBFnMuCbyErfSHOfzglxzZrlY9UoJcNbMzdZiRaVg'
token_yandex='y0_AgAAAAAFmdz2AArRrwAAAADx_0S8TuTq6oibSaCtNNXm5Cx94MDHHBs'

class VK_API_PHOTOS:
    API_BASE_URL = 'https://api.vk.com/method/photos.get'

    def __init__(self, token_vk, owner_id):
        self.token_vk=token_k
        self.owner_id=owner_id

    def get_params(self):
        params={
            'access_token': token_vk,
            'v': '5.154',
            'extended': 1
        }
        return params

    def get_photos(self):
        params=self.get_params()
        params.update({'owner_id': self.owner_id, 'album_id': 'profile'})
        response=requests.get(self.API_BASE_URL, params=params)
        return response.json()


# first_page=VK_API_PHOTOS(token_vk, 76879487)
# photos=first_page.get_photos()
# pprint.pprint(photos)
disk = YaDisk(token=token_yandex)
if disk.check_token():
    print("Авторизация прошла успешно")
else:
    print("Ошибка авторизации")







