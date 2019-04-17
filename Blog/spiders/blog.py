import scrapy
from Blog.items import BlogItem


class BlogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = ('https://blog.scrapinghub.com/tag/web-scraping',)

    def parseCSS(self, response):
        print("Response Type >>> ", type(response))
        rows = response.css(".post-item")
        print("Ready TO LOOP")
        c=1
        for row in rows:
            print("Inside Row")
            item = BlogItem()
            item['title'] = row.css('div.post-header > h2 > a::text').extract_first().strip()
            item['blogUrl'] = row.css('div.post-header > h2 > a::attr(href)').extract_first().strip()
            item['author_name'] = row.css('span.author > a::text').extract_first().strip()
            item['author_url'] = row.css('span.author > a::attr(href)').extract_first().strip()
            item['post_date'] = row.css('span.date > a::text').extract_first().strip()
            item['comments'] = row.css('span.custom_listing_comments > a::text').extract_first().strip()
            desc=row.css('div.post-content > p::text').extract_first().strip()
            print("DESC >> ",desc)
            if desc:
                item['basic_description'] = desc
            else:
                item['basic_description'] = ''
            c+=1
            yield item


    print('Completed')
