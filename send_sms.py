import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"<< AUTH TOKEN >>","sender_id":"FSTSMS","message":"This is test message","language":"english","route":"p","numbers":"<< Destination number >>"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
