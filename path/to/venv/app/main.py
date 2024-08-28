from flask import Flask, Blueprint
from controller.user import listarTodosUsuario, salvarUsuario, listarApenasUmUsuario, atualizarUmUsuario, removerUmUsuario, login

# Criação de um Blueprint para agrupar rotas relacionadas a usuários
blueprint = Blueprint('blueprint', __name__)

# Rota para listar todos os usuários
blueprint.route('/usuarios', methods=['GET'])(listarTodosUsuario)

# Rota para criar um novo usuário
blueprint.route('/usuario', methods=['POST'])(salvarUsuario)

# Rota para listar um único usuário pelo ID
blueprint.route('/usuario/<int:id>', methods=['GET'])(listarApenasUmUsuario)

# Rota para atualizar um usuário existente pelo ID
blueprint.route('/usuario/<int:id>', methods=['PUT'])(atualizarUmUsuario)

# Rota para remover um usuário pelo ID
blueprint.route('/usuario/<int:id>', methods=['DELETE'])(removerUmUsuario)

# Rota para autenticação de usuário (login)
blueprint.route('/login', methods=['POST'])(login)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
