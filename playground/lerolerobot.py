import requests

url = "https://api.twitter.com/1.1/statuses/update.json"

consumer_key = "-"
access_token = "-"

headers = {
    'authorization': 'OAuth oauth_consumer_key={consumer_key}, oauth_nonce="OAUTH_NONCE", oauth_signature="OAUTH_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="OAUTH_TIMESTAMP", oauth_token={access_token}, oauth_version="1.0"'
}

params = {
    'status': 'tweet via curl teste'
}

response = requests.post(url, headers=headers, params=params)
print(response.json())