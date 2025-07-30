from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from util import current_time
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
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # User-Agent 추가
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # 자동화 탐지 방지
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


    def get_soup(self, url, wait_time=3):
        self.driver.get(url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        current_time.custom_sleep(3, 4)
        html = self.driver.page_source

        return BeautifulSoup(html, 'html.parser')
    
    def get_first_element(self, url, by:By, css_selector):
        self.driver.get(url)
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((by, css_selector))
        )
        print(f'get_first_element : {css_selector} 찾기 성공!')
        return element

    def get_element(self, by:By, css_selector):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((by, css_selector))
        )
        print(f'get_element : {css_selector} 찾기 성공!')
        return element
    
    def get_first_elements(self, url, by:By, css_selector):
        self.driver.get(url)
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located((by, css_selector))
        )
        print(f'get_first_elements : {css_selector} 찾기 성공!')
        return element

    def get_elements(self, by:By, css_selector):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located((by, css_selector))
        )
        print(f'get_elements : {css_selector} 찾기 성공!')
        return element


    def get_category_urls(self, category_name):
        choices = {
            'dining':'DINING_URL',
            'google': 'GOOGLE_URL',
            'naver':'NAVER_URL'
        }
        env_name = choices[category_name]
        
        print(category_name)

        return os.getenv(env_name)

    @abstractmethod
    def crawl(self):
        """각 크롤러에서 구현"""
        pass

    def save_data(self, data, filename):
        with open(f'data/{self.category}/{filename}', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def close(self):
        if self.driver:
            self.driver.quit()
        
