import scrapy
import numpy as np
from scrapy.loader import ItemLoader
from loader import spideritemloader


class Engine(scrapy.Spider):
    
    name = 'Engine'    

    def start_requests(self):
        

        urls = [

         "https://www.rxlist.com/drugs/alpha_a.htm",
         "https://www.rxlist.com/drugs/alpha_b.htm",
         "https://www.rxlist.com/drugs/alpha_c.htm",
         "https://www.rxlist.com/drugs/alpha_d.htm",
         "https://www.rxlist.com/drugs/alpha_e.htm",
         "https://www.rxlist.com/drugs/alpha_f.htm",
         "https://www.rxlist.com/drugs/alpha_g.htm",
         "https://www.rxlist.com/drugs/alpha_h.htm",
         "https://www.rxlist.com/drugs/alpha_i.htm",
         "https://www.rxlist.com/drugs/alpha_j.htm",
         "https://www.rxlist.com/drugs/alpha_k.htm",
         "https://www.rxlist.com/drugs/alpha_l.htm",
         "https://www.rxlist.com/drugs/alpha_m.htm",
         "https://www.rxlist.com/drugs/alpha_n.htm",
         "https://www.rxlist.com/drugs/alpha_o.htm",
         "https://www.rxlist.com/drugs/alpha_p.htm",
         "https://www.rxlist.com/drugs/alpha_q.htm",
         "https://www.rxlist.com/drugs/alpha_r.htm",
         "https://www.rxlist.com/drugs/alpha_s.htm",
         "https://www.rxlist.com/drugs/alpha_t.htm",
         "https://www.rxlist.com/drugs/alpha_u.htm",
         "https://www.rxlist.com/drugs/alpha_v.htm",
         "https://www.rxlist.com/drugs/alpha_w.htm",
         "https://www.rxlist.com/drugs/alpha_x.htm",
         "https://www.rxlist.com/drugs/alpha_y.htm",
         "https://www.rxlist.com/drugs/alpha_z.htm",

        
        ]
        
        for url in urls :
        
            yield scrapy.Request(url=url , callback=self.parse)

    def parse(self, response):
        
        for res in response.selector.xpath("//div[@class='AZ_results']"):
       

            yield {
                
         
                'name' : res.xpath("//div[@class='AZ_results']/ul/li/a/text()").extract(),
            }
    