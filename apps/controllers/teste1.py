from flask_restful import Api, Resource

class OtherRoute(Resource):
    def get(self):
        return {'message': 'This is another route'}