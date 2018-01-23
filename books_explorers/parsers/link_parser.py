from urllib.request import urlopen
from itertools import chain
from html.parser import HTMLParser


class LinkParser(HTMLParser):
    def reset(self):
        HTMLParser.reset(self)
        self.links = iter([])

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.links = chain(self.links, [value])


def gen_links(url):
    f = urlopen(url)
    parser = LinkParser()

    encoding = f.headers.get_content_charset() or 'UTF-8'

    for line in f:
        parser.feed(line.decode(encoding))

    return parser.links


gen_links("http://textfiles.com/etext/AUTHORS/")
