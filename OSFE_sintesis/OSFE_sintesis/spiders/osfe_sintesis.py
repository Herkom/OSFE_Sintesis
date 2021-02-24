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