from flask import make_response, jsonify
from flask_restful import Resource
from models.google_news import GoogleNewsSchema, GoogleNews

googleNewsSchemas = GoogleNewsSchema(many=True)


class GoogleNewsStats(Resource):

    def get(self):
        lists = GoogleNews.objects.all()
        if lists:
            nombre_articles = 0

            for article in lists:
                nombre_articles = nombre_articles + 1

            return make_response(jsonify({"Le nombre des articles Google News est": nombre_articles}), 200)
        else:
            return make_response(jsonify({"data": "Not Found"}), 400)

