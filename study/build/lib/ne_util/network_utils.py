# -*- coding:utf-8 -*-
import urllib.parse
import urllib.request
import json


def post(url, values):
    # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

    headers = {
        'Content-Type': 'application/json',
        "Accept": "application/json"
    }
    data = json.dumps(values).encode('utf-8')

    req = urllib.request.Request(url, headers=headers, data=data)

    response = urllib.request.urlopen(req)

    html = response.read()
    html = html.decode('utf-8')
    body = json.loads(html)
    return body

if __name__ == '__main__':
    print()