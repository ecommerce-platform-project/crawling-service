from crawlers.base_crawler import BaseCrawler
from selenium.webdriver.common.by import By
import os




class DiningCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.category = 'dining'
        self.base_news_url = self.get_category_urls(self.category)


    def crawl(self):
        search_element = self.get_first_element(
            url=self.base_news_url,
            by=By.CSS_SELECTOR,
            css_selector='#root > header > div > div > div:nth-of-type(2) > div.Input__Wrap > input.Search__Input'
        )
        search_element.send_keys('오레노라멘')

        print(search_element.tag_name)

        click_element = self.get_element(
            by=By.CSS_SELECTOR,
            css_selector='#root > header > div > div > div:nth-of-type(2) > div.Input__Wrap > button.search'
        )
        if click_element.is_displayed():
            click_element.click()
            restaurant_list_element = self.get_element(
                    by=By.CSS_SELECTOR,
                    css_selector='#root > div.content > div.Scroll__List__Section > div.Poi__List__Wrap'
                )
            
            restaurant_url = self.get_element(
                    by=By.CSS_SELECTOR,
                    css_selector='#blockwJpwvXzEFYVj'
                ).get_attribute('href')

            # 아직 리뷰까지 못가져옴 확인해야함.
            restaurant_info_elements = self.get_first_element(
                url=restaurant_url,
                by=By.ID,
                css_selector='#div_review'
            )
            print(restaurant_url)
            input()



        
        



dining = DiningCrawler()

dining.crawl()
