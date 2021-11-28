from .models import Animal, Equipement 

def Nourrir(animal, mangeoire):
    if animal.etat != "affamé" :
        message = str("Désolé, "+ animal.id_animal +" n'a pas faim...") 
        result = False 
    elif mangeoire.verifie_disponibilite() == False  :
        message = str("Désolé, la mangeoire est déjà occupée !")
        result = False 
    else : 
        animal.etat = 'repus'
        animal.lieu = mangeoire
        mangeoire.disponibilite = "occupé"
        message = ("Maintenant, " + animal.id_animal + " est repus !")
        result = True 
    return result, message 


def Divertir (animal, roue, ancien_equip):
    if animal.etat != 'repus' :
        message = str("Désolé, " + animal.id_animal + " n'a pas envie de se divertir...")
        result = False
    elif roue.verifie_disponibilite() == False :
        message = str("Désolé, la roue est occupée !")
        result = False
    else :
        animal.etat = 'fatigué'
        animal.lieu = roue
        roue.disponibilitée = 'occupé'
        ancien_equip.disponibilite = "libre"
        message = str("Maintenant, " + animal.id_animal + " est fatigué !")
        result = True
    return result, message 


def Dormir(animal, nid, ancien_equip):
    if animal.etat != 'fatigué' :
        message = str("Désolé, " + animal.id_animal + " n'est pas fatigué...")
        result = False 
    elif nid.verifie_disponibilite() == False :
        message = str("Désolé, le nid est occupé !")
        result = False 
    else : 
        animal.etat = 'endormi'
        animal.lieu = nid 
        nid.disponibilite = 'occupé'
        ancien_equip.disponibilite = 'libre'
        message = str("Maintenant, " + animal.id_animal + " est endormi !")
        result = True
    return result, message 


def Réveiller(animal, litiere, ancien_equip):
    if animal.etat != 'endormi' :
        message = str("Désolé, " + animal.id_animal + " est déjà réveillé...")
        result = False 
    else : 
        animal.etat = 'affamé'
        animal.lieu = litiere 
        ancien_equip.disponibilite = 'libre'
        message = str("Maintenant, " + animal.id_animal + " est réveillé !")
        result = True 
    return result, message


        
