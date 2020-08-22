from django.db import models

# Create your models here.
class Recruteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    ville = models.TextField(null=True)
    pays = models.CharField(max_length=100)
    email = models.TextField(null=True)
    company = models.CharField(max_length=100)
    aboutMe = models.TextField(null=True)
    password = models.TextField(null=True)

    class Meta:
        verbose_name = "recruteur"
        ordering = ['nom']
    
    def __str__(self):
        return self.nom