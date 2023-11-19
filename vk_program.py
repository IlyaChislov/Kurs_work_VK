import requests
import json
import vk_class
import yandex_class
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

if __name__=='__main__':
    # owner_id=76879487
    # token_yandex='y0_AgAAAAAFmdz2AArRrwAAAADx_0S8TuTq6oibSaCtNNXm5Cx94MDHHBs'
    print("Введите id страницы пользователя вк, owner_id=")
    owner_id=input()
    print("Введите токен с полигона яндекс диска, token_yandex=")
    token_yandex = str(input())
    vk_page=vk_class.VK_API_PHOTOS(vk_class.token_vk, owner_id)
    class1=yandex_class.YANDEX_DISK_API(token_yandex, vk_page.get_photos())
    photos_list=class1.save_photos()
    with open('data_file,json', "w") as f:
        json.dump(photos_list, f)





# photos=first_page.get_photos()
# pprint.pprint(photos)
# list_file_names=[]
# for files in photos['response']['items']:
#     file_url=files['sizes'][-1]['url']
#     file_name=files['likes']['count']
#     if file_name in list_file_names:
#         file_name+=str(files['date'])
#     else:
#         list_file_names.append(file_name)
#     photo=requests.get(file_url)
#     print(file_url)
#     with open('C:/Users/User/Desktop/save_photos/'+str(file_name)+'jpeg', 'wb') as f:
#         f.write(photo.content)



# disk = YaDisk(token=token_yandex)
# if disk.check_token():
#     print("Авторизация прошла успешно")
# else:
#     print("Ошибка авторизации")







