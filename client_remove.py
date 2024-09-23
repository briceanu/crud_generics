# import requests



 

# remove = requests.delete(url="http://127.0.0.1:8000/book/delete/40e51607-6db7-4d4e-8947-e5d24c9d21d4")
 


# print(remove.status_code,remove.text)




import requests

# Pass the 'book_id' as a query parameter
url = "http://127.0.0.1:8000/book/delete/"
# params = {
#     'book_id': 'a168bd00-9219-443d-ba7b-60dfeffa463d'
# }

remove = requests.delete(url)
print(remove.status_code, remove.text)

