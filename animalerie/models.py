from django.db import models
from django.shortcuts import get_object_or_404


class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.id_equip
    
    def verifie_disponibilite(self):
        if self.disponibilite == 'libre' :
            return True 
        else :
            return False 
    
    def change_disponibilite(self):
        if self.id_equip != "litière" :
            self.disponibilite = not self.disponibilite
 

class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_animal

    def change_etat(self, etat):
        self.etat = etat

    def change_lieu(self, lieu):
        self.lieu = lieu 

