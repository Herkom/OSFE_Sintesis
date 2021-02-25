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

    custom_settings = {
        'FEEDS':{
            'osfeSintesis.json':{
                'format': 'json',
                'encoding': 'utf8',
                'indent': 4,
            }
        }
    }

    def parse(self, response):

        links_declassified = []
        
        press = {
            'Tabasco Hoy': {
                'name': 'Tabasco Hoy',
                'url': 'https://www.tabascohoy.com/'
            },
            'Diario de Tabasco': {
                'name': 'Diario de Tabasco',
                'url': 'http://www.diariodetabasco.mx/'
            },
            'XEVT': {
                'name': 'XEVT',
                'url': 'https://www.xevt.com/'
            },
            'XEVA': {
                'name': 'XEVA',
                'url': 'http://xeva.com.mx/'
            },
            'Grupo VX': {
                'name': 'Grupo VX',
                'url': 'https://www.grupovx.com/'
            },
            'Heraldo de Tabasco': {
                'name': 'Heraldo de Tabasco',
                'url': 'https://www.elheraldodetabasco.com.mx/'
            },
            'Novedades': {
                'name': 'Novedades',
                'url': 'https://novedadesdetabasco.com.mx/'
            },
            'Rumbo Nuevo': {
                'name': 'Rumbo Nuevo',
                'url': 'https://www.rumbonuevo.com.mx/'
            },
            'Diario Presente': {
                'name': 'Diario Presente',
                'url': 'https://www.diariopresente.mx/'
            },
            'La Verdad': {
                'name': 'La Verdad',
                'url': 'https://www.la-verdad.com.mx/'
            },
            'CORAT': {
                'name': 'CORAT',
                'url': 'https://corat.mx/noticias/'
            },
        }

        if response.url == press['Tabasco Hoy']['url']:
            links_declassified.append(response.xpath('//h2[contains(@class,"zox-s-title")]/../@href').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['Tabasco Hoy']['name'],
                    'url': link
                }
        elif response.url == press['Diario de Tabasco']['url']:
            links_declassified.append(response.xpath('//div[contains(@class, "container") and contains(@class, "general_wrap")]//a/@href[contains(.,"diariodetabasco") and not(contains(.,"https://twitter.com/share?")) and not(contains(.,"https://www.youtube.com/user/")) ]').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['Diario de Tabasco']['name'],
                    'url': link
                }
        elif response.url == press['XEVT']['url']:
            links_declassified.append(response.xpath('//h5/a/@href[not(contains(.,"javascript"))] | //h6/a/@href[not(contains(.,"javascript"))] | //h2/../../@href[not(contains(.,"javascript"))] | //h6/../../@href[not(contains(.,"javascript"))]').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['XEVT']['name'],
                    'url': link
                }
        elif response.url == press['XEVA']['url']:
            links_declassified.append(response.xpath('//a/@href[contains(.,"nota")]').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['XEVA']['name'],
                    'url': link
                }
        elif response.url == press['Grupo VX']['url']:
            links_declassified.append(response.xpath('//article[contains(@id,"post")]/h2/a/@href').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['Grupo VX']['name'],
                    'url': link
                }
        elif response.url == press['Heraldo de Tabasco']['url']:
            links_declassified.append(response.xpath('//h4/a/@href').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['Heraldo de Tabasco']['name'],
                    'url': link
                }
        elif response.url == press['Novedades']['url']:
            links_declassified.append(response.xpath('//h2//a/@href|//h3//a/@href').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['Novedades']['name'],
                    'url': link
                }
        elif response.url == press['Rumbo Nuevo']['url']:
            links_declassified.append(response.xpath('//a/@href').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['Rumbo Nuevo']['name'],
                    'url': link
                }
        elif response.url == press['Diario Presente']['url']:
            links_declassified.append(response.xpath('//*[contains(@class,"caption") or contains(@class,"top-stories")]//a/@href').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['Diario Presente']['name'],
                    'url': link
                }
        elif response.url == press['La Verdad']['url']:
            links_declassified.append(response.xpath('//h1/a/@href | //h3/a/@href | //p/a/@href | //div/i/following-sibling::a/@href').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['La Verdad']['name'],
                    'url': link
                }
        elif response.url == press['CORAT']['url']:
            links_declassified.append(response.xpath('//li//h5/a/@href | //div[contains(@class,"slider") and contains(@class,"wrapper")]//ul/li/@data-link').getall())

            for link in links_declassified or []:
                yield {
                    'origin': press['CORAT']['name'],
                    'url': link
                }

