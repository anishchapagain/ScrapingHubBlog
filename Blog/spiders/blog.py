'''
Listing Blog for first 50 or less
from 'https://blog.scrapinghub.com/tag/web-scraping'

'''
import scrapy
from Blog.items import BlogItem


class BlogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = (
        'http://blog.scrapinghub.com/tag/web-scraping',
        ) #Main Page
    '''
    To be used for pagination purpose.
    
    start_urls = (
        'http://blog.scrapinghub.com/tag/web-scraping',
        'http://blog.scrapinghub.com/tag/web-scraping/page/2/',
        'http://blog.scrapinghub.com/tag/web-scraping/page/3/',
    )
    or
    start_urls = ['http://blog.scrapinghub.com/tag/web-scraping/page/%s' % page for page in xrange(1, 4)]
    '''
    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)
            
    '''Using XPath'''
    def parse(self, response):
        print("Response Type >>> ", type(response))
        rows = response.xpath("//div[@class='post-listing']//div[@class='post-item']")

        for row in rows:
            item = BlogItem()

            item['title'] = row.xpath('div[@class="post-header"]/h2/a/text()').extract_first()
            item['blogUrl'] = row.xpath('div[@class="post-header"]/h2/a/@href').extract_first()
            item['author_name'] = row.xpath('div[@class="post-header"]//span[@class="author"]/a/text()').extract_first().strip()
            item['author_url'] = row.xpath('div[@class="post-header"]//span[@class="author"]/a/@href').extract_first().strip()
            item['post_date'] = row.xpath('div[@class="post-header"]//span[@class="date"]/a/text()').extract_first().strip()
            item['comments'] = row.xpath('//span[@class="custom_listing_comments"]/a/text()').extract_first().strip()
            item['basic_description'] = row.xpath('div[@class="post-content"]//p/text()').extract_first()

            yield item

	'''
        nextPage = response.xpath("//div[@class='blog-pagination']//a[@class='next-posts-link']/@href").extract_first()
        if nextPage:
            print("Next Page URL: ",nextPage)
            # nextPage obtained from either XPath or CSS can be used.
            yield scrapy.Request(nextPage,callback=self.parse)
	'''
	#print('Completed')


    '''Using CSS Selectors'''
    '''
    def parseCSS(self, response):
        print("Response Type >>> ", type(response))
        rows = response.css(".post-item")

        for row in rows:
            item = BlogItem()
            item['title'] = row.css('div.post-header > h2 > a::text').extract_first().strip()
            item['blogUrl'] = row.css('div.post-header > h2 > a::attr(href)').extract_first().strip()
            item['author_name'] = row.css('span.author > a::text').extract_first().strip()
            item['author_url'] = row.css('span.author > a::attr(href)').extract_first().strip()
            item['post_date'] = row.css('span.date > a::text').extract_first().strip()
            item['comments'] = row.css('span.custom_listing_comments > a::text').extract_first().strip()
            item['basic_description'] = row.css('div.post-content > p::text').extract_first().strip()
            yield item

        nextPage = response.css("div.blog-pagination'] > a.next-posts-link::attr(href)").extract_first().strip()
        if nextPage:
            print("Next Page URL: ", nextPage)
      #     nextPage obtained from either XPath or CSS can be used.
            yield scrapy.Request(nextPage, callback=self.parse)

        print('Completed')
    '''
