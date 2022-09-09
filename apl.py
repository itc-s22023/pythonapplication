import requests
import json
import webbrowser
#API_ENDpoint =  https://api.nasa.gov/planetary/apod

def call_api():
    base = 'https://api.nasa.gov/planetary/apod/'
    key = '?api_key=KktmCgrPKfbbteMDeRSxH3mGSKMicQHC5cSXko7q'
    key = '?api_key=NpR0jgznUtMyCuQxk5ZuB6ZvDEtDym5I112fyAIU'
    date = '&date='
    inp = input('日付入力してください: ')

    url = f'{base}{key}{date}{inp}'
    res = requests.get(url)
    print(res)
    json_data = json.loads(res.content)
    print(json_data)
    image = json_data['url']
    d = webbrowser.open(image)
    return d
    o = f'fdjkfjkf'
def mozi_api():
    print("fjkdjkds")
#    print(url)

def aaa_api():
    setm = '&explanation='
    return  setm
    url = f'{base}{key}{date}{inp}'
    res = requests.get(url)
    print(res)
    json_data = json.loads(res.content)
    print(json_data)
    image = josn_data['url']
    d = webbrowser.open(image)
    return d
    data = '&data='
    inp = input()
call_api()
aaa_api()


