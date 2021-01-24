from flask import Flask
from flask_restful import Resource, reqparse, Api, Resource
from summarizer import Summarizer
from flaskr import app

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('query')

model = Summarizer()

class Summarize(Resource):

    def post(self):
        args = parser.parse_args()
        query = args['query']

        summary = model(query, ratio=0.5)

        output = {'summary': summary}

        return output

api.add_resource(Summarize, '/input')
