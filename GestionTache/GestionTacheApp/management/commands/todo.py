from django.core.management.base import BaseCommand, CommandError
from ...models import Tache, Utilisateur, SessionUtilisateur

class Command(BaseCommand):
    help = "Gestionnaire interactif de tâches"

    # def add_arguments(self, parser):
    #     parser.add_argument('--m', type=str)
        # parser.add_argument('title', type=str)
        # parser.add_argument('description', type=str)

    def display_menu(self):
        print("Menu Principal")
        print("1. Se connecter")
        print("2. Créer un compte utilisateur")
        print("3. Afficher toutes les tâches")
        print("4. Créer une tâche")
        print("5. Modifier une tâche")
        print("6. Supprimer une tâche")
        print("7. Quitter")

        choice = input("Entrez votre choix (1-7): ")

        print("****************************************")

        return choice
    
    def login(self):
        username = input("Entrez votre nom d'utilisateur: ")
        password = input("Entrez votre mot de passe: ")

        # Authentication
        try:
            user = Utilisateur.objects.get(username=username)
        except:
            self.stdout.write("User does not exits")

        if user.password == password :
            # Delete all existing sessions
            SessionUtilisateur.objects.all().delete()
            SessionUtilisateur.objects.create(user=user)

            self.stdout.write(f"Successfully logged in as {username}")
        else:
            self.stdout.write("Invalid username or password")

    def logout(self):
        utilisateur = SessionUtilisateur.objects.all().first().user

        SessionUtilisateur.objects.all().delete()

        self.stdout.write(f"{utilisateur.username} Successfully logout.")

    def create__user(self):
        username = input("Entrez votre nom d'utilisateur: ")
        password = input("Entrez votre mot de passe: ")

        if Utilisateur.objects.filter(username=username).exists():
            print(f"Erreur: Le nom d'utilisateur '{username}' existe déjà.")
            return

        try:
            user = Utilisateur()
            user.username = username
            user.password = password
            user.save()
            print(f"Utilisateur créé: {username}")
        except Exception as e:
            print(f"Erreur lors de la création de l'utilisateur: {e}")

    def create__task(self):
        try:
            utilisateur = SessionUtilisateur.objects.all().first().user

            title = input("Entrez le titre de la tâche: ")
            description = input("Entrez une description: ")
            
            Tache.objects.create(titre=title, description=description, utilisateur=utilisateur)
            self.stdout.write(f"Tâche créée: {title}")
        except Exception:
            self.stdout.write("Aucune session active. Veuillez vous connecter d'abord.")


    def handle(self, *args, **options):

        is_not_finish = True

        while is_not_finish :
            choice = self.display_menu()

            match choice:
                case '1':
                    self.login()
                case '2':
                    self.create__user()
                case '3':
                    self.create__task()
                case '4':
                    self.create__task()
                case '7':
                    # self.stdout.write(f"Tâche créée: {title}")
                    self.stdout.write("Aurevoir")
                    self.logout()
                    is_not_finish = False
                case _:
                    self.stdout.write("Choix invalide. Veuillez réessayer.")

        
        

