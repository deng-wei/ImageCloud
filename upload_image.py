import json
import base64
import requests
from urllib.parse import unquote

proxies = { "http": "http://127.0.0.1:7890/", "https": "http://127.0.0.1:7890/", } 

def get_github_url(image_path):
    url = 'https://api.github.com/repos/deng-wei/ImageCloud/contents/'
    headers = {'Authorization': 'token ***',
                'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "message": "",
        "committer": {
            "name": "***",
            "email": "***"
        },
        "author": {
            "name": "***",
            "email": "***"
        },
        "content": ""
    }

    image_name = image_path.split('/')[-1]
    with open(image_path, "rb") as f:
        file = f.read()
        encode_f = base64.b64encode(file)
    data['content'] = str(encode_f, encoding="utf-8")
    data['message'] = image_name
    
    # print(url + image_name)
    req = requests.put(url=url + image_name, data=json.dumps(data), headers=headers, proxies=proxies)
    # print(req.json())
    # print(req.status_code) # 201
    return unquote(req.json()['content']['download_url'], 'utf-8')
