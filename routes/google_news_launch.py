import json
import os
from flask import make_response, jsonify
from flask_restful import Resource
from config.config import Config
from crawlers.google_news_crawlers.google_news_crawlers import GOOGLENewsCrawler
from models.google_news import GoogleNews



env_var = 'WEB_CRAWLER_CONFIG_FILE'
os.environ[env_var] = os.getcwd() + "/config.json"
rv = os.environ.get(env_var)
config = Config(rv)



class GoogleNewsStarter(Resource):
    def get(self):

        google_news = GOOGLENewsCrawler(config.googleNews_base_url, config.googleNews_query,
                                        config.googleNews_expiry_days, config.googleNews_proxy)

        #  save clean dat to mongo
        clean_data = google_news.scrap()

        if clean_data:
            for r in clean_data:
                res = json.loads(r)
                data = GoogleNews(res['headline'], res['article'],
                                  res['subjects'], res['source'],
                                  res['url'], res['type'], )
                GoogleNews.save(data)

            return make_response(jsonify({"Collecting data from Google News": "Done !"}), 200)
        else:
            return make_response(jsonify({"Collecting data from Google News": "Error"}), 400)