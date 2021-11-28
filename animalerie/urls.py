from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.homePage, name="home"),
    path('animal/<str:id_animal>/<str:result>/', views.animal_detail_msg, name='animal_detail_msg'),
    path('animalerie_list/', views.animalerie_list, name='animalerie_list'),
    path('animal/<str:id_animal>/', views.animal_detail, name='animal_detail'),
]

