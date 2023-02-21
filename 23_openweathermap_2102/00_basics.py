import requests as r
import json

query = input('Что ищем? ')
lang = input('Язык: ')

url = "https://api.github.com/search/repositories"
params = {'q': query,
          'language': lang}
resp = r.get(url, params=params)
# вместе с url мы отдаем функции get словарь с параметрами params
print(resp.url)
js = resp.json()
for repo in js['items']:
    print(repo['svn_url'], repo['name'])
