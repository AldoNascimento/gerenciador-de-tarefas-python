import json

from flask import Blueprint, Response
from flask_restx import Namespace, Resource, fields

import config
import dtos.UsuarioDTO
from dtos.ErroDTO import ErroDTO
from dtos.UsuarioDTO import UsuarioBaseDTO
from utils import Decorators

usuario_controller = Blueprint('usuario_controller', __name__)

api = Namespace(' Usuario')

user_fields = api.model('UsuarioBaseDTO', {
    'nome': fields.String,
    'email': fields.String,
})

@api.route('/', methods=['GET'])
class UsuarioController(Resource):
    @api.doc(responses={200: 'Login realizado com sucesso.'})
    @api.doc(responses={401: 'token inválido ou expirado.'})
    @api.response(200, 'sucesso', user_fields)
    @Decorators.token_required
    def get(self):

        try:
            return Response(
                json.dumps(UsuarioBaseDTO("Admin", config.LOGIN_TESTE).__dict__),
                status=200,
                mimetype='application/json'
            )
        except Exception:
            return Response(
                json.dumps(ErroDTO("Não foi possivel realizar a sua requisição, tente novamente", 500).__dict__),
                status=500,
                mimetype='application/json'
            )