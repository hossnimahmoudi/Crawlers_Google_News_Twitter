from flask import make_response
from flask.json import jsonify
from flask_restful import Resource
from models.google_news import GoogleNews, GoogleNewsSchema

googleNewsSchemas = GoogleNewsSchema(many=True)

class GoogleNewsRoutes(Resource):

    def get(self):
        lists = GoogleNews.objects.all()
        res = googleNewsSchemas.dump(lists)
        if res is not None:
            return make_response(jsonify(res), 200)
        else:
            return make_response(jsonify({"data": "Not Found"}), 400)