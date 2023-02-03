"""download"""
import os
import time
from pathlib import Path

import requests
from selenium.webdriver.common.by import By

from cralwers.utils.browser import init_browser


def parse_link(_browser) -> str:
    """parse link"""
    link = _browser.find_elements(
        By.TAG_NAME, 'video')[0].find_elements(By.TAG_NAME, 'source')[0].get_attribute('src')
    _browser.quit()
    return link


def check_link(_link: str = input('分享链接：')):
    """check link"""
    _aim_url = 'http' + _link.split('http')[1].split('/ ')[0] + '/'
    return _aim_url


# 0.51 HIv:/ 复制打开抖音，看看【幺零三的作品】Tab动效设计思路提示# ui # 动效 # Ae... https://v.douyin.com/hkwyAD6/
aim_url = check_link()
print(aim_url)

browser = init_browser(aim_url, False)
video_link = parse_link(browser)
print(video_link)

if 'http' not in video_link:
    video_link = 'https:' + video_link

aim_response = requests.get(video_link, timeout=20)
download_path = Path('../download')
if not download_path.exists():
    print(f'存储目录不存在, make dirs ({download_path})')
    os.makedirs(download_path)
with open((download_path / f'{time.time() * 1000000}.mp4').resolve(), 'ab') as f:
    f.write(aim_response.content)
print('下载成功')
