import scrapy

class SpiderOSFESintesis(scrapy.Spider):
    name = 'osfeSintesis'
    start_urls = [
        'https://www.tabascohoy.com/',
        'http://www.diariodetabasco.mx/',
        'https://www.xevt.com/',
        'http://xeva.com.mx/',
        'https://www.grupovx.com/',
        'https://www.elheraldodetabasco.com.mx/',
        'https://novedadesdetabasco.com.mx/',
        'https://www.rumbonuevo.com.mx/',
        'https://www.diariopresente.mx/',
        'https://www.la-verdad.com.mx/',
        'https://corat.mx/noticias/'
    ]

    custom_setting = {
        'FEED_URI': 'osfe_sintesis.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        if response.url = start_urls[0]:

        elif response.url = start_urls[1]:
        
        elif response.url = start_urls[2]:

        elif response.url = start_urls[3]:
        
        elif response.url = start_urls[4]:
        
        elif response.url = start_urls[5]:
        
        elif response.url = start_urls[6]:
        
        elif response.url = start_urls[7]:
        
        elif response.url = start_urls[8]:
        
        elif response.url = start_urls[9]:
        
        elif response.url = start_urls[10]:
        