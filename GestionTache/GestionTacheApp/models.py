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

class Tache(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    terminee = models.BooleanField(default=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)


    def __str__(self):
        return self.titre
