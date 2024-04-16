from django.db import models


# Create your models here.
class Utilisateur(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    typeCompte = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Tache(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True)

    titre = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    etat = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

