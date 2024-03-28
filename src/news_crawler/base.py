import requests
import asyncio
import aiohttp

from bs4 import BeautifulSoup

from enums.enums import NewsAgency, YnaCategory


class BaseCrawler:
    def __init__(self, agency: NewsAgency):
        if agency == NewsAgency.YNA:
            self.base_url = "https://www.yna.co.kr/"
        elif agency == NewsAgency.HANKYUNG:
            self.base_url = "https://www.hankyung.com/"
        else:
            raise ValueError(f"Wrong Agency : {agency}")

    async def async_get_html(self, url: str):
        """
        aiohttp 라이브러리를 이용해 주어진 url의 html을 비동기적으로 가져오는 메서드
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()  # 오류 발생 시 예외를 발생시킴
                    html = await response.text()  # 응답의 텍스트(HTML)를 가져옴
                    return html
        except aiohttp.ClientError as e:
            print(f"Error while crawling {url} : {e}")
            return None

    def get_html(self, url):
        """
        requests 라이브러리를 이용해 주어진 url의 html을 가져오는 메서드
        """

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print("Error while crawling {url} : {e}")
            return None

    async def _crawl_article_links(self, category):
        pass

    def get_article_links(self, category: str):
        """
        사용자가 선택한 category의 기사 제목과 url 크롤링
        """
        return asyncio.run(self._crawl_article_links(category))

    def get_article_content(self, article_url):
        """
        사용자가 선택한 기사의 원문
        """
        pass
