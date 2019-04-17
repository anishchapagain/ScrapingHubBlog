import scrapy
from Blog.items import BlogItem


class BlogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = ('http://blog.scrapinghub.com/tag/web-scraping',)

    def parse(self, response):
        print("Response Type >>> ", type(response))
        rows = response.xpath("//div[@class='post-listing']//div[@class='post-item']")
        c=1
        for row in rows:
            print("Inside Row ")
            item = BlogItem()

            item['title'] = row.xpath('div[@class="post-header"]/h2/a/text()').extract_first()

            item['blogUrl'] = row.xpath('div[@class="post-header"]/h2/a/@href').extract_first()
            item['author_name'] = row.xpath(
                'div[@class="post-header"]//span[@class="author"]/a/text()').extract_first().strip()
            item['author_url'] = row.xpath(
                'div[@class="post-header"]//span[@class="author"]/a/@href').extract_first().strip()
            item['post_date'] = row.xpath(
                'div[@class="post-header"]//span[@class="date"]/a/text()').extract_first().strip()
            item['comments'] = row.xpath('//span[@class="custom_listing_comments"]/a/text()').extract_first().strip()
            desc=row.xpath('div[@class="post-content"]//p/text()').extract_first()
            print("DESC >> ",desc)
            if desc:
                item['basic_description'] = row.xpath('div[@class="post-content"]//p/text()').extract_first()
            else:
                item['basic_description'] = ''
            c+=1
            yield item
