from selenium import webdriver
import time
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--username', default='admin')
    parser.add_argument('--passwd', default='admin123')
    parser.add_argument('--url', default='https://login.manchester.ac.uk/cas/login')
    parser.add_argument('--proxy', default=None)
    args = parser.parse_args()
    print(args)
    return args


def init_options(url, proxy=None, cookies=None):
    options = webdriver.ChromeOptions()
    if proxy is not None:
        # options.add_argument('--proxy-server=http://103.216.103.25:80')
        options.add_argument('--proxy-server=%s' % proxy)
    # options.add_argument("headless")
    # options.page_load_strategy = 'normal'
    options.page_load_strategy = 'eager'
    # browser = webdriver.Chrome(executable_path="../chromedriver", options=options)
    browser = webdriver.Chrome(executable_path="./chromedriver", options=options)
    browser.get(url)
    if cookies is not None:
        for cookie in cookies:
            browser.add_cookie(cookie)
    browser.implicitly_wait(10)
    browser.maximize_window()
    return browser


def manchester_url(url, username, passwd, proxy):
    browser = init_options(url, proxy=proxy)
    # time.sleep(10)
    user = browser.find_element_by_id('username')
    pw = browser.find_element_by_id('password')
    user.send_keys(username)
    time.sleep(1)
    pw.send_keys(passwd)
    time.sleep(1)
    warn = browser.find_element_by_id('warn')
    browser.execute_script("arguments[0].click();", warn)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="fm1"]/section[5]/input[4]').click()
    # btn_submit = browser.find_elements_by_xpath('//*[@id="fm1"]/section[5]/input[4]')
    # browser.execute_script("arguments[0].click();", btn_submit)
    time.sleep(60*60*12)
    browser.quit()
    # while True:
    #     pass


if __name__ == '__main__':
    args = get_args()
    # url = 'https://login.manchester.ac.uk/cas/login'
    # username = 'admin'
    # passwd = 'admin123'
    #
    # proxy = 'https://5.75.150.14:3128'
    # main(url, username, passwd)
    manchester_url(args.url, args.username, args.passwd, args.proxy)

