import requests as r

endpoint = 'https://www.w3schools.com/python/demopage.php'
API_KEY = 'xxxxxxxx'

data = {
    'api_dev_key': API_KEY,
    'api_option': 'paste',
    'api_paste_format': 'python',
}

resp = r.post(url=endpoint, json=data)
print(resp.text)
print(resp.url)

