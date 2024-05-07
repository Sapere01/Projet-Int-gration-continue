from django.test import TestCase
from unittest.mock import patch
from io import StringIO
from GestionTacheApp.management.commands import todo
from .models import Tache, Utilisateur, SessionUtilisateur

class CommandTestCase(TestCase):

    def setUp(self):
        # Crée un utilisateur de test
        self.data = {
            "username" : "testuser",
            "password" : "12345",
            "typeCompte" : "Standard"
        }
        
        self.user = Utilisateur.objects.create(**self.data)


    def test_create_session(self):
        SessionUtilisateur.objects.create(user=self.user)

    # def test_create_task(self):
    #     # Teste la création d'une tâche
    #     call_command('todo', verbosity=0)
    #     with self.assertRaises(Tache.DoesNotExist):
    #         Tache.objects.get(titre='Test task')

    def test_create_task(self, title='Test Task', description='Test Description'):
        return Tache.objects.create(titre=title, description=description, utilisateur=self.user)

    @patch('builtins.input', side_effect=['testuser', '12345'])
    def test_login_success_and_logout(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.Command.login(self)
            self.assertTrue(SessionUtilisateur.objects.exists())
            self.assertEqual(SessionUtilisateur.objects.first().user, self.user)

        # Test logout here
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.Command.logout(self)
            self.assertFalse(SessionUtilisateur.objects.exists())

    # def test_login_invalid_credentials(self):
    #     with self.assertRaises(SystemExit) as cm:
    #         todo.Command.login(self)
    #     self.assertEqual(str(cm.exception), "Invalid username or password")


    def print_error(self, message):
        print("\033[91m{}\033[0m".format(message))
    
    def print_success(self, message):
        print("\033[92m{}\033[0m".format(message))

