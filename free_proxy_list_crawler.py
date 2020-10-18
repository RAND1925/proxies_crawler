import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import aiohttp
import asyncio

from proxy_crawler import ProxyCraweler
from item import Proxy

class FreeProxyListCrawler(ProxyCraweler):

    first_url = 'https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search'

    def init(self):
        super(FreeProxyListCrawler, self).init()
        self.got_proxies = list()
        self.usable_proxies = list()

        '''
        type_inputs = self.driver.find_elements(By.NAME, 'type[]')
        for type_input in type_inputs:

            if type_input.get_attribute('value').strip() in ('http', 'https'):
                type_input.click()

        search_btn = self.driver.find_element(By.NAME, 'search')
        search_btn.click()
        '''

    def parse(self):
        table = self.driver.find_element(By.CSS_SELECTOR, 'body > div.wrapper > div.container > div > div > div.table-responsive > table')
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        trows = tbody.find_elements(By.TAG_NAME, 'tr')
        for trow in trows:
            tcells = trow.find_elements(By.TAG_NAME, 'td')
            ip = tcells[0].text
            port = tcells[2].text
            protocol = tcells[-3].text
            proxy = Proxy(ip, port, Proxy.Protocol(protocol))
            self.got_proxies.append(proxy)

    def close(self):
        print(self.got_proxies)

        with open('list.txt', 'w') as file:
            for proxy in self.got_proxies:
                print(str(proxy))
                file.write(str(proxy)+'\n')

    def next(self):
        pager_ul = self.driver.find_element(By.CSS_SELECTOR, 'body > div.wrapper > div.container > div > div > div.content-list-pager-wrapper > ul')
        if pager_ul:
            next_pager_li = pager_ul.find_element(By.CSS_SELECTOR, 'li.pager-item:nth-last-child(2)')
            if 'disabled' not in next_pager_li.get_attribute('class').split(' '):
                next_pager_li.find_element(By.TAG_NAME, 'a').click()
                return True
        return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_url = 'https://free-proxy-list.com/'
    crawler = FreeProxyListCrawler(first_url)
    crawler.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
