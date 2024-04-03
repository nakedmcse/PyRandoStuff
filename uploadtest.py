import requests
from requests_toolbelt import MultipartEncoder

# upload file
multipart_data = MultipartEncoder(
    fields={
        'file': ('lambda.py', open('lambda.py', 'rb'), 'text/plain')
    }
)
response = requests.put("http://localhost:8081/rest", data=multipart_data, headers={'Content-Type': multipart_data.content_type})
data = response.text
print(data)


# upload via URL
response = requests.put(
    "http://localhost:8081/rest",
    data={'url': 'https://victorique.moe/img/slider/Quotes.jpg'}
)
data = response.text
print(data)