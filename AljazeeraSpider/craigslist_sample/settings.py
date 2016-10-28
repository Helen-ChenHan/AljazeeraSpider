# Scrapy settings for craigslist_sample project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'craigslist_sample'

SPIDER_MODULES = ['craigslist_sample.spiders']
NEWSPIDER_MODULE = 'craigslist_sample.spiders'
ITEM_PIPELINES = {
    'craigslist_sample.pipelines.EmptyDrop': 100,
    'craigslist_sample.pipelines.SaveFiles': 200
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigslist_sample (+http://www.yourdomain.com)'
