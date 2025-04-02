import unittest
from unittest.mock import patch
from controller.user import (
    listagemTodosUsuariosService, salvarUserService, listarApenasUmUsuarioService,
    atualizarUmUsuarioService, removerUmUsuarioService, loginService
)

class TestServiceUser(unittest.TestCase):
    
    def setUp(self):
        """Configura dados comuns para os testes."""
        self.mock_users = [
            {"id": 1, "nome": "Pedro"},
            {"id": 2, "nome": "Chico"}
        ]
        self.mock_user = {"id": 1, "nome": "Robson"}
        self.mock_token = {"token": "1234ABCD"}
        self.mock_login_data = {"email": "teste@teste.com", "senha": "1234567"}

    # Teste: Listar todos os usuários
    @patch('service.user.listagemTodosUsuarios')
    def test_listar_todos_os_usuarios_service(self, mock_listagem):
        # Configura o mock para retornar uma lista de usuários
        mock_listagem.return_value = self.mock_users

        result = listagemTodosUsuariosService()

        mock_listagem.assert_called_once()
        self.assertEqual(result, self.mock_users)

    # Teste: Salvar um novo usuário
    @patch('service.user.salvarUsuario')
    def test_salvar_usuario_service(self, mock_salvar):
        mock_salvar.return_value = self.mock_user

        result = salvarUserService({"nome": "Robson"})

        mock_salvar.assert_called_once_with({"nome": "Robson"})
        self.assertEqual(result, self.mock_user)

    # Teste: Listar um usuário específico (sucesso)
    @patch('service.user.listarApenasUmUsuario')
    def test_listar_apenas_um_usuario_service_success(self, mock_listar):
        mock_listar.return_value = self.mock_user

        result = listarApenasUmUsuarioService(1)

        mock_listar.assert_called_once_with(1)
        self.assertEqual(result, self.mock_user)

    # Teste: Atualizar um usuário
    @patch('service.user.atualizarUmUsuario')
    def test_atualizar_usuario_service(self, mock_atualizar):
        updated_user = {"id": 1, "nome": "Marcos Antonio"}
        mock_atualizar.return_value = updated_user

        result = atualizarUmUsuarioService(1, {"nome": "Marcos Antonio"})

        mock_atualizar.assert_called_once_with(1, {"nome": "Marcos Antonio"})
        self.assertEqual(result, updated_user)

    # Teste: Remover um usuário (sucesso)
    @patch('service.user.removerUmUsuario')
    def test_remover_usuario_service_success(self, mock_remover):
        mock_remover.return_value = True

        result = removerUmUsuarioService(1)

        mock_remover.assert_called_once_with(1)
        self.assertTrue(result)

    # Teste: Login com sucesso
    @patch('service.user.login')
    def test_login_usuario_service_success(self, mock_login):
        mock_login.return_value = self.mock_token

        result = loginService(self.mock_login_data)

        mock_login.assert_called_once_with(self.mock_login_data)

if __name__ == "__main__":
    unittest.main()