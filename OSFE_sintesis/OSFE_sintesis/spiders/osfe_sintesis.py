import scrapy

newspapers = [
            {
                'name': 'Tabasco Hoy',
                'sourceURL': 'https://www.tabascohoy.com/',
                'links': '//h2[contains(@class,"zox-s-title")]/../@href',
                'body': {
                    'title': '//div[@class="zox-auto-post-main"]/article[1]//div[contains(@class, "zox-post-title-wrap")]//header//h1/text()',
                    'summary': '//div[@class="zox-auto-post-main"]/article[1]//div[contains(@class, "zox-post-title-wrap")]//header//span/p/text()',
                    'date_and_or_author': '//div[@class="zox-auto-post-main"]/article[1]//div[contains(@class, "zox-post-title-wrap")]//header//meta/@content',
                    'content': '//div[@class="zox-auto-post-main"]/article[1]//div[contains(@class,"zox-article-wrap")]/div[@class="zox-post-main-grid"]//div[contains(@class, "zox-post-body ")]//*[not(contains(@class, "jp-related"))]//text()'
                }
            },
            {
                'name': 'Diario de Tabasco',
                'sourceURL': 'http://www.diariodetabasco.mx/',
                'links': '//div[contains(@class, "container") and contains(@class, "general_wrap")]//a/@href[contains(.,"diariodetabasco") and not(contains(.,"https://twitter.com/share?")) and not(contains(.,"https://www.youtube.com/user/")) ]',
                'body': {
                    'title': '//h1',
                    'date_and_or_author' :'//div[contains(@class,"autoria-post")]//span//text()',
                    'summary': '//div[@class="post-content"]//div[contains(@class,"info-post")]//h2/text()',
                    'content': '//div[@class="post-content"]//div[contains(@class,"info-post")]//p//text()',
                }
            },
            {
                'name': 'XEVT',
                'sourceURL': 'https://www.xevt.com/',
                'links': '//h5/a/@href[not(contains(.,"javascript"))] | //h6/a/@href[not(contains(.,"javascript"))] | //h2/../../@href[not(contains(.,"javascript"))] | //h6/../../@href[not(contains(.,"javascript"))]',
                'body':{
                    'title': '//h1[@class="post__title"]/text()',
                    'date_and_or_author': '//div[@class="post__author"]/span/text() | //div[@class="post__author"]/text()[2]',
                    'content': '//div[@class="post__content"][1]//text()',
                }
            },
            {
                'name': 'XEVA',
                'sourceURL': 'http://xeva.com.mx/',
                'links': '//a/@href[contains(.,"nota")]',
                'body': {
                    'title': '//table[@id="contenido"]//tbody/tr/td//h1/text()',
                    'date_and_or_author': '//table[@id="contenido"]//tbody/tr/td//div[@class="fadoce" and not(@style)]/text()',
                    'content': '//table[@id="contenido"]//tbody/tr/td//div[@id="contenido-nota"]/p/text()',
                }
            },
            {
                'name': 'Grupo VX',
                'sourceURL': 'https://www.grupovx.com/',
                'links': '//article[contains(@id,"post")]/h2/a/@href',
                'body': {
                    'title': '//div[@id="content-area"]//article[contains(@id,"post")]//h1/text()',
                    'date_and_or_author': '//div[@id="content-area"]//article[contains(@id,"post")]//span[contains(@class,"author")]/a/text()',
                    'content': '//div[@id="content-area"]//article[contains(@id,"post")]//div[@class="entry-content"]/p//text()',
                }
            },
            {
                'name': 'Heraldo de Tabasco',
                'sourceURL': 'https://www.elheraldodetabasco.com.mx/',
                'links': '//h4/a/@href',
                'body':{
                    'title':'//section//h1[@class="title"]/text()',
                    'date_and_or_author':'//section//p[@class="published-date"]/text() | //section//div[contains(@class,"affix-start")]/p/text()',
                    'summary':'//section//h3[@class="subtitle"]/text()',
                    'content':'//section//*[contains(@class,"content")]//p/text()',
                }
            },
            {
                'name': 'Novedades',
                'sourceURL': 'https://novedadesdetabasco.com.mx/',
                'links': '//h2//a/@href|//h3//a/@href',
                'body':{
                    'title':'//div[contains(@class,"content")]//article//div[@class="post-inner"]/h1/*/text()',
                    'date_and_or_author':'//div[contains(@class,"content")]//article//div[@class="post-inner"]//*[contains(@class,"author")]//a/text()',
                    'content':'//div[contains(@class,"content")]//article//div[@class="post-inner"]//div[@class="entry"]/p/text()',
                }
            },
            {
                'name': 'Rumbo Nuevo',
                'sourceURL': 'https://www.rumbonuevo.com.mx/',
                'links': '//a/@href',
                'body':{
                    'title':'//header/h1/text()',
                    'date_and_or_author':'//header//div//span/time/text() | //header//div//span/a/text()',
                    'content':'//div[contains(@id,"content-main")]/p/text()',
                }
            },
            {
                'name': 'Diario Presente',
                'sourceURL': 'https://www.diariopresente.mx/',
                'links': '//*[contains(@class,"caption") or contains(@class,"top-stories")]//a/@href',
                'body':{
                    'title':'//article/div[@class="detail"]/div[@class="caption"]/text()',
                    'date_and_or_author':'//article/div[@class="detail"]/div[@class="info"]//text()',
                    'content':'//article/div[@class="description"]/p//text()',
                }
            },
            {
                'name': 'La Verdad',
                'sourceURL': 'https://www.la-verdad.com.mx/',
                'links': '//h1/a/@href | //h3/a/@href | //p/a/@href | //div/i/following-sibling::a/@href',
                'body':{
                    'title':'//div[@class="magazine-news"]//h1/text()',
                    'summary':'//div[@class="magazine-news"]//p[@class="lead text-danger"]/text()',
                    'date_and_or_author':'//div[@class="magazine-news"]//p[@class="text-warning"]/text()',
                    'content':'//div[@class="magazine-news"]//div[not(@class="row")]/br/../text() | //div[@class="magazine-news"]//br/../text()',
                }
            },
            {
                'name': 'CORAT',
                'sourceURL': 'https://corat.mx/noticias/',
                'links': '//li//h5/a/@href | //div[contains(@class,"slider") and contains(@class,"wrapper")]//ul/li/@data-link',
                'body':{
                    'title': '//h2[@class="entry-title"]/text()',
                    'date_and_or_author': '//span//time/text()',
                    'content': '//div[@class="the_content_wrapper"]//*//text()',
                }
            },
    ]

class SpiderOSFESintesis(scrapy.Spider):

    name = 'osfeSintesis'

    start_urls = [ sub['sourceURL'] for sub in newspapers ]

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

        for paper in newspapers:
            if response.url == paper['sourceURL']:
                links_declassified.append(response.xpath(paper['links']).getall())

                for link in links_declassified or []:

                    depurated_links = list(dict.fromkeys(link))

                    for depurado in depurated_links:
                        yield response.follow(depurado, callback=self.parse_links, cb_kwargs={'origin': paper['name']})

    
    def parse_links(self, response, **kwargs):

        origin = kwargs['origin']

        for paper in newspapers:
            if origin == paper['name']:
                estructura = {}
                elementos = paper['body']
                estructura['origen'] = origin
                estructura['link'] = response.url

                for element in elementos:
                    estructura[str(element)] = response.xpath(elementos[element]).getall()
                
                yield {
                    'article' : estructura
                }