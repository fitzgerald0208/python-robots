from ast import keyword
import json
from wsgiref import headers
import requests
if __name__ == '__main__':
    #assign the object URL
    post_url = 'https://fanyi.baidu.com/sug'
    #UAcamouflage
    UAcamouflage = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    #process of "POST request's parameter"
    #use dictionary(same to GET request).
    keywd = input('Please type in your word needed to translated: ')
    data_param = {
        'kw' : keywd
    }
    #send the requests
    response = requests.post(url = post_url, data = data_param, headers = UAcamouflage)
    #get the response as JSON because we can make sure that the response date is type of JSON from "Content-Type"
    dic_obj = response.json()
    #save the data into file
    fp = open(keywd +'.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print('That is all!')
