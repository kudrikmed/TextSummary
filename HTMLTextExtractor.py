import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


class HTMLTextExtractor:
    def __init__(self):
        pass

    @staticmethod
    def tag_visible(element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    @staticmethod
    def text_from_html(body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(string=True)
        visible_texts = filter(HTMLTextExtractor.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)

    def get_text_from_url(self, url):
        response = requests.get(url)
        html = response.content
        return self.text_from_html(html)
