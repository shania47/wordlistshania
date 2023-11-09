import requests

api_key = 'fe77ad91-7628-4196-91d9-cfdadea5f725'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'


res = requests.get(url)

definitions = res.json()

for definiton in definitions:
    print(definiton)