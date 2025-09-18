import requests
import base64
headers = {'User-Agent': 'Mozilla/5.0'}
img = open('./examples/animal-2.jpg', 'rb').read()
img = base64.b64encode(img).decode('utf-8')
# print(img)
payload = {'img': img}

session = requests.Session()
res = session.post('http://127.0.0.1:5000/process',headers=headers,json=payload)

file = open('output.jpg', 'wb+')
file.write(base64.b64decode(res.text))