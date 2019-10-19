import json
import requests
#
# url = 'http://httpbin.org/get'
# headers = {'user-agent': 'my-app/0.0.01'}
# url2 = 'http://ivan.org'
# r1 = requests.get(url, headers = headers, params = url2)
# print(r1.text)



url = 'http://pulse-rest-testing.herokuapp.com/books'
r = requests.get('http://pulse-rest-testing.herokuapp.com/books')
x = json.loads(r.text)
print(x)
book = {'title': 'Война и мир', 'author': 'Лев'}
requests.post(url, book)
f = requests.get(url)
f1 = json.loads(f.text)
print(f1)
for i in f1:
    if i['author'] =='Лев':
        z = i['id']
        z = str(url + '/' + str(z))
        requests.delete(z)


# f = requests.delete(url+z)
# print(f.status_code)



