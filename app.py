from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, Users, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)

# caminho banco de dados #tipo banco de dados sqlite:///
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
# evita que a aplicação envie avisos de rastreamento de modificações
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# chave de criptografia
app.config['JWT_SECRET_KEY'] = "DontTellAnyone"
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
    banco.create_all()


@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    # unauthorized
    return jsonify({'message': 'You have been logged out.'}), 401


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Users, '/usuarios')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from sql_alchjemy import banco
    banco.init_app(app)
    app.run(debug=True)
