import requests
from bs4 import BeautifulSoup

from enums.enums import NewsAgency


class BaseCrawler:
    def __init__(self, agency: NewsAgency):
        if agency == NewsAgency.YNA:
            self.base_url = "https://www.yna.co.kr/"
        elif agency == NewsAgency.HANKYUNG:
            self.base_url = "https://www.hankyung.com/"
        else:
            raise ValueError(f"Wrong Agency : {agency}")

    def parse_html(self, url):
        """
        requests 라이브러리를 이용해 주어진 url의 html을 가져오는 메서드
        """

        try:
            response = requests.get(url)
            response.raise_for_status()
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            return soup

        except requests.RequestException as e:
            print("Error while crawling {url} : {e}")
            return None

    def get_title_url(self, category: str):
        """
        사용자가 선택한 category의 기사 제목과 url 크롤링
        """
        pass

    def get_article_content(self, article_url):
        """
        사용자가 선택한 기사의 원문
        """
        pass
