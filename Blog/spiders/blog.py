import scrapy
from Blog.items import BlogItem


class BlogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = ('http://blog.scrapinghub.com/tag/web-scraping',)

    custom_settings = {
        'Referer':'https://blog.scrapinghub.com',
        'Cookie':'_gcl_au=1.1.1460105923.1553089613; _ga=GA1.2.1791698862.1553089614; __hs_opt_out=yes; intercom-id-hcwc7e8c=f1330569-a8b9-49c9-a21a-3ae9e789306b; _gid=GA1.2.1659281855.1555341507; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2298accf41-a760-4659-94e0-f1146f721838%22; csrftoken2=0l0IxBm5pe5KM44jdlISbCW8dMLN9C4DUOJD7ibUFzOP1cQok9Tbb5ulSdhynz48; __cfduid=d05e885c0d39c44d99bb7b2c3e0479de01555512786; __cfruid=ca2bc827d4845e94e32c5bf3264b42a1693402ea-1555512786; intercom-session-hcwc7e8c=WW5iWHdLdE84b3lTT3FBSGZQQzRFQVhFVG0reW4zcExUc1NpUk9pV2J3UzZnUTIvUGZKZUp2UmlJK2d0MkN6bS0tUzgrWEl0NFc2ZW5RNDFLWU5qWXFHUT09--ea3966bb9a147e5ba68d6a037620d40b02115b16; _hp2_id.2271566029=%7B%22userId%22%3A%220407677887482951%22%2C%22pageviewId%22%3A%220390697142752548%22%2C%22sessionId%22%3A%221356436377924511%22%2C%22identity%22%3A%22anishchapagain%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; _gat_UA-20306421-1=1',
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    # start_urls = ('http://www.espncricinfo.com/series/8048/scorecard/1178408/sunrisers-hyderabad-vs-chennai-super-kings-33rd-match-indian-premier-league-2019',)
    # def start_requests(self):
    #     for u in self.start_urls:
    #         yield scrapy.Request(u, callback = self.parse, dont_filter=True, encoding='utf-8')
    def parse(self, response):
        print("Response Type >>> ", type(response))
        rows = response.xpath("//div[@class='post-listing']//div[@class='post-item']")
        print("Response Type >>> ", type(response))
        print(response.url)
        print(response.body)

        for row in rows:
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
            item['basic_description'] = row.xpath('div[@class="post-content"]//p/text()').extract_first()

            yield item

    def parseCSS(self, response):
        print("Response Type >>> ", type(response))
        print(response.url)
        # response = scrapy.http.HtmlResponse('http://www.scrapinghub.com/',encoding="utf-8",request=scrapy.Request('http://www.scrapinghub.com'))
        # print("Response Type >>> ", type(response))
        # print(response.url)
        # response = scrapy.http.HtmlResponse(response.url,encoding='utf-8')#,body=response.body.decode('utf-8'),)
        # print(response.body)

        # response = scrapy.Request('http://www.scrapinghub.com')
        print("Response Type >>> ", type(response))
        print(response.url)
        print(response.body.decode("utf-8"))
        response = unicode(response.body.decode(response.encoding)).encode('utf-8')
        print("Response Type >>> ", type(response))

        print(response.url)
        print(response.body)

        # rows = response.css('div[class="post-item"]')
        rows = response.css('title').extract()
        print("Ready TO LOOP")
        print("count >> ", rows.__len__())
        print(rows)
        '''
        pass
        c=1
        for row in rows:
            print("Inside Row ",c)
            #print(row.css('.post-header > h2 > a::text').extract_first())
            #print(row.css('.post-header h2 a::text').extract_first())
            item = BlogItem()
            item['title'] = row.css('div.post-header > h2 > a::text').extract_first().strip()
            item['blogUrl'] = row.css('div.post-header > h2 > a::attr(href)').extract_first().strip()
            item['author_name'] = row.css('span.author > a::text').extract_first().strip()
            item['author_url'] = row.css('span.author > a::attr(href)').extract_first().strip()
            item['post_date'] = row.css('span.date > a::text').extract_first().strip()
            item['comments'] = row.css('span.custom_listing_comments > a::text').extract_first().strip()
            desc=row.css('[class=post-content] p::text').extract_first()
            print("DESC >> ",desc)
            if desc:
                item['basic_description'] = desc
            else:
                item['basic_description'] = ''
            c+=1
            yield item
        '''
        print('Completed')
