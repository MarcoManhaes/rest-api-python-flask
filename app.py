from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, Users, UserRegister, UserLogin
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# caminho banco de dados #tipo banco de dados sqlite:///
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
# evita que a aplicação envie avisos de rastreamento de modificações
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# chave de criptografia
app.config['JWT_SECRET_KEY'] = "DontTellAnyone"

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Users, '/usuarios')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    from sql_alchjemy import banco
    banco.init_app(app)
    app.run(debug=True)
