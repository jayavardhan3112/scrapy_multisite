# Import Statements
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scraper.items import ScraperItem


# Function to remove newline,tabspace and whitespace characters using RegEx
def CleanTag(textToClean):
    finaltext = []
    for text in textToClean:
        cleanText = re.sub("(\n|\t)*", "", text)
        cleanText = cleanText.strip()
        if (cleanText != ""):
            finaltext.append(cleanText)
    return finaltext


class MySpider(CrawlSpider):
    name = "mySpider"
    rule = (Rule(LinkExtractor(canonicalize=True, unique=True), callback="parse", follow=True))

    # Function to initialise start url and allowed domain.
    def __init__(self, url=None, domain=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['%s' % url]
        self.allowed_domains = [domain]

    # Function to generate links from a starting URL
    def parse(self, response):
        allLinks = []
        allLinks.append(response.request.url)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        print(links[1])
        items = {}
        for link in links:
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    allLinks.append(link.url)

        # Passing each page to parse_items to retrieve content
        for link in allLinks:
            yield scrapy.Request(link, callback=self.parse_items)

    # Function to crawl a given page and create an Item which is sent to the pipeline.
    def parse_items(self, response):
        p_tags = response.xpath('//p/text()').extract()
        content = CleanTag(p_tags)
        currentPage = response.request.url
        item = ScraperItem()
        item['page'] = currentPage
        item['content'] = content
        yield item
        return
