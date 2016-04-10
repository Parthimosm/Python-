from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()


    def handle_starttag(self, base_url, page_url):
        if base_url == 'a':
            for (attribute, value) in page_url:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links


    def error(self, message):
        pass




