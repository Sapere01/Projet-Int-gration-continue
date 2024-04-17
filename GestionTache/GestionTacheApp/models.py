from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    TYPES_COMPTE = (
        ('standard', 'Standard'),
        ('administrateur', 'Administrateur'),
    )

    type_compte = models.CharField(max_length=20, choices=TYPES_COMPTE, default='standard')
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.username

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
    titre = models.CharField(max_length=100)
    description = models.TextField()
    terminee = models.BooleanField(default=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)


    def __str__(self):
        return self.titre
