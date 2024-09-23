import requests



url = "http://127.0.0.1:8000/book/update/2fb8d07a-d0a4-4e6b-8bad-839fa5c51c3f"


data = {
        'name':'la fuftifn ',
        'year_of_publish':1979,
        'author':'ion creanga'
        }

#  inside the body of the dictionary is the updated data

# save = requests.put(url=url,data=data)
patch = requests.put(url=url,data=data)

 
# print(save.status_code,save.text)
print(patch.status_code,patch.text)