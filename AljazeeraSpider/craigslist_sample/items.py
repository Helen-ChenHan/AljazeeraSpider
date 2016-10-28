from scrapy.item import Item, Field

class ALJItem(Item):
    title = Field()
    link = Field()
    article = Field()
    date = Field()
