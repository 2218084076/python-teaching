"""cralwers proxy"""
import json
from typing import List

import requests

from cralwers.cralwers_info import write_to_file


# from lxml import etree

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
    res = get_link('https://proxylist.geonode.com/'
                   'api/proxy-list?limit=500&page=1&'
                   'sort_by=lastChecked&sort_type=desc')
    info = parse_html(res)
    write_to_file(info, 'proxy-ip')
