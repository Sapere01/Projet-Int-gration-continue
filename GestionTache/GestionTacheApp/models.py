from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    typeCompte = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def create_logged_user(self, username, type_compte):
        """Creates a logged_user object with limited information."""
        return {
            'id': self.id,
            'username': username,
            'type_compte': type_compte,
        }

class SessionUtilisateur(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    # session_key = models.CharField(max_length=255, unique=True)
    # Add other relevant fields for your session data

class Tache(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True)

    titre = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    etat = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

