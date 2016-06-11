import scrapy

from dbspider.items import DbspiderItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request

class DbSpider(scrapy.spiders.Spider):
	name = "dbmovie"
	allow_domains = ["douban.com"]
	start_urls = [
		"https://movie.douban.com/subject/20438962/comments"
	]

	def parse(self, response):
		sel = Selector(response)
		self.log('Url crawled: %s' % response.url)
		item = DbspiderItem()
		
		# Grade of movie
		item['grade'] = sel.xpath('//div[@class="comment"]/h3/span[@class="comment-info"]/span[contains(@class, "allstar")]/@title').extract()
		# Time of comment
		item['time'] = sel.xpath('//div[@class="comment"]/h3/span[@class="comment-info"]/span[@class=""]/text()[1]').extract()
		# Approval of comment
		item['approval'] = sel.xpath('//div[@class="comment"]/h3/span[@class="comment-vote"]/span[contains(@class, "votes")]/text()[1]').extract()
		# Comment of movie
		item['comment'] = sel.xpath('//div[@class="comment"]/p[@class=""]/text()[1]')
		yield item

		# with open('text', 'wb') as f:
		# 	f.write(response.body)
