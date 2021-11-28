from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Animal, Equipement
from .controller import Nourrir, Divertir, Dormir, Réveiller  
 
# Create your views here.
def homePage(request):
    return render(request, 'animalerie/home.html')

def animalerie_list(request):
    animals = Animal.objects.filter()
    equipements = Equipement.objects.filter()
    return render(request, 'animalerie/animalerie_list.html', {'animals': animals, 'equipements': equipements})

def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    ancien_equip = Equipement.objects.filter(id_equip = animal.lieu)[0]
    if request.method == "POST" :
        form = MoveForm(request.POST)
        if form.is_valid():
            nom_equip = request.POST['lieu']
            nouveau_equip = Equipement.objects.filter(id_equip = nom_equip)[0]
            if nouveau_equip.id_equip == "Mangeoire" :
                result, message = Nourrir(animal, nouveau_equip)
                print(message)
            if nouveau_equip.id_equip == "Roue" :
                result, message= Divertir(animal, nouveau_equip, ancien_equip)
                print(message)
            if nouveau_equip.id_equip == "Nid" :
                result, message = Dormir(animal, nouveau_equip, ancien_equip)
                print(message)
            if nouveau_equip.id_equip == "Litière" : 
                result, message = Réveiller(animal, nouveau_equip, ancien_equip)
                print(message)
            animal.save()
            ancien_equip.save()
            nouveau_equip.save()
            return render(request, 'animalerie/animal_detail_msg.html', 
                        {'animal': animal, 'result': result, 'message': message, 'form':form})
    else : 
        form = MoveForm(instance=animal)
        return render(request, 'animalerie/animal_detail.html', 
                  {'animal': animal, 'lieu': animal.lieu, 'form': form})
                  

def animal_detail_msg(request, id_animal, result, message): #quand on essaye de déplace un animal
    animal = get_object_or_404(Animal, id_animal=id_animal)
    return render(request, "animalerie/animal_detail_msg.html", {"animals": animal, "result": result, "message" : message})