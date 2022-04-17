import scrapy
from scrapy.loader.processors import MapCompose , Join , TakeFirst



def remover(value):

    return value.replace(u"\u201b" , "").replace(u"\u201c" , "")

class spideritemloader(scrapy.Item):
    name = scrapy.Field(
        input_processor = MapCompose(str.strip, remover),
        output_processor = TakeFirst()
    )

    dangertype = scrapy.Field(
        input_processor = MapCompose(str.strip, remover),
        output_processor = TakeFirst()  
    )