from requests import get, post, delete


# print(post('http://localhost:5000/api/news').json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/v2/news',
           json={'title': 'Новость API',
                 'content': 'API работает!',
                 'user_id': 1,
                 'is_private': False}).json())
news = get('http://localhost:5000/api/v2/news').json()
for nws in news['news']:
    print(nws)
    print('--------------------------')
