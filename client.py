import requests


# 
url = 'http://127.0.0.1:8000/book/'


data = {"name":'la tiganci',
        "author":'ioan bulaideleanu',
        'year_of_publish':1983
        }


# save = requests.post(url=url,data=data)
list_books = requests.get(url='http://127.0.0.1:8000/book/')

# print(save.status_code,save.text)
print(list_books.status_code,list_books.text)