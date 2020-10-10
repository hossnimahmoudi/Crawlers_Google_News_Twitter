from flask import make_response, jsonify
from flask_restful import Resource

from models.twitter import TwitterModel, TwitterSchema

twitterSchemas = TwitterSchema(many=True)


class TwitterStats(Resource):
    def get(self):
        articles = TwitterModel.objects.all()
        if articles:
            nombre_articles = 0
            for article in articles:
                nombre_articles = nombre_articles+1
            return make_response(jsonify({"La nombre des tweets est": nombre_articles}), 200)
        else:
            return make_response(jsonify({"data": "Not Found"}), 400)