#Sometimes, the server may examine the User-Agent of the requests, so we should do something to go through it. 
#How to camouflage as an explorer? -> Wrap the User-Agent into the dictionary.
import requests
if __name__ == "__main__":
    #Destination of resources
    website='https://cn.bing.com/search?'
    #UA-camouflage
    UAcamouflage = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    kw = input('enter a word:')
    #Define a dictionary to realize dynamic searching
    param = {
        'q': kw
    }
    #Requests sent by the websites carry with parameters(url, params) and deal with them during this process
    response = requests.get(url = website, params = param, headers = UAcamouflage)
    #Save the page into a file as a text
    page_text = response.text
    filename = kw + '.html'
    with open(filename, 'w', encoding = 'utf-8') as fp:
        fp.write(page_text)
    print(filename, 'has saved successfully!!!')