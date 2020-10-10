import requests as req
from bs4 import BeautifulSoup
from newspaper import Article
from pandas._libs import json

from api.api_caller import ApiCaller
from common.file_writer import FileWriter


class GOOGLENewsCrawler:

    def __init__(self, server_url, query,  expiry_dates, proxy):
        self.server_url = server_url
        self.url_search = query
        self.expiry_dates = expiry_dates
        self.proxy = {'https': proxy}

    def get(self,):
        return ApiCaller.execute(self.server_url + str(self.url_search), req.get, params=None, headers=None, proxies=self.proxy)

    def crawl(self, output_folder):

            res = self.get()
            if res:
                FileWriter.write_to_file(output_folder=output_folder,
                                         file_name="google_news_{}.html", to_write=res,)
            return res

    def scrap(self):
        res = self.crawl(output_folder="/home/hosni/data-collection/data/google_news_data/")
        urls = self.get_urls(res)
        list = []
        df = []
        for url in urls:
            try:
                articl = Article(url)
                articl.download()
                articl.parse()
            except:
                print(' *** Unable To Download *** ', articl.url)
                print(articl.publish_date)
                continue
            df = {
                "headline": {"title": articl.title,
                             "abstract": articl.meta_description,
                             "authors": articl.authors,
                             "publish_date": articl.publish_date},
                "article": articl.text,
                "subjects": articl.keywords,
                "source": "GOOGLE NEWS",
                "url": articl.url,
                "type": "ARTICLE",
                #"html_code": articl.html,
            }


            list.append(json.dumps(df))
        return list



    @staticmethod
    def get_urls(htmlpage):

        soup = BeautifulSoup(htmlpage, 'lxml')
        dataframe = []
        for result_table in soup.findAll("div", {"class": "xrnccd"}):

            try:
                a_click = result_table.find("a")
                if "https://news.google.com" + str(a_click.get("href")).strip('/url?q='):
                    dataframe.append("https://news.google.com" + str(a_click.get("href")).strip('/url?q='))

                else:
                    pass
            except:
                print("Unable to get that element")
                continue

        return dataframe


