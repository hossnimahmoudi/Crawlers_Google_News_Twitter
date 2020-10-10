import os
import json


class Config:

    def __init__(self, fileName):
        self.fileName = fileName
        self.data_path = None
        self.googleNews_base_url = None
        self.googleNews_expiry_days = None
        self.googleNews_proxy = None
        self.googleNews_output_folder = None
        self.googleNews_query = None
        self.app_port = None
        self.app_host = None
        self.mongo_collection = None
        self.mongo_uri = None
        self.db_name = None
        self.mongo_port = None
        self.mongo_username = None
        self.mongo_password = None
        self.mongo_collection = None
        self.mongo_auth_source = None
        # self.ACCESS_TOKEN = None
        # self.ACCESS_TOKEN_SECRET = None
        # self.CONSUMER_KEY = None
        # self.CONSUMER_SECRET = None
        self.init_config()

    def init_config(self):
        if not os.path.isfile(self.fileName):
            raise print('file {} not exist.'.format(self.fileName))
        with open(self.fileName) as data_file:
            root_data_item = json.load(data_file)
            print(root_data_item)
        self.data_path = root_data_item.get("data_path")
        # configuration application
        data_app = root_data_item.get("application", {})
        self.app_port = data_app.get("port")
        self.app_host = data_app.get("host")
        # part google news
        google_news = root_data_item.get("googleNews", {})
        self.googleNews_query = google_news.get("query")
        self.googleNews_base_url = google_news.get("base_url")
        if not self.googleNews_base_url:
            raise print("empty base_url for google_news_crawlers")

        self.googleNews_expiry_days = google_news.get("expiry_days")
        if not self.googleNews_expiry_days:
            raise print("empty expiry_days for google_news_crawlers")

        self.googleNews_proxy = google_news.get("proxy")
        if not self.googleNews_proxy:
            raise print("empty proxy for google_news_crawlers")

        self.googleNews_output_folder = "{}{}".format(self.data_path, google_news.get("output_folder"))

        if not self.googleNews_output_folder:
            raise print("empty output_folder for google_news_crawlers")
        data = google_news.get("mongo", {})
        self.mongo_port = data.get("port")
        self.mongo_username = data.get("username")
        self.mongo_password = data.get("password")
        self.db_name = data.get("db_name")
        self.mongo_uri = data.get("mongo_uri")
        self.mongo_collection = data.get("mongo_collection")
        self.mongo_auth_source = data.get("mongo_auth_source")

        # twitter = root_data_item.get("twitter",{})
        # self.ACCESS_TOKEN = twitter.get("ACCESS_TOKEN")
        # self.ACCESS_TOKEN_SECRET = twitter.get("ACCESS_TOKEN_SECRET")
        # self.CONSUMER_KEY = twitter.get("CONSUMER_KEY")
        # self.CONSUMER_SECRET = twitter.get("CONSUMER_SECRET")
