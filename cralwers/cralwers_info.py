"""company"""
import csv
import datetime
import time
from pathlib import Path
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def init_browser(
        target_url: str = 'https://www.11467.com/shenzhen/dir/i67.htm',
        headless: bool = True
):
    """
    init browser

    初始化浏览器对象，通过参数控制浏览器的有头无头模式

    :param headless:
    :param target_url:
    :return:
    """
    if headless:
        _chrome_options = Options()
        _chrome_options.add_argument('--headless')
        _browser = webdriver.Chrome(chrome_options=_chrome_options)
    else:
        _browser = webdriver.Chrome()
    time.sleep(3)
    _browser.get(target_url)
    return _browser


def parse_page(_browser) -> List[dict]:
    """
    parse page

    通过上述方法中获取的页面，进行页面解析
    :param _browser:
    :return:
    """
    info_list = []
    company_info_list = _browser.find_elements(By.CLASS_NAME, 'f_l')  # get 所有 class name 为f_l的元素
    num = 1
    for i in company_info_list:
        _company_info = {
            'title': i.find_element(By.TAG_NAME, 'h4').text,
            'product': i.find_elements(By.TAG_NAME, 'div')[0].text,
            'address': i.find_elements(By.TAG_NAME, 'div')[1].text,
            'funds': '',
            'create_date': '',
            'link': ''
        }
        extra_infos = i.find_elements(By.TAG_NAME, 'span')
        if extra_infos:
            if len(extra_infos) > 1:
                _company_info.update({'funds': extra_infos[0].text})
                _company_info.update({'create_date': extra_infos[1].text})
            if len(extra_infos) < 2:
                if '成立时间' in extra_infos[0].text:
                    _company_info.update({'create_date': extra_infos[0].text})
                if '注册资本' in extra_infos[0].text:
                    _company_info.update({'funds': extra_infos[0].text})
        try:
            _company_info.update(
                {'link': i.find_element(By.CLASS_NAME, 'shop').get_attribute('href')})
            # get_attribute获取标签属性值
        except Exception:
            info_list.append(_company_info)
        num += 1
    print(info_list)
    _browser.quite()
    return info_list


def write_to_file(info: List[dict], file_name: str):
    """
    write to file
    """
    keys = info[0].keys()
    with open(
            Path(f'{file_name}-{datetime.datetime.now().date()}.csv'),
            'w', newline='', encoding='utf-8'
    ) as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(info)
