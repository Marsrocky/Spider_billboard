import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
	name = "dmoz"
	allow_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"

	]

	def parse(self, response):
		for sel in response.xpath('//section[@class="results sites"]'):
			item = DmozItem()
			item['title'] = sel.xpath('//div[@class="site-title"]/text()').extract()
			item['link'] = sel.xpath('//div[@class="title-and-desc"]/a/attribute::href').extract()
			item['desc'] = sel.xpath('//div[@class="title-and-desc"]/div[@class="site-descr "][1]/text()').extract()
			yield item
