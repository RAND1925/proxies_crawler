import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import aiohttp
import asyncio

class ProxyCraweler:

    def __init__(self, first_url):
        # Use a breakpoint in the code line below to debug your script.
        self.first_url = first_url

        self.options = Options()
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
        pass

    def init(self):
        pass

    def open_first_url(self):
        self.driver.get(self.first_url)

    def next(self):
        pass

    def parse(self):
        pass

