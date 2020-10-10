from flask import make_response, jsonify
from flask_restful import Resource
from models.twitter import TwitterSchema, TwitterModel

twitterSchemas = TwitterSchema(many=True)

class TwitterData(Resource):

    def get(self):
        lists = TwitterModel.objects.all()
        res = twitterSchemas.dump(lists)
        if res is not None:
            return make_response(jsonify(res), 200)
        else:
            return make_response(jsonify({"data": "Not Found"}), 400)