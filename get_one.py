import requests


# 
# url = 'http://127.0.0.1:8000/get_book/bdc5bace-525c-4d9e-8b7d-0e7c06765429'
url = 'http://127.0.0.1:8000/get_book'

params = {"book_idd":"bdc5bace-525c-4d9e-8b7d-0e7c06765429"}

list_books = requests.get(url=url,params=params)
 
# print(save.status_code,save.text)
print(list_books.url)
print(list_books.status_code,list_books.text)