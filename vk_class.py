import requests
import json
from urllib.parse import urlencode
import pprint

token_vk='vk1.a.77EDsiAquiSMVsIdCdTqIoEFqx3-J9euk160rX_yolfCOaG_bojE3oG7r-4nIwsEYJNqWRkqLNFlymD0oHoiyxXi3oNnf1ks7eQUI5GDJBmXVCHmQTh9r0f5ZyBzKmshaNavn1L2B8eOuqJwuwELoV2I87dPrkcV1OnIooEwmIBdNnBFnMuCbyErfSHOfzglxzZrlY9UoJcNbMzdZiRaVg'
class VK_API_PHOTOS:
    API_BASE_URL = 'https://api.vk.com/method/photos.get'

    def __init__(self, token_vk, owner_id):
        self.token_vk=token_vk
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
        response=requests.get(self.API_BASE_URL, params=params).json()
        list_file_names=[]
        photos_list=[]
        for files in response['response']['items']:
            file_url=files['sizes'][-1]['url']
            file_name=str(files['likes']['count'])+'.jpg'
            for photo in photos_list:
                if file_name in photo.keys():
                    file_name=str(files['likes']['count'])+str(files['date'])+'.jpg'
            size=files['sizes'][-1]['type']
            photos_list.append({file_name: [file_url, size]})
        return photos_list