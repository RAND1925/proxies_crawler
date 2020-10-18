import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import aiohttp
import asyncio
from item import Proxy

class ProxyCraweler:

    first_url = ''
    def __init__(self, first_url: str = '', headless: bool = True):
        # Use a breakpoint in the code line below to debug your script.
        self.got_proxies = list()
        self.usable_proxies = list()
        self.options = Options()
        if headless:
            self.options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.implicitly_wait(10)

    def run(self):
        self.open_first_url()
        self.init()
        self.parse()
        while self.next():
            self.parse()
        else:
            self.close()

    def close(self):
        print(self.got_proxies)

        with open('list.txt', 'w') as file:
            for proxy in self.got_proxies:
                print(str(proxy))
                file.write(str(proxy)+'\n')

    def init(self):
        pass

    def open_first_url(self):
        self.driver.get(self.first_url)

    def next(self):
        pass

    @staticmethod
    def parse_table(driver) :
        return driver.find_element(By.TAG_NAME, 'table')

    @staticmethod
    def parse_tbody(table):
        return table.find_element(By.TAG_NAME, 'tbody')

    @staticmethod
    def parse_trows(tbody):
        return tbody.find_elements(By.TAG_NAME, 'tr')

    @staticmethod
    def parse_tcells(trow):
        return trow.find_elements(By.TAG_NAME, 'td')

    @staticmethod
    def parse_tcell(tcell):
        return Proxy()

    def parse(self):
        table = self.parse_table(self.driver)
        tbody = self.parse_tbody(table)
        trows = self.parse_trows(tbody)
        tcells = self.parse_tcells(trows)
        for tcell in tcells:
            self.parse_tcell()

