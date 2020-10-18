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

class ProxyDbCrawler(ProxyCraweler):
    first_url = 'http://proxydb.net/?protocol=http&protocol=https&country_='

    @staticmethod
    def parse_table(driver) :
        return driver.find_element(By.CSS_SELECTOR,
                                         'body > div.container-fluid > div > table.table')

    def parse(self):
        table = self.parse_table(self.driver)

        tbody = self.parse_tbody(table)
        trows = self.parse_trows(tbody)
        for trow in trows:
            tcells = self.parse_tcells(trow)
            # ads
            if len(tcells) < 3:
                continue
            ip,port = tcells[0].text.split(':')
            protocol = tcells[4].text.strip()
            proxy = Proxy(ip, port, Proxy.Protocol(protocol.lower()))
            print(str(proxy))
            self.got_proxies.append(proxy)


    def next(self):
        next_button = self.driver.find_element(By.CSS_SELECTOR, '#paging-form > nav > ul > button')

        # may get a captcha
        if next_button and next_button.cl:

            assert 'Next' in next_button.text
            next_button.click()
            return True

        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_url = 'https://free-proxy-list.com/'
    crawler = ProxyDbCrawler()
    crawler.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
