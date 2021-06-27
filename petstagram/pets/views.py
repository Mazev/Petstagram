from django.shortcuts import render

from petstagram.pets.models import Pet


def list_pets(request):
    all_pets = Pet.objects.all()

    context = {
        'pets': all_pets
    }

    return render(request, 'pets/pet_list.html',context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)

    context = {
        'pet': pet,
    }
