import unittest
from unittest.mock import patch

from service.user import (
    listagemTodosUsuariosService, salvarUserService, listarApenasUmUsuarioService,
    atualizarUmUsuarioService, removerUmUsuarioService, loginService
)

class TestServiceUser(unittest.TestCase):
    def setUp(self):
        """Dados mockados que serão reutilizados nos testes"""
        self.sample_user = {"id": 1, "nome": "Test User"}
        self.sample_users_list = [self.sample_user]
        self.login_data = {"email": "test@example.com", "senha": "123456"}
        self.token = {"token": "abc123"}

    # Teste para listar todos os usuários
    @patch('service.user.listagemTodosUsuarios')
    def test_listar_todos_usuarios(self, mock_listar):
        # Configuração do mock
        mock_listar.return_value = self.sample_users_list
        
        # Execução
        result = listagemTodosUsuariosService()
        
        # Verificações
        mock_listar.assert_called_once()
        self.assertEqual(result, self.sample_users_list)
        self.assertIsInstance(result, list)

    # Teste para salvar usuário
    @patch('service.user.salvarUsuario')
    def test_salvar_usuario(self, mock_salvar):
        mock_salvar.return_value = self.sample_user
        
        result = salvarUserService({"nome": "Test User"})
        
        mock_salvar.assert_called_once_with({"nome": "Test User"})
        self.assertEqual(result, self.sample_user)

    # Teste para listar um usuário específico
    @patch('service.user.listarApenasUmUsuario')
    def test_listar_um_usuario(self, mock_listar_um):
        mock_listar_um.return_value = self.sample_user
        
        result = listarApenasUmUsuarioService(1)
        
        mock_listar_um.assert_called_once_with(1)
        self.assertEqual(result, self.sample_user)

    # Teste para atualizar usuário
    @patch('service.user.atualizarUmUsuario')
    def test_atualizar_usuario(self, mock_atualizar):
        updated_user = {"id": 1, "nome": "Updated User"}
        mock_atualizar.return_value = updated_user
        
        result = atualizarUmUsuarioService(1, {"nome": "Updated User"})
        
        mock_atualizar.assert_called_once_with(1, {"nome": "Updated User"})
        self.assertEqual(result, updated_user)

    # Teste para remover usuário
    @patch('service.user.removerUmUsuario')
    def test_remover_usuario(self, mock_remover):
        mock_remover.return_value = True
        
        result = removerUmUsuarioService(1)
        
        mock_remover.assert_called_once_with(1)
        self.assertTrue(result)

    # Teste para login bem-sucedido
    @patch('service.user.login')
    def test_login_sucesso(self, mock_login):
        mock_login.return_value = self.token
        
        result = loginService(self.login_data)
        
        mock_login.assert_called_once_with(self.login_data)
        self.assertEqual(result, self.token)

        
if __name__ == "__main__":
    unittest.main()