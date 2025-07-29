from crawlers.base_crawler import BaseCrawler
import os




class NewsCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.category = 'news'
        self.base_news_url = self.get_category_urls(self.category)
        self.press_url_list = self.get_press_urls()

    def get_press_urls(self):
        news_press_urls = []

        urls = self.base_news_url
        soup = self.get_soup(url=urls)

        press_wrap = soup.find('div', 'pressWrap')
        press_list = press_wrap.find('ul', 'pressList')
        press_block_list_li = press_list.find_all('li', 'block')

        for press_block_li in press_block_list_li:
            press_li_list = press_block_li.find_all('li')
            for press_li in press_li_list:
                press = {}
                press_a = press_li.find('a')
                # print(f'a pressName {press_a.text} href = {press_a['href']}')

                """
                name : 언론사 이름,
                url : 언론사 기사 목록

                위 딕션널리를 news_press_urls 리스트로 담음
                """
                sub_str = '/news/'
                press['name'] = press_a.text if press_a else None
                press['url'] = self.base_news_url+press_a['href'][len(sub_str)::] if press_a['href'] else None
                news_press_urls.append(press)

        print(news_press_urls)  

        return news_press_urls
           
    
    def crawl(self):
        return super().crawl()


news = NewsCrawler()

news.crawl()