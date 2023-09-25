import requests as rq
import json


# url = 'https://reactjs.org'
# r = rq.get(url)
# print (r.status_code, 'Status code')
# print(r.json())
# r.encoding='utf-8'
# print(r.text)

r = rq.get('https://api.github.com')
# print (r.status_code, 'Status code')


def jpring(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# jpring(r.json())


def check_status():
    if (r.status_code == 200):
        print("Success")
    else:
        print("Error")


def check_status2():
    try:
        r.raise_for_status()
        print("Success")
    except r.exceptions.HTTPError as error:
        print("Error", error)


check_status()
check_status2()
