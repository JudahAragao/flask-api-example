# -*- coding: utf-8 -*-

# Importamos as classes API e Resource
from flask_restful import Api, Resource
from .controllers.teste1 import OtherRoute
from .controllers.teste2 import OtherRoute2

# Criamos uma classe que extende de Resource
class Index(Resource):

    # Definimos a operação get do protocolo http
    def get(self):

        # retornamos um simples dicionário que será automáticamente
        # retornado em json pelo flask
        return {'hello': 'world by apps'}


# Instânciamos a API do FlaskRestful
api = Api()


def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index
    api.add_resource(Index, '/')
    api.add_resource(OtherRoute, '/other')
    api.add_resource(OtherRoute2, '/other2')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)