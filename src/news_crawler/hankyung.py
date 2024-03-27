from .main import BaseCrawler


class HankyungCrawler(BaseCrawler):
    def get_article_links(self, category):
        test = {"a": "Test", "b": "DDDD"}
        return test

    def get_article_content(self, article_url):
        pass
