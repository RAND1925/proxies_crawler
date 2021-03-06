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

class FreeProxyCzCrawler(ProxyCraweler):
    first_url = 'http://free-proxy.cz/en/proxylist/country/all/http/ping/all'

    def __init__(self):
        first_url = 'http://free-proxy.cz/en/proxylist/country/all/http/ping/all'
        super(FreeProxyCzCrawler, self).__init__(first_url, False)


    @staticmethod
    def parse_table(driver) :
        return driver.find_element(By.ID,
                                         'proxy_list')

    def parse(self):
        table = self.parse_table(self.driver)

        tbody = self.parse_tbody(table)
        trows = self.parse_trows(tbody)
        for trow in trows:
            tcells = self.parse_tcells(trow)
            # ads
            if len(tcells) < 3:
                continue
            ip = tcells[0].text
            port = tcells[1].text
            protocol = tcells[2].text
            proxy = Proxy(ip, port, Proxy.Protocol(protocol.lower()))
            print(str(proxy))
            self.got_proxies.append(proxy)


    def next(self):
        next_button = self.driver.find_element(By.CSS_SELECTOR, 'body > div.main > div.body_w > div.paginator > :last-child')
        assert 'Next' in next_button.text
        next_button =  ec.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.main > div.body_w > div.paginator > :last-child'))
        if next_button.tag_name == 'a':
            next_button.click()
            return True
        else:
            return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_url = 'https://free-proxy-list.com/'
    crawler = FreeProxyCzCrawler()
    crawler.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
