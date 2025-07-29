from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()


class BaseCrawler(ABC):
    def __init__(self):
        self.driver = None
        self.setup_driver()

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_soup(self, url, wait_time=3):
        self.driver.get(url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait_time)
        html = self.driver.page_source
        return BeautifulSoup(html, 'html.parser')
    
    def get_category_urls(self, category_name):
        choices = {
            'news':'FINANCE_NEWS_URL',
            'fashion': 'FASHION_URL',
            'beauty':'BEAUTY_URL'
        }
        env_name = choices[category_name]
        
        print(category_name)

        return os.getenv(env_name)

    @abstractmethod
    def crawl(self):
        """각 크롤러에서 구현"""
        pass

    def save_data(self, data, filename):
        with open(f'data/{self.catagory}/{filename}', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def close(self):
        if self.driver:
            self.driver.quit()
        
