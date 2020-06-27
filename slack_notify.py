import requests

def slack_post(text):
    headers = {"Content-Type": "application/json"}
    
    params = {
    "token": "xoxb-1181947537393-1224678523232-mpt8NLqgyLwdV9zZLNzl1Gu6",
    "channel": "campfire",
    "text": text
    }

    requests.post("https://slack.com/api/chat.postMessage",headers=headers, params=params)

# print("return ", r.json())
