"""get company"""
from cralwers.practice.cralwers_info import parse_page
from cralwers.utils.browser import init_browser
from cralwers.utils.files import write_to_file

if __name__ == '__main__':
    browser = init_browser(headless=False)
    company_info = parse_page(browser)
    write_to_file(company_info, 'company_info')
