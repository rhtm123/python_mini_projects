import requests

url = "https://www.fast2sms.com/dev/bulk"

message = "Hello,"

querystring = {"authorization":"MlmbC4RnJtXGS20VZ5YFzPTLKEougQj7vHwqI9r8AWiad6DpB1a3vfV1IYm7yodqbMKxBRuJpgnA2e4i",
"sender_id":"SMSINI","message":message,"language":"english","route":"p",
"numbers":"9518901902"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)