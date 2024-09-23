import requests





url = 'http://127.0.0.1:8000/book_all/bdc5bace-525c-4d9e-8b7d-0e7c06765429'

data = {"name":'gogug in wa',
        "author":'awldiaw',
        # 'year_of_publish':1963
        }


data = requests.patch(url=url,data=data)
print(data.url)
print(data.status_code,data.text)