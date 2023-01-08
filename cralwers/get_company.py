"""get company"""
from cralwers.cralwers_info import init_browser, parse_page, write_to_file

if __name__ == '__main__':
    browser = init_browser(headless=False)
    company_info = parse_page(browser)
    write_to_file(company_info, 'company_info')
