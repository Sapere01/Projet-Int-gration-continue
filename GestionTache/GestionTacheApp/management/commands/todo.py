from django.core.management.base import BaseCommand, CommandError
from ...models import Tache, Utilisateur, SessionUtilisateur
from django.db.models import Q

class Command(BaseCommand):
    help = "Gestionnaire interactif de tâches"

    # def add_arguments(self, parser):
    #     parser.add_argument('--m', type=str)
        # parser.add_argument('title', type=str)
        # parser.add_argument('description', type=str)

    def beautify(self):
        print("****************************************************************************")

    def print_error(self, message):
        self.stdout.write("\033[91m{}\033[0m".format(message))
    
    def print_success(self, message):
        print("\033[92m{}\033[0m".format(message))

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
        self.beautify()

        return choice
    
    def login(self):
        username = input("Entrez votre nom d'utilisateur: ")
        password = input("Entrez votre mot de passe: ")

        # Authentication
        try:
            user = Utilisateur.objects.get(username=username)
        except Exception:
            self.print_error("User does not exits")

        if user.password == password :
            # Delete all existing sessions
            SessionUtilisateur.objects.all().delete()
            SessionUtilisateur.objects.create(user=user)

            self.print_success("Successfully logged in as "+username)
        else:
            self.print_error("Invalid username or password")
            self.beautify()

    def logout(self):
        utilisateur = SessionUtilisateur.objects.all().first().user

        SessionUtilisateur.objects.all().delete()

        self.stdout.write(f"{utilisateur.username} Successfully logout.")

    def create__user(self):
        username = input("Entrez votre nom d'utilisateur: ")
        password = input("Entrez votre mot de passe: ")

        if Utilisateur.objects.filter(username=username).exists():
            self.print_error("Erreur: Le nom d'utilisateur "+username+" existe déjà.")
            return

        try:
            user = Utilisateur()
            user.username = username
            user.password = password
            user.save()
            self.print_success("Utilisateur créé: "+username)
        except Exception:
            self.print_error("Erreur lors de la création de l'utilisateur")

    def create__task(self):
        try:
            utilisateur = SessionUtilisateur.objects.all().first().user

            title = input("Entrez le titre de la tâche: ")
            description = input("Entrez une description: ")
            
            Tache.objects.create(titre=title, description=description, utilisateur=utilisateur)
            self.stdout.write(f"Tâche créée: {title}")
        except Exception:
            self.print_error("Aucune session active. Veuillez vous connecter d'abord...")
            self.beautify()

    def print__all_task(self):
        try:
            utilisateur = SessionUtilisateur.objects.all().first().user
            try:
                mes_taches = Tache.objects.filter(
                    Q(utilisateur__username__icontains=utilisateur.username))
                print("******************************** MES TACHES ********************************")
                if mes_taches.count()==0:
                    print("Aucune tâche disponible")
                for tache in mes_taches:
                    self.stdout.write(f"{tache.id} - {tache} : {tache.description}")
                self.beautify()
            except Exception:
                self.print_error("Vous n'avez aucune tâche prévue...")
                self.beautify()
            
        except Exception:
            self.print_error("Aucune session active. Veuillez vous connecter d'abord...")
            self.beautify()

    def mod__task(self):
        task_id = input("Entrez l'id de la tâche: ")

        try:
            utilisateur = SessionUtilisateur.objects.all().first().user

            try:
                task = Tache.objects.get(id=task_id)

                new_titre = input("Entrez le nouveau libellé / Saisir 'no' pour ne pas modifier ce champ: ")
                new_description = input("Entrez la nouvelle description / Saisir 'no' pour ne pas modifier ce champ: ")

                if new_titre != "no":
                    task.titre = new_titre

                if new_description != "no":
                    task.description = new_description

                task.save()
                self.print_success("Tache "+task_id+" modifié avec succès!")
            except Exception:
                self.print_error("Aucune tâche trouvée avec l'id "+task_id)
                self.beautify()
            
        except Exception:
            self.print_error("Aucune session active. Veuillez vous connecter d'abord...")
            self.beautify()

    def del__task(self):
        task_id = input("Entrez l'id de la tâche: ")

        try:
            utilisateur = SessionUtilisateur.objects.all().first().user

            try:
                task_to_del = Tache.objects.get(id=task_id)
                task_to_del.delete()

                self.print_success("Tache "+task_id+" supprimée avec succès!")
            except Exception:
                self.print_error("Aucune tâche trouvée avec l'id "+task_id)
                self.beautify()
            
        except Exception:
            self.print_error("Aucune session active. Veuillez vous connecter d'abord...")
            self.beautify()

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
                    self.print__all_task()
                case '4':
                    self.create__task()
                case '5':
                    self.mod__task()
                case '6':
                    self.del__task()
                case '7':
                    self.stdout.write("Aurevoir")
                    self.logout()
                    is_not_finish = False
                case '9': # Supprimer toutes les tâches
                    tasks = Tache.objects.all()
                    for task in tasks:
                        task.delete()
                case _:
                    self.print_error("Choix invalide. Veuillez réessayer.")


        
        

