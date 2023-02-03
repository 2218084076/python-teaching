"""
cralwers proxy

author：linbo.wang
language: python
本实例使用requests库，静态请求代理网站，抓取页面中代理列表
"""
import json
from typing import List

import requests

from cralwers.config import settings
from cralwers.utils.files import write_to_file


def get_link(url: str):
    """get"""
    response = requests.get(url, timeout=20)
    return response


def parse_html(response) -> List[dict]:
    """parse"""
    info_list = []
    page_info = json.loads(response.text)  # "json.loads" is str to dict
    for i in page_info.get('data'):
        kv = {
            'ip': i.get('ip'),
            'port': i.get('port'),
            'city': i.get('city')
        }
        info_list.append(kv)
    print(info_list)
    return info_list


if __name__ == '__main__':
    res = get_link(settings.PROXY_URL)
    info = parse_html(res)
    write_to_file(info, 'proxy-ip')
