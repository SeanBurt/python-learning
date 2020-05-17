#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.ip138.com/tel.htm'
# url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

try:
    resp = requests.get(url, headers=headers)
    resp.encoding='utf-8'
    # print(resp.text)
    soup=BeautifulSoup(resp.text,'lxml')
    data = soup.select('body > div.wrapper > div.container > div.content > div.mod-panel > div.bd > div > table > tr:not(:first-child)')
    # print(data)
    contact = {}
    for item in data:
        txt = item.get_text("|", strip=True)
        ary = txt.split('|')
        for index in range(len(ary)):
            if index % 2 == 0:
                contact[ary[index]] = ''
            else:
                contact[ary[index - 1]] = ary[index]
    with open('data.json', 'w') as json_file:
        json.dump(contact, json_file, ensure_ascii=False)
except BaseException as ex:
    print(ex.args)
