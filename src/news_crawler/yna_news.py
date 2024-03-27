from .main import BaseCrawler


class YnaCrawler(BaseCrawler):
    def get_article_links(self, category):
        test = {"c": "Test", "d": "DDDD"}
        return test

    def get_article_content(self, article_url):
        return article_url
