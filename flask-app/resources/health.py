from flask import Response, request, jsonify
from flask_restful import Resource


class HealthApi(Resource):
    def get(self):
        return jsonify({'Health': 'healthy boi'})    
