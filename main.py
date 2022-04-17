#### do not run nigga


import json 
import scrapy
import numpy as np
import math


class Founder(scrapy.Spider):
    name='Drugs'

    def start_requests(self):
        
        urls = [
            'https://www.rxlist.com/',
        ]
        yield scrapy.Request(url=urls[0] , callback=self.parse)

    def parse(self, response):
        for i in range(10):
            for medi in response.selector.xpath(XpathA):
                yield {
                    'MediName' : medi.xpath(XpathAli + f'[{i}]/a').extract_first()
                }
                with open('rs.txt' , 'a') as w :
                    w.writable()
                    w.write(f' "MediName" : {medi.xpath(XpathAli + f"[{i}]/a").extract()} \n')
        # for i in range(10):
        #     for medi in response.selector.xpath(XpathB):
        #         yield {
        #             'MediName' : medi.xpath(XpathBli + f'[{i}]').extract_first()
        #         }
        #         with open('rs.txt' , 'a') as w :
        #             w.writable()
        #             w.write(f' "MediName" : {medi.xpath(XpathBli + f"[{i}]").extract_first()} \n')            

        # for i in range(10):
        #     for medi in response.selector.xpath(XpathC):
        #         yield {
        #             'MediName' : medi.xpath(XpathCli + f'[{i}]').extract_first()
        #         }
        #         with open('rs.txt' , 'a') as w :
        #             w.writable()
        #             w.write(f' "MediName" : {medi.xpath(XpathCli + f"[{i}]").extract_first()} \n')

        # for i in range(10):
        #     for medi in response.selector.xpath(XpathD):
        #         yield {
        #             'MediName' : medi.xpath(XpathDli + f'[{i}]').extract_first()
        #         }
        #         with open('rs.txt' , 'a') as w :
        #             w.writable()
        #             w.write(f' "MediName" : {medi.xpath(XpathDli + f"[{i}]").extract_first()} \n')

        # for i in range(10):
        #     for medi in response.selector.xpath(XpathA):
        #         yield {
        #             'MediName' : medi.xpath(XpathAli + f'[{i}]').extract_first()
        #         }
        #         with open('rs.txt' , 'a') as w :
        #             w.writable()
        #             w.write(f' "MediName" : {medi.xpath(XpathAli + f"[{i}]").extract_first()} \n')            
        # for i in range(10):
        #     for medi in response.selector.xpath(XpathA):
        #         yield {
        #             'MediName' : medi.xpath(XpathAli + f'[{i}]').extract_first()
        #         }
        #         with open('rs.txt' , 'a') as w :
        #             w.writable()
        #             w.write(f' "MediName" : {medi.xpath(XpathAli + f"[{i}]").extract_first()} \n')
        # for i in range(10):
        #     for medi in response.selector.xpath(XpathA):
        #         yield {
        #             'MediName' : medi.xpath(XpathAli + f'[{i}]').extract_first()
        #         }
        #         with open('rs.txt' , 'a') as w :
        #             w.writable()
        #             w.write(f' "MediName" : {medi.xpath(XpathAli + f"[{i}]").extract_first()} \n')



XpathA = '//*[@id="list-azA"]'
XpathB = '//*[@id="list-bzB"]'
XpathC = '//*[@id="list-czC"]'
XpathD = '//*[@id="list-dzD"]'
XpathE = '//*[@id="list-ezE"]'
XpathF = '//*[@id="list-fzF"]'
XpathG = '//*[@id="list-gzG"]'
XpathH = '//*[@id="list-hzH"]'
XpathI = '//*[@id="list-izI"]'
XpathK = '//*[@id="list-kzK"]'
XpathL = '//*[@id="list-lzL"]'
XpathM = '//*[@id="list-mzM"]'
XpathN = '//*[@id="list-nzN"]'
XpathO = '//*[@id="list-ozO"]'
XpathP = '//*[@id="list-pzP"]'
XpathR = '//*[@id="list-rzR"]'
XpathS = '//*[@id="list-szS"]'
XpathT = '//*[@id="list-tzT"]'
XpathU = '//*[@id="list-uzU"]'
XpathV = '//*[@id="list-vzV"]'
XpathW = '//*[@id="list-wzW"]'
XpathX = '//*[@id="list-xzX"]'
XpathY = '//*[@id="list-yzY"]'
XpathZ = '//*[@id="list-zzZ"]'




XpathAli = '//*[@id="list-azA"]/li'
XpathBli = '//*[@id="list-bzB"]/li'
XpathCli = '//*[@id="list-czC"]/li'
XpathDli = '//*[@id="list-dzD"]/li'
XpathEli = '//*[@id="list-ezE"]/li'
XpathFli = '//*[@id="list-fzF"]/li'
XpathGli = '//*[@id="list-gzG"]/li'
XpathHli = '//*[@id="list-hzH"]/li'
XpathIli = '//*[@id="list-izI"]/li'
XpathKli = '//*[@id="list-kzK"]/li'
XpathLli = '//*[@id="list-lzL"]/li'
XpathMli = '//*[@id="list-mzM"]/li'
XpathNli = '//*[@id="list-nzN"]/li'
XpathOli = '//*[@id="list-ozO"]/li'
XpathPli = '//*[@id="list-pzP"]/li'
XpathRli = '//*[@id="list-rzR"]/li'
XpathSli = '//*[@id="list-szS"]/li'
XpathTli = '//*[@id="list-tzT"]/li'
XpathUli = '//*[@id="list-uzU"]/li'
XpathVli = '//*[@id="list-vzV"]/li'
XpathWli = '//*[@id="list-wzW"]/li'
XpathXli = '//*[@id="list-xzX"]/li'
XpathYli = '//*[@id="list-yzY"]/li'
XpathZli = '//*[@id="list-zzZ"]/li'

