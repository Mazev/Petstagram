from django.urls import path

from petstagram.pets.views import list_pets

urlpatterns = [
    path('', list_pets, name= 'list pets')
]