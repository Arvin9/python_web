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
    url = 'http://10.1.8.9:8280/dc/v1/usercenter/userinfo/gestureCodeOperate'
    values = {
        "content": "NICUDJVSFFUqag11FThINnMta8RFPicashIlN+p9xOY8y0fJPNtEsOh9BKNO0msjXM8iU9vHLhHyLkZNLxodi+LZhsx6h6gbqXWt5ZUvGiNlxFKxmBkm2vB3Vw48rAJSSw7R6EDZlM7djEdG2QGpOI+bjPaYx5NyFI2Calts1TI=",
        "header": {"appId": "1002", "appVersion": "1.0", "deviceId": "862033030711343",
                   "requestSeq": "5b0cf572-3af2-4ad9-a0f2-e8842196b531", "requestTime": "20171025155112",
                   "userId": "100360489403505971200", "userToken": "2d6de3941ae54da1b246096e91f7e67a"}}
    body = post(url, values)
    print("return：" + body)