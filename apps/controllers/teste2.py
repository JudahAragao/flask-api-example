from flask_restful import Api, Resource

class OtherRoute2(Resource):
    def get(self):
        return {'message': 'This is another route'}