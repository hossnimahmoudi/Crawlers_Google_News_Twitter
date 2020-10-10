from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from connection.mongo_connection import mongoConnection
from routes.google_news_data import GoogleNewsRoutes
from routes.google_news_launch import GoogleNewsStarter, config
from routes.stats_google_news import GoogleNewsStats
from routes.stats_twitter import TwitterStats
from routes.twitter_data import TwitterData
from routes.twitter_launch import TwitterLaunch


app = Flask(__name__)
api = Api(app)
CORS(app)

if __name__ == '__main__':

    # Establish mongo connection
    with mongoConnection(config):

        #   Route article
        #app.add_url_rule("/api/articles/", view_func=GoogleNewsRoutes().get)

        #   Route To Launch Google News
        api.add_resource(GoogleNewsStarter,      '/startgooglenews')

        #   Route Google News
        api.add_resource(GoogleNewsRoutes,      '/googlenewsarticles')

        #   Route To Launch Twitter Agent
        api.add_resource(TwitterLaunch,         '/starttwitter')

        #   Route TwitterData
        api.add_resource(TwitterData,           '/gettweets')

        #   Route StatsGoogleNews
        api.add_resource(GoogleNewsStats,       '/statsgooglenews')

        #   Route StatsTwitter
        api.add_resource(TwitterStats,          '/statstwitter')

        #   run app
        app.run(debug=True, host=config.app_host, port=config.app_port)

