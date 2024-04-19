from django.db import models
from django.core.validators import MinLengthValidator
from enum import Enum
from django.core.exceptions import ValidationError

# Create your models here.
class AccountType(Enum):
    ADMIN = 'Administrateur'
    USER = 'Standard'

class Utilisateur(models.Model):
    username = models.CharField(unique=True ,max_length=200)
    password = models.CharField(max_length=200, validators=[MinLengthValidator(8)])
    typeCompte = models.CharField(max_length=200, choices=[(t.name, t.value) for t in AccountType], default=AccountType.USER)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def clean_typeCompte(self):
        # Custom validation to ensure valid account type
        value = self.cleaned_data['typeCompte']
        if value not in [t.value for t in AccountType]:
            raise ValidationError(_('Invalid account type'))
        return value


class SessionUtilisateur(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    # session_key = models.CharField(max_length=255, unique=True)
    # Add other relevant fields for your session data

class Tache(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True)

    titre = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    etat = models.BooleanField(default=False) # This value becomes true when the task is completed

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

