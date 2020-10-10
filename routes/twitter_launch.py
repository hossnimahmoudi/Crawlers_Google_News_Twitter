import datetime

from flask import make_response, jsonify
from flask_restful import Resource
from crawlers.twitter_crawlers.twitter import search_for_hashtags
import json
from models.twitter import TwitterModel


class TwitterLaunch(Resource):


    def get(self):
        consumer_key = "wpjfstyikV9KrXhfmiVZfEc4y"
        consumer_secret = "D9nPYlE3u8piuGeToToUU61m3IpMiKPhGZUmvziHJsPHs5Qrjo"
        access_token = "1085687624004718592-OFt18RwTk2Fjs8iIkxNQJ7hGCTRc8k"
        access_token_secret = "aJbXM453ABM6XYjZdadkDbSVfTuW8W4UlSnyheevlZAIY"
        query = "donald trump"

        crawling_date = datetime.datetime.now()

        clean_data_twitter = search_for_hashtags(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret,
            query
        )

        if clean_data_twitter:
            for tweet in clean_data_twitter:
                res = json.loads(tweet)
                data = TwitterModel(res['created_at'], res['full_text'],
                                    res['place'], res['username'],
                                    res['user_followers'], res['user_id_str'],
                                    res['user_location'], res['description']
                                    )
                data.save(validate=False)

            return make_response(jsonify({"Collecting data from Twitter": "Done !"}), 200)
        else:
            return make_response(jsonify({"Collecting from Twitter": "Error "}), 400)


