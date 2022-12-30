"""cralwer campus information"""
# -*- coding: UTF-8 -*-
import re
import time
from datetime import datetime
from typing import List
from urllib import parse

import matplotlib.pyplot as plt
import pymysql.cursors
import requests
from bs4 import BeautifulSoup
from lxml.etree import Element  # pylint: disable=no-name-in-module
from requests.models import Response

start_urls = [
    'https://jxjy.imu.edu.cn/tzgg.htm',
    'https://jxjy.imu.edu.cn/tzgg/1.htm',
    'https://jxjy.imu.edu.cn/tzgg/2.htm',
    'https://jxjy.imu.edu.cn/tzgg/3.htm'
]
TABLE_NAME = 'test'

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123qweasd',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)


def create_table():
    """create_table"""
    con = connection.cursor()
    con.execute('use qmks')
    con.execute(
        f'''
create table if not exists {TABLE_NAME}(
id int unsigned auto_increment,
tag varchar(200) not null,
title varchar(200) not null,
release_time date,
hits varchar(200),
news_url varchar(255),
content mediumtext,
primary key (id)
)engine=InnoDB default charset=utf8mb3;
        '''
    )


def insert_data(_data: List[dict]):
    """Insert data"""
    cur_insert = connection.cursor()
    for d in _data:
        sql_insert = f"""
        insert into {TABLE_NAME}(
        tag,title,release_time,hits,news_url,content
        ) values (
        "{d.get("tag")}",
        "{d.get("title")}",
        "{d.get("release_time")}",
        "{d.get("hits")}",
        "{d.get("news_url")}",
        "{d.get("content")}")"""
        try:
            cur_insert.execute(sql_insert)
            connection.commit()
        except Exception as e:
            print(e)
            connection.rollback()


def query() -> List[dict]:
    """query"""
    res = []
    cur = connection.cursor()
    sql = f"select * from {TABLE_NAME}"
    try:
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            res.append(row)
        return res
    except Exception as e:
        raise e


def statistics(_data: List[dict]):
    """statistics"""
    date_list = []
    count = {}
    for d in _data:
        date_list.append(str(d.get('release_time')))
    for k in date_list:
        count[k] = count.get(k, 0) + 1
    plt.barh(list(count.keys()), list(count.values()))
    plt.show()


def format_str(content: str) -> str:
    """format string"""
    formatting = parse.unquote(content.encode('unicode_escape').decode('utf-8').replace('\\x', '%'))
    return formatting


def get_news(url: str) -> Response | None:
    """get news list"""
    for i in range(5):
        try:
            _response = requests.get(url, verify=False, timeout=30)
            return _response
        except Exception as e:
            print(e)
            time.sleep(3 * (i + 1))
        return None


def parse_news_list(url: str) -> List[dict]:
    """parse_news_list"""
    res = get_news(url)
    infos_list = []
    soup = BeautifulSoup(res.text, 'lxml')
    li_list: List[Element] = soup.find_all('li')
    tag_text = soup.find('div', {'id': 'right_title'}).text
    for li in li_list:
        a_tag = li.find('a', href=True)
        span_tag = li.find('span')
        news_link = 'https://jxjy.imu.edu.cn/' + a_tag['href']
        content = parse_news_content(news_link)
        kv = {
            'tag': re.findall(r'[\u4e00-\u9fa5]+', format_str(tag_text))[0],  # 使用正则匹配中文
            'title': format_str(a_tag.text),
            'release_time': datetime.strptime(
                re.search(
                    r"(\d{4}-\d{1,2}-\d{1,2})",
                    format_str(span_tag.text)).groups()[0],
                '%Y-%m-%d'
            ),
            'hits': li.find_all('span')[-1].text,
            'news_url': news_link,
            'content': content,
        }
        infos_list.append(kv)
    return infos_list


def parse_news_content(news_url: str) -> str:
    """parse_news_content"""
    res = get_news(news_url)
    soup = BeautifulSoup(res.text, 'lxml')
    content = soup.find('div', {'id': 'home_more_right'})
    content_text = ','.join(re.findall(r'[\u4e00-\u9fa5]+', format_str(content.text)))
    if content_text:
        return content_text
    return ''


if __name__ == '__main__':
    for u in start_urls:
        info = parse_news_list(u)
        create_table()
        insert_data(info)
    time.sleep(2)
    data = query()
    statistics(data)
    connection.close()
