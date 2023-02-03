"""
author：linbo.wang
language: python

本示例演示解析抓取顺企网一个页面的企业信息列表
并将其导出到本地csv文件中
"""
from typing import List

from selenium.webdriver.common.by import By


def parse_page(_browser) -> List[dict]:
    """
    parse page

    通过上述方法中获取的页面，进行页面解析
    :param _browser:
    :return:
    """
    info_list = []
    company_info_list = _browser.find_elements(
        By.CLASS_NAME, 'f_l')  # get 所有 class name 为f_l的元素
    num: int = 1
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
        except Exception as e:
            print(e)
            info_list.append(_company_info)
        num += 1
    print(info_list)
    _browser.quite()
    return info_list
