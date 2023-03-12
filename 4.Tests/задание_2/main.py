import requests


def path_yadisk():
    token_ya = ""
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token_ya}'}
    params = {"path": "netology", "overwrite": "True"}
    folder_path = requests.put(upload_url, headers=headers, params=params)
    return folder_path




