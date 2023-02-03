"""
cralwers medical data

author：linbo.wang
language: python
description: cralwers medical data

使用静态请求接口的方式获取页面数据
url: https://bn59.s2ps.cn/webroot/decision/
"""

import requests
from bs4 import BeautifulSoup

from cralwers.config import settings

url = settings.CRALWERS_MEDICAL_URL

headers = settings.CRALWERS_MEDICAL_HEADERS
r = requests.get(url, headers=dict(headers),timeout=settings.CRALWERS_MEDICAL_TIMEOUT)
soup = BeautifulSoup(r.text, 'lxml')
tr_list = soup.find_all('tr')[2:]
res = []
for tr in tr_list:
    info_list = []
    for td in tr.find_all('td')[1:]:
        info_list.append(td.text.strip())
    res.append(info_list)
print(res)
